from datetime import datetime
import datetime

import psutil

from app.monitor.models import TemperatureModel

def get_cpu_temperature() -> TemperatureModel:
    temps = psutil.sensors_temperatures()

    return TemperatureModel(
        temp = float(temps['cpu_thermal'][0].current),
        datetime = datetime.datetime.today()
    )