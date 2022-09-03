from datetime import datetime
import typing
from typing import Optional, List

from app.base.base_accessor import BaseAccessor
from app.monitor.models import (
    CPUInfoModel,
    CPUInfo
)

from app.monitor.acquirer import Acquirer

from sqlalchemy import (
    select
)

from sqlalchemy.engine import (
    ChunkedIteratorResult
)

if typing.TYPE_CHECKING:
    from app.web.app import Application


class MonitorAccessor(BaseAccessor):
    def __init__(self, app: "Application", *args, **kwargs):
        super().__init__(app, *args, **kwargs)

        self.acquirer: Acquirer = Acquirer(app)

    async def start(self, app: "Application", period: int):
        await self.acquirer.start(period)

    async def stop(self, app: "Application"):
        await self.acquirer.stop()

    async def list_cpu_info(self, count: int) -> List[CPUInfo]:
        Q1 = select(CPUInfoModel).order_by(CPUInfoModel.datetime.desc()).limit(count)

        res: List[CPUInfo] = []

        async with self.app.database._session() as session:
            cir: ChunkedIteratorResult = await session.execute(Q1)
            for row in cir:
                for obj in row:
                    res.append(
                        obj.dump()
                    ) 
        return res

    async def insert_cpu_info(self, temp: CPUInfoModel):
        async with self.app.database._session() as session:
            session.add(temp)
            await session.commit()


