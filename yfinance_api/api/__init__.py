from flask import Flask
from .download_endpoint import _add_download_endpoint
from .json_endpoints import _add_json_endpoints


def add_api_routes(app: Flask):
    _add_download_endpoint(app)
    _add_json_endpoints(app)
