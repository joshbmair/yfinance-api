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

    @app.get('/api/analyst-price-target')
    def analyst_price_target(): return _analyst_price_target()

    @app.get('/api/balance-sheet')
    def balance_sheet(): return _balance_sheet()

    @app.get('/api/balance-sheet-time-series')
    def balance_sheet_time_series(): return _balance_sheet_time_series()

    @app.get('/api/calendar')
    def calendar(): return _calendar()

    @app.get('/api/cash-flow')
    def cash_flow(): return _cash_flow()

    @app.get('/api/capital-gains')
    def capital_gains(): return _capital_gains()

    @app.get('/api/dividends')
    def dividends(): return _dividends()

    @app.get('/api/earnings')
    def earnings(): return _earnings()

    @app.get('/api/earnings-dates')
    def earnings_dates(): return _earnings_dates()

    @app.get('/api/earnings-forecast')
    def earnings_forecast(): return _earnings_forecast()

    @app.get('/api/earnings-trend')
    def earnings_trend(): return _earnings_trend()

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

    @app.get('/api/recommendations')
    def recommendations(): return _recommendations()

    @app.get('/api/recommendations-summary')
    def recommendations_summary(): return _recommendations_summary()

    @app.get('/api/rev-forecast')
    def rev_forecast(): return _rev_forecast()

    @app.get('/api/shares')
    def shares(): return _shares()

    @app.get('/api/shares-full')
    def shares_full(): return _shares_full()

    @app.get('/api/splits')
    def splits(): return _splits()

    @app.get('/api/sustainability')
    def sustainability(): return _sustainability()

    @app.get('/api/trend-details')
    def trend_details(): return _trend_details()


def _actions() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_actions().to_json()


def _analyst_price_target() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_analyst_price_target().to_json()


def _balance_sheet() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_balance_sheet().to_json()


def _balance_sheet_time_series() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_balance_sheet_time_series().to_json()


def _calendar() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_calendar().to_json()


def _cash_flow() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_cash_flow().to_json()


def _capital_gains() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_capital_gains().to_json()


def _dividends() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_dividends().to_json()


def _earnings() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_earnings().to_json()


def _earnings_dates() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_earnings_dates().to_json()


def _earnings_forecast() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_earnings_forecast().to_json()


def _earnings_trend() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_earnings_trend().to_json()


def _fast_info() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_fast_info().to_json()


def _financials() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_financials().to_json()


def _history_metadata() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_history_metadata().to_json()


def _income_stmt() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_income_stmt().to_json()


def _info() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_info().to_json()


def _institutional_holders() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_institutional_holders().to_json()


def _isin() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_isin().to_json()


def _major_holders() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_major_holders().to_json()


def _mutualfund_holders() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_mutualfund_holders().to_json()


def _news() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_news().to_json()


def _recommendations() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_recommendations().to_json()


def _recommendations_summary() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_recommendations_summary().to_json()


def _rev_forecast() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_rev_forecast().to_json()


def _shares() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_shares().to_json()


def _shares_full() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_shares_full().to_json()


def _splits() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_splits().to_json()


def _sustainability() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_sustainability().to_json()


def _trend_details() -> str:
    ticker: str = __get_ticker_from_header()
    return Ticker(ticker).get_trend_details().to_json()
