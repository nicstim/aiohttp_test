from aiohttp import web
import aiohttp_jinja2
import jinja2

from app.db import init_pg, close_pg
from app.middlewares import setup_middlewares
from app.routes import setup_routes
from app.settings import config, BASE_DIR

app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(BASE_DIR / 'app' / 'templates')))
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)
setup_routes(app)
setup_middlewares(app)
app['config'] = config
web.run_app(app, host='127.0.0.1', port=8000)
