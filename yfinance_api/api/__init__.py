from flask import Flask
from .ticker import _add_ticker_api_routes

def add_api_routes(app: Flask):
    _add_ticker_api_routes(app)
