# EchoBase Voice Pipeline
1. **Ingest:** WebSocket receives 16kHz PCM.
2. **Detect:** VAD identifies end-of-turn.
3. **Stream:** AWS Bedrock generates text.
4. **Chunk:** Sentence Splitter creates TTS-ready segments.
5. **Output:** High-priority phrases sent to TTS first to reduce 'Time to First Byte'.
