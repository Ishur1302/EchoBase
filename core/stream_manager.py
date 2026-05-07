import asyncio

async def manage_stream(websocket, orchestrator):
    while True:
        data = await websocket.recv()
        # Process audio in a non-blocking background task
        asyncio.create_task(orchestrator.handle_audio_stream(data))
