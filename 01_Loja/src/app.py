from flask import Flask
from src.routes.routers import *


app = Flask(__name__)

app.add_url_rule(routes['home'], view_func=routes['test'])

app.register_error_handler(routes['notFound_route'], routes['ne'])