# Y!Finance API

The Y!Finance API provides what the official Yahoo! Finance API did until it was shut down. Using the Python libraries [Flask](https://pypi.org/project/Flask/) the [yfinance](https://pypi.org/project/yfinance/) library, Y!Finance API serves financial data from [Yahoo! Finance](https://finance.yahoo.com/).


## How to run the app

1. Use the virtual environment: `python3 -m venv .venv`
1. Install the required dependencies: `pip3 install -r requirements.txt`
1. Run the app: `flask --app yfinance_api run`


## Endpoints

The endpoints serve JSON data about a specific stock ticker -- With the exception of `/api/download`, which responds with a CSV file. Each endpoint requires a `ticker` parameter. For example: `http://127.0.0.1:5000/api/actions?ticker=MSFT`.

Here are all the endpoints:

* `/api/actions`
* `/api/balance-sheet`
* `/api/cash-flow`
* `/api/capital-gains`
* `/api/dividends`
* `/api/downloads`
* `/api/fast-info`
* `/api/financials`
* `/api/history-metadata`
* `/api/income-stmt`
* `/api/info`
* `/api/institutional-holders`
* `/api/isin`
* `/api/major-holders`
* `/api/mutualfund-holders`
* `/api/news`
* `/api/splits`
