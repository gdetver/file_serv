from aiohttp import web
from apps.file_serv.router import routes

app = web.Application()

for route in routes:
    app.router.add_route(route[0], route[1], route[2])
