# Interim Task 1 Report: Data Preprocessing and Exploratory Data Analysis

**10 Academy Week 11 Challenge: Portfolio Forecasting**  
**Author:** Yitbarek Geletaw  
**GitHub:** [TimeSeries-Trading-Optimization](https://github.com/emegua19/TimeSeries-Trading-Optimization)  
**Date:** August 10, 2025  

---

## Table of Contents
1. [Introduction](#introduction)
2. [Data Overview](#data-overview)
3. [Data Cleaning](#data-cleaning)
4. [Exploratory Data Analysis](#exploratory-data-analysis)
5. [Outlier Detection](#outlier-detection)
6. [Stationarity Testing](#stationarity-testing)
7. [Risk Metrics](#risk-metrics)
8. [Insights](#insights)
9. [Future Work](#future-work)

---

## Introduction
This interim report presents the results of **Task 1** for the *10 Academy Week 11 Challenge*, focusing on preprocessing and exploratory data analysis (EDA) of financial data for **Tesla (TSLA)**, **Vanguard Total Bond Market ETF (BND)**, and **S&P 500 ETF (SPY)** from **July 1, 2015, to July 31, 2025**.  

Objectives:
- Data extraction, cleaning, and EDA
- Stationarity testing
- Volatility and risk metric calculation

All code is available here: [GitHub Repository](https://github.com/emegua19/TimeSeries-Trading-Optimization).

---

## Data Overview
Historical data for TSLA, BND, and SPY were fetched from **Yahoo Finance** using the `yfinance` library.  
- **Period:** July 1, 2015 – July 31, 2025  
- **Observations:** 7,605 total (2,535 per ticker)  
- **Columns:** Date, Open, High, Low, Close, Adjusted Close, Volume, Ticker  

**Basic Statistics for Adjusted Close Prices:**

| Ticker | Count | Mean    | Std Dev  | Min    | Median | Max    |
|--------|-------|---------|----------|--------|--------|--------|
| TSLA   | 2535  | 131.96  | 120.91   | 9.58   | 94.57  | 479.86 |
| BND    | 2535  | 68.47   | 4.55     | 60.78  | 67.60  | 77.32  |
| SPY    | 2535  | 334.19  | 126.43   | 155.87 | 305.26 | 637.10 |

- **TSLA:** High volatility and growth potential  
- **BND:** Stable bond returns  
- **SPY:** Diversified market exposure  

---

## Data Cleaning
- **Missing Values:** None  
- **Data Types:** Verified (`float64` for prices, `datetime64` for Date)  
- **Scaling:** Adjusted Close prices scaled to [0, 1] per ticker using `MinMaxScaler`  
- **Daily Returns Calculation:**

\[
\text{Daily Return}_t = \frac{\text{Adj Close}_t - \text{Adj Close}_{t-1}}{\text{Adj Close}_{t-1}}
\]

- **Additional Features:** `Adj_Close_Scaled`, `Daily_Return`

---

## Exploratory Data Analysis

**Key Observations:**
- **Closing Prices:**  
  - TSLA: Strong upward trend  
  - BND: Stable  
  - SPY: Steady growth  

- **Daily Returns:**  
  - TSLA: Large swings  
  - BND: Minimal fluctuations  
  - SPY: Moderate variability  

- **Rolling Volatility (30-day):**  
  - TSLA: Frequent peaks  
  - BND: Low volatility  
  - SPY: Intermediate profile  

*Figures:*  
- **Figure 1:** Closing Prices for TSLA, BND, SPY (2015–2025)  
- **Figure 2:** Daily Percentage Returns for TSLA, BND, SPY  
- **Figure 3:** 30-Day Rolling Volatility for TSLA, BND, SPY  

---

## Outlier Detection
**Method:** 3-standard-deviation rule (\(\mu \pm 3\sigma\))  

| Ticker | Date       | Daily Return |
|--------|-----------|--------------|
| TSLA   | 2018-08-02 | 0.1619       |
| TSLA   | 2018-09-28 | -0.1390      |
| TSLA   | 2018-10-01 | 0.1735       |
| BND    | 2020-03-12 | -0.0544      |
| BND    | 2020-03-13 | 0.0422       |
| SPY    | 2015-08-24 | -0.0421      |
| SPY    | 2015-08-26 | 0.0384       |

---

## Stationarity Testing
**Method:** Augmented Dickey-Fuller (ADF) Test

| Ticker        | ADF Statistic | p-value | Stationary |
|---------------|--------------:|--------:|------------|
| TSLA          | -1.4189       | 0.5732  | No         |
| TSLA Returns  | -34.6811      | 0.0000  | Yes        |
| BND           | -1.5363       | 0.5155  | No         |
| BND Returns   | -9.8898       | 0.0000  | Yes        |
| SPY           | 0.6908        | 0.9897  | No         |
| SPY Returns   | -16.2644      | 0.0000  | Yes        |

- Prices: Non-stationary (require differencing)  
- Returns: Stationary (can be modeled directly)  

---

## Risk Metrics
**Formulas:**

\[
\text{Sharpe Ratio} = \frac{\text{Mean Return} - \text{Risk-Free Rate}}{\text{Return Std Dev}} \cdot \sqrt{252}
\]

**Assumptions:**  
- Daily risk-free rate = \(0.04/252\)

| Ticker | VaR (95%)  | Sharpe Ratio |
|--------|-----------:|-------------:|
| TSLA   | -0.0547    | 0.7108       |
| BND    | -0.0049    | -0.3715      |
| SPY    | -0.0172    | 0.5748       |

---

## Insights
- **TSLA:** High volatility (VaR: -5.47%) and strong growth; prices need differencing for ARIMA  
- **BND:** Low volatility (VaR: -0.49%); stable and predictable returns  
- **SPY:** Balanced risk-return profile; steady growth and stationary returns  

---

## Future Work
1. **Task 2:** ARIMA forecasting using differenced prices (TSLA, BND, SPY) and stationary returns  
2. **Task 3:** Machine learning models (LSTM, Random Forest) with scaled prices and returns  
3. **Task 4:** Portfolio optimization using VaR and Sharpe Ratio  
4. **Task 5:** Final report and presentation integrating findings from all tasks  
