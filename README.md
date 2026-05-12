# EchoBase 🎙️
A high-performance toolkit for building low-latency, voice-integrated AI agents.

## Structure
- `core/voice-engine`: Processing Real-time audio (WebRTC/LiveKit).
- `core/llm-bridge`: Handling streaming responses from AWS Bedrock/OpenAI.
- `web/dashboard`: Monitoring agent performance and latency.
## Next Steps
- [ ] Integrate ElevenLabs/Amazon Polly for Streaming TTS.
- [ ] Add WebRTC data channel for ultra-low latency control signals.
## Frontend
- Integrated WebSocket client for low-latency audio transmission.
- Implemented MediaRecorder API for browser-based voice capture.
