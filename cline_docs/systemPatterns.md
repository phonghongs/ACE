# System Patterns: Speech-to-Speech Application with NVIDIA ACE

## How the System is Built

The system is built using a hybrid architecture that combines NVIDIA ACE components with custom speech components. The architecture follows these key patterns:

1. **Microservices Architecture**: The system is composed of multiple independent services, each responsible for a specific function:
   - ACE Chat Engine: Handles conversation logic
   - Redis: Manages event streams
   - Custom Whisper ASR: Handles speech-to-text
   - Custom ElevenLabs TTS: Handles text-to-speech

2. **Event-Driven Architecture**: The system uses Redis event streams for communication between components, allowing for asynchronous processing and loose coupling.

3. **Docker Containerization**: Each component runs in its own Docker container, providing isolation, portability, and ease of deployment.

4. **API Integration**: The system integrates with external APIs (OpenAI Whisper and ElevenLabs) for speech processing.

## Key Technical Decisions

1. **Using ACE Event Interface**: We chose to use ACE's event interface (`speech_umim` pipeline) because it provides a more flexible and extensible architecture compared to the server interface. This allows for easier integration with custom components and future animation capabilities.

2. **Replacing Riva with External APIs**: We decided to replace NVIDIA's Riva ASR and TTS components with OpenAI Whisper and ElevenLabs APIs to leverage their advanced capabilities and flexibility.

3. **Redis for Event Streaming**: We chose Redis for event streaming because it's already integrated with ACE's event interface and provides reliable message delivery with minimal overhead.

4. **Docker for Deployment**: We decided to use Docker for deployment to ensure consistency across environments and simplify the setup process.

5. **Hybrid Approach**: Rather than building a completely custom solution or using ACE as-is, we chose a hybrid approach that leverages ACE's strengths while replacing components that didn't meet our requirements.

## Architecture Patterns

### Component Interaction Flow

```
User Audio → Custom Whisper ASR → Redis Event Stream → ACE Chat Engine → Redis Event Stream → Custom ElevenLabs TTS → Audio Output
```

### Event-Based Communication

The system uses Redis event streams for communication between components:
- ASR results are published to the `ace:events:in` stream
- Bot responses are published to the `ace:events:out` stream
- Components subscribe to relevant streams to receive events

### Extensibility Points

The architecture includes several extensibility points for future enhancements:
- The ElevenLabs TTS component can be extended to send audio to Audio2Face
- Additional event handlers can be added to process events from the Redis streams
- The bot configuration can be customized to support different conversation flows

### Error Handling and Resilience

The system includes error handling and resilience mechanisms:
- Components can reconnect to Redis if the connection is lost
- API calls include error handling and retry logic
- The system can continue operating even if some components fail

This architecture provides a solid foundation for the speech-to-speech application while allowing for future extensions and improvements.
