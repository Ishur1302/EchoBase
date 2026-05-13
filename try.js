const socket = new WebSocket('ws://localhost:8080');
socket.binaryType = 'arraybuffer';

socket.onopen = () => {
    console.log('EchoBase Connection Established');
};
async function startStreaming() {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.ondataavailable = (e) => socket.send(e.data);
    mediaRecorder.start(100); // Send chunks every 100ms
}
function drawWaveform(stream) {
    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    const source = audioContext.createMediaStreamSource(stream);
    const analyser = audioContext.createAnalyser();
    source.connect(analyser);
    console.log("Visualizer initialized: Analyzing PCM data...");
}
