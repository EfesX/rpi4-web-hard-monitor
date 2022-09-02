import yaml

import typing
from dataclasses import dataclass

if typing.TYPE_CHECKING:
    from app.web.app import Application

@dataclass
class DatabaseConfig:
    url: str = ""

@dataclass
class Config:
    database: DatabaseConfig = None

def setup_config(app: "Application", config_path: str):
    with open(config_path, "r") as f:
        raw_config = yaml.safe_load(f)

    print(raw_config["database"]["url"])

    app.config = Config(
        database=DatabaseConfig(
            url=raw_config["database"]["url"]
        )
    )


