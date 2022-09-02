from typing import Optional

from aiohttp.web import (
    Application as AiohttpApplication,
    Request as AiohttpRequest,
    View as AiohttpView,
)

from app.web.routes import setup_routes
from app.web.config import setup_config
from app.store import setup_store

from app.web.config import Config
from app.store import Store
from app.store.database.database import Database


class Application(AiohttpApplication):
    config: Optional[Config] = None
    store: Optional[Store] = None
    database: Optional[Database] = None

class Request(AiohttpRequest):
    @property
    def app(self) -> Application:
        return super().app()

class View(AiohttpView):
    @property
    def request(self) -> Request:
        return super().request

    @property
    def data(self) -> dict:
        return self.request.get("data", {})

app = Application()


def setup_app(config_path: str) -> Application:
    setup_config(app, "./config.yml")
    setup_store(app)
    setup_routes(app)
    return app