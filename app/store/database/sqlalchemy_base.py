from sqlalchemy.orm import declarative_base

db = declarative_base()

from app.monitor.models import TemperatureModel
