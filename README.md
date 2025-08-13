
# TIMESERIES-TRADING-OPTIMIZATION

This repository contains the work for the **10 Academy Week 11 Challenge**, focusing on **time series forecasting** and **portfolio optimization** using financial data for:

- Tesla (TSLA)
- Vanguard Total Bond Market ETF (BND)
- S&P 500 ETF (SPY)

**Data period:** July 1, 2015 – July 31, 2025  
The project completes **Tasks 1–5**, culminating in a **backtested portfolio strategy**.

**GitHub Repository:** [TimeSeries-Trading-Optimization](https://github.com/emegua19/TimeSeries-Trading-Optimization)

---

## 📂 Project Structure

```plaintext
TIMESERIES-TRADING-OPTIMIZATION/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .pytest_cache/
├── .venv/
├── data/
│   ├── processed/
│   │   ├── processed_task1.csv
│   │   └── risk_metrics.csv
│   └── raw/
│       ├── BND_raw.csv
│       ├── SPY_raw.csv
│       ├── test.csv
│       └── TSLA_raw.csv
├── notebooks/
│   ├── 01_data_eda.ipynb
│   ├── 02_modeling.ipynb
│   ├── 03_forecast_analysis.ipynb
│   ├── 04_portfolio_optimization.ipynb
│   └── 05_backtesting.ipynb
├── report/
│   ├── final/
│   └── interim/
│       ├── interim_task1_report.tex
│       └── interim_task1_report.pdf
├── result/
│   ├── csv/
│   │   ├── arima_future_12m.csv
│   │   ├── arima_future_30d.csv
│   │   ├── arima_test_predictions.csv
│   │   ├── backtest_summary.csv
│   │   ├── comparison_test_predictions.csv
│   │   ├── lstm_future_12m.csv
│   │   ├── lstm_future_30d.csv
│   │   ├── lstm_test_predictions.csv
│   │   ├── metrics_test.csv
│   │   └── portfolio_optimization_summary.csv
│   └── figures/
│       ├── arima_forecast.png
│       ├── backtest_strategy_vs_benchmark.png
│       ├── closing_prices.png
│       ├── comparison_forecast.png
│       ├── daily_returns.png
│       ├── efficient_frontier.png
│       ├── forecast_comparison_12m.png
│       ├── lstm_forecast.png
│       └── rolling_volatility.png
├── src/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── data_cleaning.py
│   ├── data_fetch.py
│   ├── eda.py
│   └── utils.py
├── tests/
│   ├── __pycache__/
│   ├── __init__.py
│   └── test_data_pipeline.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
````

---

## ⚙️ Setup

**1. Clone the repository**

```bash
git clone https://github.com/emegua19/TimeSeries-Trading-Optimization.git
cd TIMESERIES-TRADING-OPTIMIZATION
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**Required packages:**

* yfinance
* pandas
* numpy
* matplotlib
* seaborn
* statsmodels
* pmdarima
* scikit-learn
* python-docx
* tensorflow
* scipy

---

##  Project Pipeline

1. **Data Fetching**

   * Script: `src/data_fetch.py`
   * Fetch TSLA, BND, SPY data (2015-07-01 → 2025-07-31).

2. **Data Cleaning**

   * Script: `src/data_cleaning.py`
   * Clean & scale data, save to `data/processed/processed_task1.csv`.

3. **EDA**

   * Script: `src/eda.py`
   * Perform exploratory data analysis, outlier detection, stationarity tests.

4. **Forecasting**

   * Notebook: `notebooks/02_modeling.ipynb`
   * Implement **ARIMA** & **LSTM** models for TSLA price predictions.

5. **Portfolio Optimization**

   * Notebook: `notebooks/04_portfolio_optimization.ipynb`
   * Apply Modern Portfolio Theory (MPT) to optimize portfolio weights.

6. **Backtesting**

   * Notebook: `notebooks/05_backtesting.ipynb`
   * Compare optimized portfolio vs. benchmark.

---

##  Tasks & Key Results

### **Task 1: Preprocess and Explore Data**

* Notebook: `notebooks/01_data_eda.ipynb`
* Outputs:

  * Raw data in `data/raw/`
  * Processed data & risk metrics in `data/processed/`
  * EDA plots in `result/figures/`
  * Interim report in `report/interim/`
* **Key Findings**:

  * Dataset shape: 7,605 rows
  * Stationarity: Prices non-stationary; returns stationary
  * Risk metrics: TSLA VaR = -5.47%, Sharpe = 0.7108

---

### **Task 2: Time Series Forecasting**

* Models: ARIMA vs LSTM
* Train/Test Split:

  * Train: 2015-07-01 → 2023-07-21 (n=2028)
  * Test: 2023-07-24 → 2025-07-30 (n=507)
* **Performance (MAPE)**:

  * ARIMA: 21.85%
  * LSTM: **4.76%** (better at capturing non-linear trends)

---

### **Task 3: Forecast Future Market Trends**

* Forecast period: 2025-08-01 → 2026-07-31
* LSTM provided more volatility-sensitive forecasts with widening confidence intervals.

---

### **Task 4: Portfolio Optimization**

* Based on LSTM & historical returns
* **Max Sharpe Portfolio**:

  * TSLA: 0%, BND: 0%, SPY: 100%
  * Return: 13.65%, Volatility: 18.31%, Sharpe: 0.745
* **Min Volatility Portfolio**:

  * TSLA: 0%, BND: 94.31%, SPY: 5.69%

---

### **Task 5: Strategy Backtesting**

* Period: 2024-08-01 → 2025-07-31
* Strategy (Max Sharpe portfolio) **outperformed** benchmark:

  * Total Return: 16.84% vs 10.10%
  * Sharpe: 0.881 vs 0.846

---

##  Testing

Run tests with:

```bash
pytest tests/
```

---

##  Notes

* Code is modularized in `src/`
* Outputs are saved in `result/csv/` & `result/figures/`
* Final report to be added in `report/final/`