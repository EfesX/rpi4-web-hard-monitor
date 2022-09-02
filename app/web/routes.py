from aiohttp.web_app import Application

def setup_routes(app: Application):
    from app.monitor.routes import setup_routes as monitor_setup_routes
    
    monitor_setup_routes(app)