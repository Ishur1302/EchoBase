const socket = new WebSocket('ws://localhost:8080');
socket.binaryType = 'arraybuffer';

socket.onopen = () => {
    console.log('EchoBase Connection Established');
};
