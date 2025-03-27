#!/usr/bin/env python3
"""
Whisper ASR Component for Speech-to-Speech Application

This component captures audio from the microphone, sends it to the OpenAI Whisper API
for transcription, and publishes the results to Redis for the ACE Chat Engine.

This implementation includes:
1. Two-pass End of Utterance (EOU) detection for lower latency
2. Support for interim transcripts to trigger early responses
3. Spurious transcript filtering to avoid unnecessary interruptions
"""

import os
import time
import json
import logging
import threading
import numpy as np
import pyaudio
import redis
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("whisper-asr")

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    logger.error("OPENAI_API_KEY environment variable not set")
    exit(1)

# Initialize Redis client
REDIS_HOST = os.getenv("REDIS_HOST", "redis-server")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

# Audio configuration
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024
RECORD_SECONDS = 5  # Record in chunks of 5 seconds
SILENCE_THRESHOLD = int(os.getenv("SILENCE_THRESHOLD", "500"))  # Threshold for silence detection

# EOU (End of Utterance) configuration
FIRST_PASS_SILENCE = 0.24  # 240ms silence for first pass (interim) transcript
SECOND_PASS_SILENCE = 0.8  # 800ms silence for second pass (final) transcript

# Spurious transcript filtering
FILTER_WORDS = [
    "yeah", "okay", "right", "yes", "yum", "and", "one", "all", 
    "when", "thank", "but", "next", "what", "i see", "the", 
    "hmm", "mmm", "so that", "why", "that", "well"
]
INCLUDE_WORDS = ["hi", "hello"]

class WhisperASR:
    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.stream = None
        self.is_recording = False
        self.frames = []
        self.last_activity = time.time()
        self.first_pass_timeout = FIRST_PASS_SILENCE  # First pass silence timeout (interim)
        self.second_pass_timeout = SECOND_PASS_SILENCE  # Second pass silence timeout (final)
        self.current_transcript = ""
        self.last_interim_time = 0
        self.processing_interim = False

    def start_recording(self):
        """Start recording audio from the microphone"""
        if self.is_recording:
            return

        logger.info("Starting audio recording")
        self.stream = self.audio.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK
        )
        self.is_recording = True
        self.frames = []
        self.last_activity = time.time()
        self.current_transcript = ""
        self.last_interim_time = 0
        self.processing_interim = False

        # Start recording thread
        threading.Thread(target=self._record_audio, daemon=True).start()

    def _record_audio(self):
        """Record audio in a separate thread with two-pass EOU detection"""
        interim_frames = []
        silence_duration = 0
        
        while self.is_recording:
            data = self.stream.read(CHUNK, exception_on_overflow=False)
            self.frames.append(data)
            interim_frames.append(data)
            
            # Check for silence
            audio_data = np.frombuffer(data, dtype=np.int16)
            is_silent = np.abs(audio_data).mean() <= SILENCE_THRESHOLD
            
            if is_silent:
                silence_duration += CHUNK / RATE
                
                # First pass EOU detection (interim transcript)
                if silence_duration >= self.first_pass_timeout and not self.processing_interim:
                    self.processing_interim = True
                    # Process interim transcript in a separate thread
                    interim_audio_data = b''.join(interim_frames)
                    threading.Thread(
                        target=self._process_interim_audio,
                        args=(interim_audio_data,),
                        daemon=True
                    ).start()
                
                # Second pass EOU detection (final transcript)
                if silence_duration >= self.second_pass_timeout:
                    logger.info("Final silence threshold reached, stopping recording")
                    self.stop_recording()
                    self.process_audio(is_final=True)
                    break
            else:
                silence_duration = 0
                self.last_activity = time.time()

            # Process audio after a certain duration regardless of silence
            if len(self.frames) * CHUNK / RATE >= RECORD_SECONDS:
                self.process_audio(is_final=False)
                self.frames = []

    def _process_interim_audio(self, audio_data):
        """Process interim audio for lower latency responses"""
        try:
            # Save audio to temporary file
            temp_file = f"temp_interim_{time.time()}.wav"
            with open(temp_file, "wb") as f:
                f.write(audio_data)
            
            # Send to Whisper API
            with open(temp_file, "rb") as f:
                transcript = openai.Audio.transcribe("whisper-1", f)
            
            text = transcript["text"].strip()
            
            if text and not self._is_spurious(text):
                logger.info(f"Interim transcription: {text}")
                self._publish_to_redis(text, is_final=False)
                self.last_interim_time = time.time()
            else:
                logger.info("No interim transcription or spurious transcript detected")
                
            # Clean up temporary file
            os.remove(temp_file)
            
        except Exception as e:
            logger.error(f"Error processing interim audio: {e}")
        finally:
            self.processing_interim = False

    def _is_spurious(self, text):
        """Filter spurious transcripts and filler words"""
        text_lower = text.lower()
        
        # Filter short transcripts unless they're in the include list
        if len(text) < 3 and text_lower not in INCLUDE_WORDS:
            return True
            
        # Filter common filler words
        if text_lower in FILTER_WORDS:
            return True
            
        return False

    def stop_recording(self):
        """Stop recording audio"""
        if not self.is_recording:
            return

        logger.info("Stopping audio recording")
        self.is_recording = False
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None

    def process_audio(self, is_final=True):
        """Process recorded audio with Whisper API"""
        if not self.frames:
            return

        logger.info(f"Processing {'final' if is_final else 'chunk of'} audio with Whisper API")
        
        # Convert frames to audio file
        audio_data = b''.join(self.frames)
        
        try:
            # Save audio to temporary file
            temp_file = f"temp_audio_{time.time()}.wav"
            with open(temp_file, "wb") as f:
                f.write(audio_data)
            
            # Send to Whisper API
            with open(temp_file, "rb") as f:
                transcript = openai.Audio.transcribe("whisper-1", f)
            
            text = transcript["text"].strip()
            
            if text and not self._is_spurious(text):
                logger.info(f"Transcription: {text}")
                self._publish_to_redis(text, is_final=is_final)
                self.current_transcript = text
            else:
                logger.info("No transcription or spurious transcript detected")
                
            # Clean up temporary file
            os.remove(temp_file)
            
        except Exception as e:
            logger.error(f"Error processing audio: {e}")

    def _publish_to_redis(self, text, is_final=True):
        """Publish transcription to Redis"""
        try:
            event_data = {
                "event_type": "speech_recognition_result",
                "text": text,
                "is_final": is_final,
                "timestamp": time.time()
            }
            
            redis_client.xadd(
                "ace:events:in",
                {"data": json.dumps(event_data)}
            )
            logger.info(f"Published {'final' if is_final else 'interim'} transcription to Redis")
            
            # If user starts speaking while bot is responding, send interrupt event
            if is_final:
                interrupt_data = {
                    "event_type": "user_interrupt",
                    "timestamp": time.time()
                }
                
                redis_client.xadd(
                    "ace:events:out",
                    {"data": json.dumps(interrupt_data)}
                )
                logger.info("Published user interrupt event to Redis")
                
        except Exception as e:
            logger.error(f"Error publishing to Redis: {e}")

    def run(self):
        """Run the ASR service"""
        logger.info("Whisper ASR service starting")
        
        try:
            while True:
                logger.info("Waiting for speech...")
                self.start_recording()
                time.sleep(0.1)  # Small delay to prevent CPU hogging
        except KeyboardInterrupt:
            logger.info("Stopping Whisper ASR service")
        finally:
            self.stop_recording()
            self.audio.terminate()

if __name__ == "__main__":
    asr = WhisperASR()
    asr.run()
