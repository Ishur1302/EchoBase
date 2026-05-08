import asyncio

class VoiceLock:
    def __init__(self):
        self.lock = asyncio.Lock()

    async def acquire_to_speak(self):
        return await self.lock.acquire()

    def release_speech(self):
        if self.lock.locked():
            self.lock.release()
