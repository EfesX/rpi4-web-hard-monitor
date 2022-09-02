import typing
from dataclasses import dataclass

if typing.TYPE_CHECKING:
    from app.web.app import Application

@dataclass
class DatabaseConfig:
    host: str = "localhost"
    port: int = 5432
    user: str = "postgres"
    password: str = "123456"
    database: str = ""

@dataclass
class Config:
    database: DatabaseConfig = None

def setup_config(app: "Application", config_path: str):
    pass
