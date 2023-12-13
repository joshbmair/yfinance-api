from flask import Flask, abort, jsonify, request
from yfinance import Ticker


def __get_ticker_from_header() -> str:
    try:
        return request.headers['ticker']
    except KeyError:
        abort(400, description='Ticker not given')


def _add_ticker_api_routes(app: Flask) -> None:
    @app.get('/api/actions')
    def actions(): return _actions()

    @app.get('/api/balance-sheet')
    def balance_sheet(): return _balance_sheet()

    @app.get('/api/cash-flow')
    def cash_flow(): return _cash_flow()

    @app.get('/api/capital-gains')
    def capital_gains(): return _capital_gains()

    @app.get('/api/dividends')
    def dividends(): return _dividends()

    @app.get('/api/fast-info')
    def fast_info(): return _fast_info()

    @app.get('/api/financials')
    def financials(): return _financials()

    @app.get('/api/history-metadata')
    def history_metadata(): return _history_metadata()

    @app.get('/api/income-stmt')
    def income_stmt(): return _income_stmt()

    @app.get('/api/info')
    def info(): return _info()

    @app.get('/api/institutional-holders')
    def institutional_holders(): return _institutional_holders()

    @app.get('/api/isin')
    def isin(): return _isin()

    @app.get('/api/major-holders')
    def major_holders(): return _major_holders()

    @app.get('/api/mutualfund-holders')
    def mutualfund_holders(): return _mutualfund_holders()

    @app.get('/api/news')
    def news(): return _news()

    @app.get('/api/splits')
    def splits(): return _splits()


def _actions() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_actions().to_json()


def _balance_sheet() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_balance_sheet().to_json()


def _cash_flow() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_cash_flow().to_json()


def _capital_gains() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_capital_gains()


def _dividends() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_dividends().to_json()


def _fast_info() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_fast_info().toJSON()


def _financials() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_financials().to_json()


def _history_metadata() -> str:
    ticker: str = __get_ticker_from_header()
    return jsonify(Ticker(ticker).get_history_metadata())


def _income_stmt() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_income_stmt().to_json()


def _info() -> str:
    ticker: str = __get_ticker_from_header()
    return jsonify(Ticker(ticker).get_info())


def _institutional_holders() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_institutional_holders()


def _isin() -> str:
    ticker: str = __get_ticker_from_header()
    return jsonify(Ticker(ticker).get_isin())


def _major_holders() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_major_holders().to_json()


def _mutualfund_holders() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_mutualfund_holders().to_json()


def _news() -> str:
    ticker: str = __get_ticker_from_header()
    return jsonify(Ticker(ticker).get_news())


def _splits() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_splits().to_json()
