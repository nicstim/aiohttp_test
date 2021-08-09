from app.settings import BASE_DIR
from app.views import index


def setup_routes(app):
    app.router.add_get('/', index)


def setup_static_routes(app):
    app.router.add_static('/static/',
                          path=BASE_DIR / 'static',
                          name='static')
