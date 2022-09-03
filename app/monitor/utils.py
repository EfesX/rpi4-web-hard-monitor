from datetime import datetime
import datetime

import psutil

from app.monitor.models import CPUInfoModel

def get_cpu_info() -> CPUInfoModel:
    temp = psutil.sensors_temperatures()
    workload = psutil.cpu_percent()
    frequency = psutil.cpu_freq()
    #ram_usage = psutil.virtual_memory().percent

    return CPUInfoModel(
        temperature = float(temp['cpu_thermal'][0].current),
        workload = float(workload),
        frequency = float(frequency.current),
        datetime = datetime.datetime.today(),
    )
