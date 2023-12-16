import pandas as pd
import yfinance as yf
from flask import Flask, Response, abort, request, send_file
from io import BytesIO


def _add_download_endpoint(app: Flask) -> None:
    @app.get('/api/download')
    def respond_download() -> Response:
        ticker: str = request.args.get('ticker')

        if ticker == None:
            abort(400, description='Ticker not given')

        csv_file = BytesIO()
        df: pd.DataFrame = yf.download(ticker)
        df.to_csv(csv_file, index=False)
        csv_file.seek(0)

        return send_file(csv_file, 'text/csv', True, f'{ticker}.csv')
