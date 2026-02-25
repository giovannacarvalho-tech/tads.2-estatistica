import yfinance as yf
import pandas as pd


def download_data(ticker:str = 'TSLA') -> pd.DataFrame:
    df = yf.download(
        ticker,
        period='max',
        multi_level_index=False).reset_index()
    return df
