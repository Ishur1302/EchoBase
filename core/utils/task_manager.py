import asyncio

class TaskManager:
    def __init__(self):
        self.active_tasks = set()

    def add_task(self, coro):
        task = asyncio.create_task(coro)
        self.active_tasks.add(task)
        task.add_done_callback(self.active_tasks.discard)
        return task

    def cancel_all(self):
        for task in self.active_tasks:
            task.cancel()
        self.active_tasks.clear()
