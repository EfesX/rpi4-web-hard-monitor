from app.web.app import View

from app.monitor.models import TemperatureModel
from app.monitor.utils import get_cpu_temperature


class StartAcquireView(View):
    async def get(self):
        await self.store.monitor.start(self.request.app)

class StopAcquireView(View):
    async def get(self):
        await self.store.monitor.stop(self.request.app)



class TempView(View):
    async def get(self):
        temp: TemperatureModel = get_cpu_temperature()
        print(temp.temp)
        print(temp.datetime)
        
