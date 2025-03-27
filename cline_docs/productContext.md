# Product Context: Speech-to-Speech Application with NVIDIA ACE

## Why This Project Exists

This project aims to create a speech-to-speech conversational AI application using NVIDIA's Avatar Cloud Engine (ACE) framework with custom speech components. The application will use OpenAI Whisper API for speech-to-text (STT) and ElevenLabs API for text-to-speech (TTS) instead of the default NVIDIA Riva components.

## Problems It Solves

1. **Customizable Speech Components**: While ACE provides a comprehensive framework for conversational AI, it is tightly integrated with NVIDIA's Riva services for speech components. This project demonstrates how to replace these components with alternative services like OpenAI Whisper and ElevenLabs.

2. **Flexible Deployment**: By using Docker containers, the application can be easily deployed in various environments without complex setup procedures.

3. **Future Extensibility**: The architecture is designed to be scalable, allowing for future integration with animation components like Audio2Face and Animation Graph for creating animated avatars.

4. **Conversational AI**: The application provides a natural language interface for users to interact with, similar to the chitchat example in ACE.

## How It Should Work

1. **User Input**: The user speaks into a microphone, and the audio is captured by the custom speech client.

2. **Speech-to-Text**: The audio is sent to the OpenAI Whisper API, which transcribes it into text.

3. **Conversation Processing**: The transcribed text is sent to the ACE Chat Engine through Redis event streams, which processes the input and generates a response based on the conversational context.

4. **Text-to-Speech**: The response text is sent to the ElevenLabs API, which converts it into natural-sounding speech.

5. **User Output**: The synthesized speech is played back to the user.

6. **Future Animation**: In future iterations, the audio can also be sent to Audio2Face for generating facial animations, and the Animation Graph can coordinate body movements for a fully animated avatar.

The application uses a hybrid architecture that leverages ACE's event-based interface while integrating custom speech components. This approach allows for the flexibility of using preferred speech APIs while maintaining compatibility with the ACE framework for future extensions.
