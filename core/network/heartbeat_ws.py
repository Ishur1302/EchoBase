import asyncio

async def start_heartbeat(websocket, interval=30):
    while True:
        try:
            await websocket.ping()
            await asyncio.sleep(interval)
        except Exception:
            break
