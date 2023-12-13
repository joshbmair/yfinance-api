# Y!Finance API

The Y!Finance API provides what the official Yahoo! Finance API did until it was shut down. Using the Python libraries [Flask](https://pypi.org/project/Flask/) the [yfinance](https://pypi.org/project/yfinance/) library, Y!Finance API serves financial data from [Yahoo! Finance](https://finance.yahoo.com/).


## How to run the app

1. Use the virtual environment: `python3 -m venv .venv`
1. Install the required dependencies: `pip3 install -r requirements.txt`
1. Run the app: `flask --app yfinance_api run`


## Endpoints

### Ticker

The ticker endpoints serve data about a specific stock ticker. Each endpoint requires a `ticker` parameter. For example: `http://127.0.0.1:5000/api/ticker/actions?ticker=MSFT`.

Here are all the endpoints:

* `/api/ticker/actions`
* `/api/ticker/balance-sheet`
* `/api/ticker/cash-flow`
* `/api/ticker/capital-gains`
* `/api/ticker/dividends`
* `/api/ticker/fast-info`
* `/api/ticker/financials`
* `/api/ticker/history-metadata`
* `/api/ticker/income-stmt`
* `/api/ticker/info`
* `/api/ticker/institutional-holders`
* `/api/ticker/isin`
* `/api/ticker/major-holders`
* `/api/ticker/mutualfund-holders`
* `/api/ticker/news`
* `/api/ticker/splits`
