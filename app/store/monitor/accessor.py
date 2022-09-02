from datetime import datetime
import typing
from typing import Optional

from app.base.base_accessor import BaseAccessor
from app.monitor.models import TemperatureModel

from app.monitor.acquirer import Acquirer

from sqlalchemy import (
    insert
)

if typing.TYPE_CHECKING:
    from app.web.app import Application


class MonitorAccessor(BaseAccessor):
    def __init__(self, app: "Application", *args, **kwargs):
        super().__init__(app, *args, **kwargs)

        self.acquirer: Acquirer = Acquirer(app)

    async def start(self, app: "Application"):
        await self.acquirer.start()

    async def stop(self, app: "Application"):
        await self.acquirer.stop()

    async def list_cpu_temp(self):
        raise NotImplementedError

    async def insert_cpu_temp(self, temp: TemperatureModel):
        async with self.app.database._session() as session:
            session.add(temp)
            await session.commit()

