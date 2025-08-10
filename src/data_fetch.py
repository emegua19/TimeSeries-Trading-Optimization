# src/data_fetch.py
import yfinance as yf
import pandas as pd
import os

def fetch_yfinance_data(ticker, start_date, end_date, save_path):
    """
    Fetch historical data from YFinance and save to raw directory.
    """
    df = yf.download(ticker, start=start_date, end=end_date, auto_adjust=False, progress=False)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]
    df.reset_index(inplace=True)
    df['Ticker'] = ticker
    df.to_csv(save_path, index=False)
    return df

def fetch_all_tickers(tickers, start_date, end_date, raw_path):
    """
    Fetch data for multiple tickers and combine into a single DataFrame.
    """
    df_list = []
    for ticker in tickers:
        save_path = os.path.join(raw_path, f"{ticker}_20150701_20250731_raw.csv")
        df = fetch_yfinance_data(ticker, start_date, end_date, save_path)
        df_list.append(df)
    return pd.concat(df_list, ignore_index=True)