import asyncio
from asyncio import Task
import typing
from typing import Optional

from app.store import Store

import app.monitor.utils as mutils

if typing.TYPE_CHECKING:
    from app.web.app import Application


class Acquirer:
    def __init__(self, app: "Application") -> None:
        self.app = app
        self.is_running = False
        self.acquire_task: Optional[Task] = None
        self.interval = 15

    async def start(self, period: int):
        if self.is_running == False:
            self.interval = period
            self.is_running = True
            self.acquire_task = asyncio.create_task(self.acquire())

    async def stop(self):
        if self.is_running == True:
            self.is_running = False
            try:
                await asyncio.wait_for(self.acquire_task, timeout=(self.interval + 1))
            except asyncio.TimeoutError:
                pass
        
    async def acquire(self):
        while self.is_running:
            await self.app.store.monitor.insert_cpu_info(mutils.get_cpu_info())
            await asyncio.sleep(self.interval)

