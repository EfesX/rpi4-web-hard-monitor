import typing


if typing.TYPE_CHECKING:
    from app.web.app import Application


def setup_routes(app: "Application"):
    from app.monitor.views import TempView
    app.router.add_view("/api/temp", TempView)
