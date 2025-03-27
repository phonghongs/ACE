#!/usr/bin/env python3
"""
HTTP Server for ElevenLabs TTS Component

This server exposes an HTTP endpoint that ACE can use to request TTS synthesis.
It acts as a bridge between ACE's expected TTS interface and our custom ElevenLabs implementation.
"""

import os
import io
import json
import logging
import elevenlabs
from dotenv import load_dotenv
from flask import Flask, request, Response, stream_with_context

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("elevenlabs-tts-server")

# Initialize ElevenLabs client
elevenlabs.api_key = os.getenv("ELEVENLABS_API_KEY")
if not elevenlabs.api_key:
    logger.error("ELEVENLABS_API_KEY environment variable not set")
    exit(1)

# Create Flask app
app = Flask(__name__)

@app.route('/tts', methods=['POST'])
def tts():
    """
    TTS endpoint that ACE will call to synthesize speech.
    
    Expected request format:
    {
        "text": "Text to synthesize",
        "voice_name": "Voice name (e.g., Adam)",
        "model_name": "Model name (e.g., eleven_monolingual_v1)",
        "language_code": "Language code (e.g., en-US)",
        "sample_rate_hz": 44100
    }
    
    Returns:
        Streaming audio response in PCM format
    """
    try:
        # Parse request
        data = request.json
        text = data.get('text', '')
        voice_name = data.get('voice_name', 'Adam')
        model_name = data.get('model_name', 'eleven_monolingual_v1')
        
        if not text:
            return Response(json.dumps({"error": "No text provided"}), 
                           status=400, 
                           mimetype='application/json')
        
        logger.info(f"Synthesizing speech for: {text}")
        logger.info(f"Using voice: {voice_name}, model: {model_name}")
        
        # Generate audio using ElevenLabs with streaming for lower latency
        audio_stream = elevenlabs.generate(
            text=text,
            voice=voice_name,
            model=model_name,
            stream=True,  # Enable streaming for lower latency
            optimize_streaming_latency=3  # Optimize for low latency
        )
        
        # Stream the audio response
        def generate():
            for chunk in audio_stream:
                yield chunk
        
        return Response(stream_with_context(generate()), 
                       mimetype='audio/pcm')
        
    except Exception as e:
        logger.error(f"Error synthesizing speech: {e}")
        return Response(json.dumps({"error": str(e)}), 
                       status=500, 
                       mimetype='application/json')

if __name__ == '__main__':
    # Get port from environment or use default
    port = int(os.getenv('PORT', 5000))
    
    # Run server
    logger.info(f"Starting ElevenLabs TTS server on port {port}")
    app.run(host='0.0.0.0', port=port)
