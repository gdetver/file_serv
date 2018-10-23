#!/usr/bin/python3.5
from aiohttp import web
from apps.file_serv import app

web.run_app(app)
