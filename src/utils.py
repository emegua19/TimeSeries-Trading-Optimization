# src/utils.py
import numpy as np
import pandas as pd

def calculate_risk_metrics(df, tickers, risk_free_rate=0.04/252):
    """
    Calculate VaR (95%) and Sharpe Ratio for each ticker.
    """
    risk_metrics = {}
    for ticker in tickers:
        returns = df[df['Ticker'] == ticker]['Daily_Return'].dropna()
        var_95 = np.percentile(returns, 5)
        sharpe_ratio = (returns.mean() - risk_free_rate) / returns.std() * np.sqrt(252)
        risk_metrics[ticker] = {"VaR(95%)": var_95, "Sharpe Ratio": sharpe_ratio}
    return pd.DataFrame(risk_metrics).T