# Enhanced Speech-to-Speech Application with NVIDIA ACE

This project implements an enhanced speech-to-speech conversational AI application using NVIDIA's Avatar Cloud Engine (ACE) framework with custom speech components. The application uses OpenAI Whisper API for speech-to-text (STT) and ElevenLabs API for text-to-speech (TTS) instead of the default NVIDIA Riva components.

## Features

- **Speech-to-speech conversation** with a conversational AI bot
- **Custom speech components** using OpenAI Whisper and ElevenLabs
- **Low latency** with two-pass End of Utterance (EOU) detection
- **Barge-in support** for natural conversation flow
- **Event-based architecture** using Redis for communication
- **Docker-based deployment** for easy setup
- **Extensible** for future integration with animation components

## Prerequisites

- Docker and Docker Compose
- OpenAI API key for Whisper
- ElevenLabs API key
- (Optional) NGC API key for pulling ACE images
- Audio input/output capabilities

## Setup

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Set up API keys:
   - Edit the `.env` file and add your OpenAI API key and ElevenLabs API key
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
   ```
   - (Optional) Add your NGC API key if you need to pull ACE images

3. Build and start the application:
   ```bash
   docker-compose up -d
   ```

4. Access the web UI:
   - Open a web browser and navigate to `http://localhost:7006/`

## Usage

1. Start the application using Docker Compose:
   ```bash
   docker-compose up -d
   ```

2. Speak into your microphone to interact with the bot
   - The Whisper ASR component will transcribe your speech
   - The ACE Chat Engine will process your input and generate a response
   - The ElevenLabs TTS component will convert the response to speech

3. Experience enhanced conversation features:
   - **Low latency responses**: The system uses a two-pass approach to detect the end of your speech, starting to process your input after just 240ms of silence
   - **Barge-in capability**: You can interrupt the bot while it's speaking, and it will stop and listen to you
   - **Natural conversation flow**: The system filters out spurious transcripts and filler words

4. Stop the application:
   ```bash
   docker-compose down
   ```

## Architecture

The application uses a hybrid architecture that leverages ACE's event-based interface while integrating custom speech components:

```
User Audio → Whisper ASR → Redis Event Stream → ACE Chat Engine → Redis Event Stream → ElevenLabs TTS → Audio Output
```

- **Whisper ASR**: Captures audio from the microphone, sends it to the OpenAI Whisper API for transcription, and publishes the results to Redis
- **ACE Chat Engine**: Processes the transcribed text and generates a response based on the conversational context
- **ElevenLabs TTS**: Listens for bot responses from Redis, sends the text to the ElevenLabs API for speech synthesis, and plays the audio back to the user
- **Redis**: Provides event streaming for communication between components
- **Chat Controller**: Manages the conversation flow and coordinates between components

## Advanced Features

### Low Latency with Two-Pass EOU

The system uses a two-pass approach to detect the end of user speech:
- First pass (240ms): Triggers an interim transcript for early processing
- Second pass (800ms): Confirms the final transcript

This approach reduces perceived latency while maintaining transcription quality.

### Barge-In Support

The system supports barge-in, allowing users to interrupt the bot while it's speaking:
- When user speech is detected during bot speech, the TTS playback is stopped
- The system then processes the new user input
- This creates a more natural conversation flow

### Spurious Transcript Filtering

The system filters out spurious transcripts and filler words to avoid unnecessary interruptions and improve conversation quality.

## Future Extensions

The architecture is designed to be scalable for future integration with animation components:

- **Audio2Face**: Can be integrated to generate facial animations from the synthesized speech
- **Animation Graph**: Can be integrated to coordinate body movements for a fully animated avatar

## Troubleshooting

- **Audio Issues**: Make sure your microphone and speakers are properly configured and accessible to Docker
- **API Key Issues**: Verify that your API keys are correctly set in the `.env` file
- **Docker Issues**: Make sure Docker and Docker Compose are properly installed and running
- **Latency Issues**: If you experience high latency, check your internet connection as the system relies on external APIs

## License

This project is licensed under the MIT License - see the LICENSE file for details.
