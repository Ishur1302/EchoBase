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
### Tech Stack Architecture
- **Frontend**: JavaScript (MediaRecorder API, WebSockets)
- **Backend**: Python (Asyncio, AWS Bedrock)
- **Protocol**: Binary PCM over WS
## Voice Engine Specifications
- **Sample Rate**: 16,000 Hz (Mono)
- **VAD**: RMS-based thresholding (500 units)
- **Security**: Regex-based transcript sanitization
