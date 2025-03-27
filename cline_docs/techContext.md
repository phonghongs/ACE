# Technical Context

## Current Technology Stack
- Docker/Kubernetes deployment
- Python microservices
- NVIDIA Riva for ASR/TTS
- NVIDIA NeMo Guardrails for conversation flow
- Colang for dialog management

## New Technology Requirements
- Whisper OpenAI API for ASR
- ElevenLabs API for TTS
- OpenAI API for LLM
- Python client libraries for all APIs

## Development Setup
- Docker Desktop required
- Kubernetes cluster (local or cloud)
- API keys for:
  - OpenAI (Whisper + LLM)
  - ElevenLabs
- Python 3.8+ environment

## Configuration Needs
- API endpoint URLs
- Authentication keys
- Rate limiting considerations
- Audio format compatibility
