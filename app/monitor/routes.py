import typing


if typing.TYPE_CHECKING:
    from app.web.app import Application


def setup_routes(app: "Application"):
    from app.monitor.views import CPUInfoListView
    from app.monitor.views import StartAcquireView
    from app.monitor.views import StopAcquireView

    app.router.add_view("/api/list_cpu_info", CPUInfoListView)
    app.router.add_view("/api/acq_start", StartAcquireView)
    app.router.add_view("/api/acq_stop", StopAcquireView)
