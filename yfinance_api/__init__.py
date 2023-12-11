from flask import Flask
from .api import add_api_routes


def create_app() -> Flask:
    app = Flask(__name__)

    add_api_routes(app)

    return app
