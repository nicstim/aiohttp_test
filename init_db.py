from sqlalchemy import create_engine, MetaData

from app.settings import config
from app.db import user


DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"


def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[user])


def sample_data(engine):
    conn = engine.connect()
    conn.execute(user.insert(), [
        {'username': 'admin',
         'password': 'admin',
         'is_staff': True}
    ])
    conn.close()


if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    engine = create_engine(db_url)

    create_tables(engine)
    sample_data(engine)
