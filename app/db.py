from sqlalchemy import MetaData, Table, Column, Integer, String, Boolean
import aiopg.sa


meta = MetaData()

user = Table(
    'user', meta,

    Column('id', Integer, primary_key=True),
    Column('username', String(200), nullable=False),
    Column('password', String(200), nullable=False),
    Column('is_staff', Boolean, unique=False, default=False),
)


async def init_pg(app):
    conf = app['config']['postgres']
    engine = await aiopg.sa.create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
        minsize=conf['minsize'],
        maxsize=conf['maxsize'],
    )
    app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()
