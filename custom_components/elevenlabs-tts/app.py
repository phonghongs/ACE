#!/usr/bin/env python3
"""
ElevenLabs TTS Component for Speech-to-Speech Application

This component listens for bot responses from Redis, sends the text to the ElevenLabs API
for speech synthesis, and plays the audio back to the user.

This implementation includes:
1. Support for barge-in (interruption during speech)
2. Streaming response handling for more responsive interactions
3. Integration with ACE's event-based architecture
"""

import os
import time
import json
import logging
import threading
import io
import numpy as np
import pyaudio
import redis
import elevenlabs
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("elevenlabs-tts")

# Initialize ElevenLabs client
elevenlabs.api_key = os.getenv("ELEVENLABS_API_KEY")
if not elevenlabs.api_key:
    logger.error("ELEVENLABS_API_KEY environment variable not set")
    exit(1)

# Initialize Redis client
REDIS_HOST = os.getenv("REDIS_HOST", "redis-server")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

# Audio configuration
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

class ElevenLabsTTS:
    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.voice_id = os.getenv("ELEVENLABS_VOICE_ID", "Adam")
        self.model_id = os.getenv("ELEVENLABS_MODEL_ID", "eleven_monolingual_v1")
        self.last_id = "0-0"  # Redis stream ID
        self.is_playing = False
        self.stop_event = threading.Event()
        
        # Subscribe to user speech events to enable barge-in
        self.speech_thread = threading.Thread(target=self._listen_for_speech_events, daemon=True)
        self.speech_thread.start()

    def _listen_for_speech_events(self):
        """Listen for user speech events to enable barge-in"""
        logger.info("Listening for user speech events for barge-in")
        
        speech_last_id = "0-0"
        while True:
            try:
                # Read from Redis stream for speech recognition events
                streams = redis_client.xread(
                    {"ace:events:in": speech_last_id},
                    block=1000,
                    count=1
                )
                
                if not streams:
                    continue
                
                for stream_name, messages in streams:
                    for message_id, data in messages:
                        speech_last_id = message_id
                        
                        # Process message
                        if b'data' in data:
                            try:
                                event_data = json.loads(data[b'data'].decode('utf-8'))
                                # If we detect user speech and we're currently playing audio, stop it (barge-in)
                                if event_data.get("event_type") == "speech_recognition_result" and self.is_playing:
                                    logger.info("Barge-in detected: User started speaking, stopping TTS playback")
                                    self.stop_event.set()
                            except json.JSONDecodeError:
                                pass
            
            except Exception as e:
                logger.error(f"Error reading speech events from Redis: {e}")
                time.sleep(1)  # Wait before retrying

    def listen_for_responses(self):
        """Listen for bot responses from Redis"""
        logger.info("Listening for bot responses from Redis")
        
        while True:
            try:
                # Read from Redis stream
                streams = redis_client.xread(
                    {"ace:events:out": self.last_id},
                    block=1000,
                    count=1
                )
                
                if not streams:
                    continue
                
                for stream_name, messages in streams:
                    for message_id, data in messages:
                        self.last_id = message_id
                        
                        # Process message
                        if b'data' in data:
                            self._process_message(data[b'data'].decode('utf-8'))
            
            except Exception as e:
                logger.error(f"Error reading from Redis: {e}")
                time.sleep(1)  # Wait before retrying

    def _process_message(self, data_str):
        """Process a message from Redis"""
        try:
            data = json.loads(data_str)
            
            # Check if this is a bot response event
            if data.get("event_type") == "bot_response" and "text" in data:
                text = data["text"]
                logger.info(f"Received bot response: {text}")
                self._synthesize_speech(text)
            
            # Check for user interruption event
            elif data.get("event_type") == "user_interrupt" and self.is_playing:
                logger.info("Received explicit interruption event, stopping TTS playback")
                self.stop_event.set()
            
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON data: {data_str}")
        except Exception as e:
            logger.error(f"Error processing message: {e}")

    def _synthesize_speech(self, text):
        """Synthesize speech using ElevenLabs API"""
        if not text:
            return
        
        try:
            logger.info(f"Synthesizing speech for: {text}")
            
            # Generate audio using ElevenLabs with streaming for lower latency
            audio_stream = elevenlabs.generate(
                text=text,
                voice=self.voice_id,
                model=self.model_id,
                stream=True,  # Enable streaming for lower latency
                optimize_streaming_latency=3  # Optimize for low latency
            )
            
            # Play the audio stream
            self._play_audio_stream(audio_stream)
            
        except Exception as e:
            logger.error(f"Error synthesizing speech: {e}")

    def _play_audio(self, audio_data):
        """Play audio data"""
        if self.is_playing:
            self.stop_event.set()  # Stop any currently playing audio
            time.sleep(0.1)  # Give time for the current playback to stop
        
        self.stop_event.clear()
        self.is_playing = True
        
        # Start playback in a separate thread
        threading.Thread(
            target=self._play_audio_thread,
            args=(audio_data, self.stop_event),
            daemon=True
        ).start()

    def _play_audio_stream(self, audio_stream):
        """Play streaming audio data for lower latency"""
        if self.is_playing:
            self.stop_event.set()  # Stop any currently playing audio
            time.sleep(0.1)  # Give time for the current playback to stop
        
        self.stop_event.clear()
        self.is_playing = True
        
        # Start playback in a separate thread
        threading.Thread(
            target=self._play_audio_stream_thread,
            args=(audio_stream, self.stop_event),
            daemon=True
        ).start()

    def _play_audio_thread(self, audio_data, stop_event):
        """Play audio in a separate thread"""
        try:
            # Convert audio data to stream
            audio_io = io.BytesIO(audio_data)
            
            # Open stream
            stream = self.audio.open(
                format=self.audio.get_format_from_width(2),  # 16-bit audio
                channels=CHANNELS,
                rate=RATE,
                output=True
            )
            
            # Play audio
            logger.info("Playing audio")
            
            while True:
                if stop_event.is_set():
                    break
                
                data = audio_io.read(CHUNK)
                if not data:
                    break
                
                stream.write(data)
            
            # Clean up
            stream.stop_stream()
            stream.close()
            
            logger.info("Audio playback complete")
            
        except Exception as e:
            logger.error(f"Error playing audio: {e}")
        finally:
            self.is_playing = False

    def _play_audio_stream_thread(self, audio_stream, stop_event):
        """Play streaming audio in a separate thread for lower latency"""
        try:
            # Open stream
            stream = self.audio.open(
                format=self.audio.get_format_from_width(2),  # 16-bit audio
                channels=CHANNELS,
                rate=RATE,
                output=True
            )
            
            # Play audio stream
            logger.info("Playing audio stream")
            
            for chunk in audio_stream:
                if stop_event.is_set():
                    break
                
                stream.write(chunk)
            
            # Clean up
            stream.stop_stream()
            stream.close()
            
            if not stop_event.is_set():
                logger.info("Audio playback complete")
            else:
                logger.info("Audio playback interrupted")
            
        except Exception as e:
            logger.error(f"Error playing audio stream: {e}")
        finally:
            self.is_playing = False

    def run(self):
        """Run the TTS service"""
        logger.info("ElevenLabs TTS service starting")
        
        try:
            self.listen_for_responses()
        except KeyboardInterrupt:
            logger.info("Stopping ElevenLabs TTS service")
        finally:
            self.audio.terminate()

if __name__ == "__main__":
    tts = ElevenLabsTTS()
    tts.run()
