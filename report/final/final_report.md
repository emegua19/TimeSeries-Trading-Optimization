# Time Series Trading Optimization

## Abstract
This project focuses on developing a robust pipeline for time series-based trading optimization, incorporating forecasting models, portfolio optimization, and backtesting strategies. We use historical stock and ETF data to demonstrate a complete quantitative finance workflow.

---

## Table of Contents
1. [Introduction](#introduction)  
2. [Data Collection & Preprocessing](#data-collection--preprocessing)  
3. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)  
4. [Modeling](#modeling)  
   - [ARIMA Forecasting](#arima-forecasting)  
   - [LSTM Forecasting](#lstm-forecasting)  
5. [Portfolio Optimization](#portfolio-optimization)  
6. [Backtesting](#backtesting)  
7. [Results](#results)  
8. [Conclusion](#conclusion)  
9. [References](#references)  

---

## Introduction
The goal of this project is to design and evaluate trading strategies using time series forecasting and portfolio optimization techniques. The methodology integrates:
- **Data preprocessing**
- **Exploratory analysis**
- **Model selection and evaluation**
- **Risk-adjusted portfolio allocation**
- **Backtesting for performance validation**

---

## Data Collection & Preprocessing
We collected daily adjusted closing prices for the following assets:
- **TSLA** (Tesla)
- **SPY** (S&P 500 ETF)
- **BND** (Vanguard Total Bond Market ETF)

The raw datasets were cleaned and transformed to:
- Handle missing values
- Align dates across assets
- Calculate returns and volatility metrics

---

## Exploratory Data Analysis (EDA)
The EDA involved:
- Visualizing price trends and return distributions
- Computing rolling volatility
- Analyzing asset correlations
- Identifying stationarity for model suitability

---

## Modeling

### ARIMA Forecasting
- **Purpose:** Predict short- and medium-term price movements  
- **Process:**  
  - Differencing to ensure stationarity  
  - Model selection via AIC minimization  
  - Forecast horizons: **30 days** and **12 months**  
- **Metrics Evaluated:** RMSE, MAE, MAPE

### LSTM Forecasting
- **Purpose:** Capture nonlinear dependencies in time series  
- **Process:**  
  - Normalization of input data  
  - Sliding window sequences  
  - Early stopping to prevent overfitting  
- **Metrics Evaluated:** RMSE, MAE, MAPE

---

## Portfolio Optimization
- **Method:** Mean-Variance Optimization (Markowitz Model)  
- **Inputs:** Forecasted returns from ARIMA & LSTM models  
- **Output:** Asset weights that maximize the Sharpe Ratio  
- Efficient frontier plots generated to visualize trade-offs between return and risk.

---

## Backtesting
- **Approach:** Simulated trading over historical data using optimized portfolio weights  
- **Benchmark:** Equal-weight portfolio of the same assets  
- **Metrics:**  
  - Cumulative returns  
  - Annualized volatility  
  - Sharpe ratio

---

## Results
- **ARIMA** performed well for short-term forecasts but lagged in long horizons.  
- **LSTM** captured longer-term trends better but required more data preprocessing.  
- Portfolio optimization improved Sharpe ratios over the benchmark.  
- Backtesting showed **reduced volatility** and **improved risk-adjusted returns** compared to the benchmark.

---

## Conclusion
The pipeline successfully integrates:
- Time series forecasting
- Quantitative portfolio optimization
- Backtesting for strategy evaluation

Future work:
- Incorporating more assets
- Exploring alternative models like Prophet, XGBoost
- Implementing live trading integration

---

## References
1. Box, G. E., & Jenkins, G. M. (1976). *Time Series Analysis: Forecasting and Control*. Holden-Day.  
2. Hochreiter, S., & Schmidhuber, J. (1997). *Long Short-Term Memory*. Neural Computation, 9(8), 1735–1780.  
3. Markowitz, H. (1952). *Portfolio Selection*. Journal of Finance, 7(1), 77–91.
