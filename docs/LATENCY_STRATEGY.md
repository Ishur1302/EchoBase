# Low-Latency Voice Strategy
To achieve <500ms response times, we implement:
1. **VAD (Voice Activity Detection):** Start processing the moment the user stops speaking.
2. **Streaming TTS:** Begin audio playback while the LLM is still generating the rest of the sentence.
3. **WebRTC over WebSockets:** Reducing transport layer overhead.
