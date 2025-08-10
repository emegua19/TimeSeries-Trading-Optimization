# src/data_cleaning.py
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def clean_data(df):
    """
    Handle missing values and print data summary.
    """
    print("\nMissing values before cleaning:\n", df.isnull().sum())
    df = df.groupby("Ticker", group_keys=False).apply(lambda x: x.ffill().bfill())
    print("\nData Types:\n", df.dtypes)
    print("\nBasic statistics:\n", df.groupby("Ticker")['Adj Close'].describe())
    return df

def scale_adj_close(df):
    """
    Scale Adjusted Close prices per ticker using MinMaxScaler.
    """
    scaler = MinMaxScaler()
    df['Adj_Close_Scaled'] = df.groupby("Ticker", group_keys=False)['Adj Close'] \
        .transform(lambda x: scaler.fit_transform(x.values.reshape(-1, 1)).flatten())
    return df

def calculate_daily_returns(df):
    """
    Calculate daily percentage returns.
    """
    df['Daily_Return'] = df.groupby("Ticker")['Adj Close'].pct_change()
    return df