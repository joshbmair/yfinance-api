from flask import Flask, abort, request
from yfinance import Ticker


def __get_ticker_from_header() -> str:
    try:
        return request.headers['ticker']
    except KeyError:
        abort(400, description='Ticker not given')


def _add_ticker_api_routes(app: Flask) -> None:
    @app.get('/api/actions')
    def actions(): return _actions()


def _actions() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).actions.to_json()
