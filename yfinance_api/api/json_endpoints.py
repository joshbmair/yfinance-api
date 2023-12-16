import json
from typing import Any, Callable
from flask import Flask, Response, abort, jsonify, request, send_file
from yfinance import Ticker


def __get_endpoint_map() -> dict[str, Callable]:
    return {
        'actions': __actions,
        'balance-sheet': __balance_sheet,
        'cash-flow': __cash_flow,
        'capital-gains': __capital_gains,
        'dividends': __dividends,
        'fast-info': __fast_info,
        'financials': __financials,
        'history-metadata': __history_metadata,
        'income-stmt': __income_stmt,
        'info': __info,
        'institutional-holders': __institutional_holders,
        'isin': __isin,
        'major-holders': __major_holders,
        'mutualfund-holders': __mutualfund_holders,
        'news': __news,
        'splits': __splits
    }


def _add_json_endpoints(app: Flask) -> None:
    @app.get('/api/<endpoint>')
    def respond(endpoint: str) -> Response:
        ticker: str = request.args.get('ticker')

        if ticker == None:
            abort(400, description='Ticker not given')

        endpoint_map: dict[str, Callable] = __get_endpoint_map()
        result: Any = endpoint_map[endpoint](ticker.upper())

        if type(result) == str:
            result = json.loads(result)

        return jsonify(result)


def __actions(ticker: str) -> str:
    return Ticker(ticker).get_actions().to_json()


def __balance_sheet(ticker: str) -> str:
    return Ticker(ticker).get_balance_sheet().to_json()


def __cash_flow(ticker: str) -> str:
    return Ticker(ticker).get_cash_flow().to_json()


def __capital_gains(ticker: str) -> list:
    return Ticker(ticker).get_capital_gains()


def __dividends(ticker: str) -> str:
    return Ticker(ticker).get_dividends().to_json()


def __fast_info(ticker: str) -> str:
    return Ticker(ticker).get_fast_info().toJSON()


def __financials(ticker: str) -> str:
    return Ticker(ticker).get_financials().to_json()


def __history_metadata(ticker: str) -> str:
    return str(Ticker(ticker).get_history_metadata())


def __income_stmt(ticker: str) -> str:
    return Ticker(ticker).get_income_stmt().to_json()


def __info(ticker: str) -> dict:
    return Ticker(ticker).get_info()


def __institutional_holders(ticker: str) -> str:
    return Ticker(ticker).get_institutional_holders().to_json()


def __isin(ticker: str) -> str:
    return f'"{Ticker(ticker).get_isin()}"'


def __major_holders(ticker: str) -> str:
    return Ticker(ticker).get_major_holders().to_json()


def __mutualfund_holders(ticker: str) -> str:
    return Ticker(ticker).get_mutualfund_holders().to_json()


def __news(ticker: str) -> list:
    return Ticker(ticker).get_news()


def __splits(ticker: str) -> str:
    return Ticker(ticker).get_splits().to_json()
