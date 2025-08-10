# tests/test_data_pipeline.py
import pytest
import pandas as pd
from src.data_fetch import fetch_yfinance_data
from src.data_cleaning import clean_data, scale_adj_close

def test_fetch_yfinance_data():
    df = fetch_yfinance_data('TSLA', '2015-07-01', '2025-07-31', 'data/raw/test.csv')
    assert isinstance(df, pd.DataFrame)
    assert 'Adj Close' in df.columns
    assert 'Ticker' in df.columns

def test_clean_data():
    df = pd.DataFrame({'Ticker': ['TSLA'], 'Adj Close': [100, None], 'Date': ['2020-01-01', '2020-01-02']})
    cleaned_df = clean_data(df)
    assert cleaned_df['Adj Close'].isnull().sum() == 0

def test_scale_adj_close():
    df = pd.DataFrame({'Ticker': ['TSLA'], 'Adj Close': [100, 200], 'Date': ['2020-01-01', '2020-01-02']})
    scaled_df = scale_adj_close(df)
    assert 'Adj_Close_Scaled' in scaled_df.columns
    assert scaled_df['Adj_Close_Scaled'].between(0, 1).all()