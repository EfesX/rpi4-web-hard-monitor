from typing import Optional

from aiohttp.web import (
    Application as AiohttpApplication,
    Request as AiohttpRequest,
    View as AiohttpView,
)

from app.web.routes import setup_routes
from app.web.config import setup_config
from app.store import setup_store
from app.web.middlewares import setup_middlewares

from app.web.config import Config
from app.store import Store
from app.store.database.database import Database

from aiohttp_apispec import setup_aiohttp_apispec


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

    @property
    def store(self) -> Store:
        return self.request.app.store

app = Application()


def setup_app(config_path: str) -> Application:
    setup_config(app, config_path)
    setup_routes(app)
    setup_aiohttp_apispec(app, title="RPi4 Hard Monitor", url="/docs/json", swagger_path="/docs")
    setup_middlewares(app)
    setup_store(app)
    
    return app
