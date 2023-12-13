import json
from typing import Any, Callable
from flask import Flask, Response, abort, jsonify, request
from yfinance import Ticker


def _get_endpoint_map() -> dict[str, Callable]:
    return {
        'actions': _actions,
        'balance-sheet': _balance_sheet,
        'cash-flow': _cash_flow,
        'capital-gains': _capital_gains,
        'dividends': _dividends,
        'fast-info': _fast_info,
        'financials': _financials,
        'history-metadata': _history_metadata,
        'income-stmt': _income_stmt,
        'info': _info,
        'institutional-holders': _institutional_holders,
        'isin': _isin,
        'major-holders': _major_holders,
        'mutualfund-holders': _mutualfund_holders,
        'news': _news,
        'splits': _splits
    }


def _add_ticker_api_routes(app: Flask) -> None:
    @app.get('/api/<endpoint>')
    def ticker_callback(endpoint: str) -> Response:
        endpoint_map: dict[str, Callable] = _get_endpoint_map()

        try:
            ticker: str = request.headers['ticker']
        except KeyError:
            abort(400, description='Ticker not given')

        result: Any = endpoint_map[endpoint](ticker.upper())

        if type(result) == str:
            result = json.loads(result)

        return jsonify(result)


def _actions(ticker: str) -> str:
    return Ticker(ticker).get_actions().to_json()


def _balance_sheet(ticker: str) -> str:
    return Ticker(ticker).get_balance_sheet().to_json()


def _cash_flow(ticker: str) -> str:
    return Ticker(ticker).get_cash_flow().to_json()


def _capital_gains(ticker: str) -> list:
    return Ticker(ticker).get_capital_gains()


def _dividends(ticker: str) -> str:
    return Ticker(ticker).get_dividends().to_json()


def _fast_info(ticker: str) -> str:
    return Ticker(ticker).get_fast_info().toJSON()


def _financials(ticker: str) -> str:
    return Ticker(ticker).get_financials().to_json()


def _history_metadata(ticker: str) -> str:
    return str(Ticker(ticker).get_history_metadata())


def _income_stmt(ticker: str) -> str:
    return Ticker(ticker).get_income_stmt().to_json()


def _info(ticker: str) -> dict:
    return Ticker(ticker).get_info()


def _institutional_holders(ticker: str) -> str:
    return Ticker(ticker).get_institutional_holders().to_json()


def _isin(ticker: str) -> str:
    return f'"{Ticker(ticker).get_isin()}"'


def _major_holders(ticker: str) -> str:
    return Ticker(ticker).get_major_holders().to_json()


def _mutualfund_holders(ticker: str) -> str:
    return Ticker(ticker).get_mutualfund_holders().to_json()


def _news(ticker: str) -> list:
    return Ticker(ticker).get_news()


def _splits(ticker: str) -> str:
    return Ticker(ticker).get_splits().to_json()
