# EchoBase Network Topology

1. **Client**: Captures audio (PCM 16-bit).
2. **WebSocket**: Streams chunks to `core/network`.
3. **Orchestrator**: Dispatches to VAD and LLM.
4. **Bedrock**: Returns text tokens via AWS SDK.
5. **TTS**: Streams audio back to Client.
