from app.web.app import View

from app.monitor.models import CPUInfoModel
from app.monitor.utils import get_cpu_info

from app.web.utils import json_response

from app.monitor.schemes import (
    CPUInfoListSchemaRequest,
    CPUInfoSchema,
    CPUInfoStartAcquireRequest,
)

from aiohttp_apispec import (
    querystring_schema,
    response_schema
)

from marshmallow import Schema

class StartAcquireView(View):
    @querystring_schema(CPUInfoStartAcquireRequest)
    async def get(self):
        period = abs(int(self.request.query.get('period')))

        await self.store.monitor.start(self.request.app, period)
        return json_response(
            data={
                "start": True,
            }
        )

class StopAcquireView(View):
    @querystring_schema(Schema)
    async def get(self):
        await self.store.monitor.stop(self.request.app)
        return json_response(
            data={
                "stop": True,
            }
        )

class CPUInfoListView(View):
    @querystring_schema(CPUInfoListSchemaRequest)
    async def get(self):
        count = abs(int(self.request.query.get('count')))
        
        cpuinfolist = await self.request.app.store.monitor.list_cpu_info(count)

        return json_response(
            data={
                "cpu_info": [CPUInfoSchema().dump(obj) for obj in cpuinfolist]
            }
        )
        
