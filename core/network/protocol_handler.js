class VoiceProtocol {
    static decodeChunk(buffer) {
        // Standard Int16 PCM decoding
        return new Int16Array(buffer);
    }
}
