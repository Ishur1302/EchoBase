import asyncio

class StreamBackpressure:
    def __init__(self, max_buffer_size=10):
        self.queue = asyncio.Queue(maxsize=max_buffer_size)

    async def push_chunk(self, chunk):
        # This will block if the queue is full, slowing down the LLM ingest
        await self.queue.put(chunk)

    async def pop_chunk(self):
        return await self.queue.get()
