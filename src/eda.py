# src/eda.py
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.stattools import adfuller

def set_plot_style():
    """
    Set consistent plot style.
    """
    sns.set(style="whitegrid", palette="muted")
    plt.rcParams['figure.dpi'] = 300

def plot_closing_prices(df, tickers, save_path):
    """
    Plot closing prices over time for each ticker.
    """
    set_plot_style()
    plt.figure(figsize=(12, 6))
    for ticker in tickers:
        subset = df[df['Ticker'] == ticker]
        plt.plot(subset['Date'], subset['Adj Close'], label=ticker)
    plt.title("Closing Prices Over Time")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.savefig(save_path, dpi=300)
    plt.close()

def plot_daily_returns(df, tickers, save_path):
    """
    Plot daily percentage change for each ticker.
    """
    set_plot_style()
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='Date', y='Daily_Return', hue='Ticker')
    plt.title("Daily Percentage Change")
    plt.savefig(save_path, dpi=300)
    plt.close()

def plot_rolling_volatility(df, tickers, window=30, save_path):
    """
    Plot rolling volatility for each ticker.
    """
    set_plot_style()
    df['Rolling_30d_Vol'] = df.groupby("Ticker")['Daily_Return'].rolling(window=window).std().reset_index(0, drop=True)
    plt.figure(figsize=(12, 6))
    for ticker in tickers:
        subset = df[df['Ticker'] == ticker]
        plt.plot(subset['Date'], subset['Rolling_30d_Vol'], label=ticker)
    plt.title(f"{window}-Day Rolling Volatility")
    plt.xlabel("Date")
    plt.ylabel("Volatility")
    plt.legend()
    plt.savefig(save_path, dpi=300)
    plt.close()

def detect_outliers(df, ticker):
    """
    Detect outliers in daily returns using 3-std rule.
    """
    subset = df[df['Ticker'] == ticker]
    mean = subset['Daily_Return'].mean()
    std = subset['Daily_Return'].std()
    outliers = subset[(subset['Daily_Return'] > mean + 3*std) | (subset['Daily_Return'] < mean - 3*std)]
    return outliers[['Date', 'Daily_Return']]

def adf_test(series, ticker):
    """
    Perform ADF test for stationarity.
    """
    result = adfuller(series.dropna())
    return {
        'Ticker': ticker,
        'ADF Statistic': result[0],
        'p-value': result[1],
        'Stationary': '✅ Stationary' if result[1] < 0.05 else '❌ Non-Stationary'
    }