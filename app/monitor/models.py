from dataclasses import dataclass
from app.store.database.sqlalchemy_base import db
from sqlalchemy import Column, DateTime, Float


@dataclass
class CPUInfo:
    datetime: DateTime
    temperature: float
    frequency: float
    workload: float

class CPUInfoModel(db):
    __tablename__ = "cpu_info"
    
    datetime = Column("datetime", DateTime, primary_key = True)
    temperature = Column("temperature", Float)
    frequency = Column("frequency", Float)
    workload = Column("workload", Float)

    def __repr__(self) -> str:
        return f"CPUInfo(datetime: {self.datetime}, temp: {self.temperature}, freq: {self.frequency}, load: {self.workload})"

    def dump(self) -> CPUInfo:
        return CPUInfo(
            datetime = self.datetime,
            temperature = self.temperature,
            frequency = self.frequency,
            workload = self.workload,
        )
