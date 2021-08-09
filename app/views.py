import aiohttp_jinja2
from app import db


@aiohttp_jinja2.template('pages/index.html')
async def index(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(db.user.select(),)
        records = await cursor.fetchall()
        users = [dict(q) for q in records]
        return {"users": users}
