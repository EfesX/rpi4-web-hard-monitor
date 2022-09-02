from app.base.base_accessor import BaseAccessor

class MonitorAccessor(BaseAccessor):
    async def list_cpu_temp(self):
        raise NotImplementedError


