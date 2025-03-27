# System Patterns

## ACE Agent 4.1 Architecture
- Microservices-based architecture
- Core components:
  - Chat Controller (orchestrates pipeline)
  - Chat Engine (conversation flow)
  - NLP Server (NLP tasks)
  - Plugin Server (business logic)
  - Web App (frontend)

## Current Integration Points
- Uses NVIDIA Riva for ASR/TTS by default
- Supports custom LLM integration
- Conversation flows defined in Colang
- Supports RAG workflows

## New Integration Requirements
- Replace ASR with Whisper OpenAI API
- Replace TTS with ElevenLabs API
- Configure OpenAI LLM
- Maintain existing chat controller/engine
- Keep Docker/Kubernetes deployment
