from app.store.database.sqlalchemy_base import db
from sqlalchemy import Column, Integer, DateTime

class TemperatureModel(db):
    __tablename__ = "temperatures"
    
    datetime = Column(DateTime, primary_key = True)
    temp = Column(Integer)
    