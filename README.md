# Week 11 Portfolio Forecasting

This repository contains the work for the **10 Academy Week 11 Challenge**, focusing on **time series forecasting** and **portfolio optimization** using financial data for:

- **Tesla (TSLA)**
- **Vanguard Total Bond Market ETF (BND)**
- **S&P 500 ETF (SPY)**

The time period covered is **July 1, 2015 – July 31, 2025**.  
The project is structured to meet the requirements of **Tasks 1–5**, with **Task 1 completed** for the interim submission.

**GitHub:** [TimeSeries-Trading-Optimization](https://github.com/emegua19/TimeSeries-Trading-Optimization)

---

## Project Structure

```

week11\_portfolio\_forecasting/
├── data/
│   ├── raw/
│   │   ├── BND\_raw\.csv
│   │   ├── SPY\_raw\.csv
│   │   ├── test.csv
│   │   └── TSLA\_raw\.csv
│   └── processed/
│       ├── processed\_task1.csv
│       ├── risk\_metrics.csv
├── notebooks/
│   └── 01\_data\_eda.ipynb
├── reports/
│   ├── figures/
│   │   ├── closing\_prices.png
│   │   ├── daily\_returns.png
│   │   └── rolling\_volatility.png
│   └── interim/
│       ├── interim\_task1\_report.tex
│       └── interim\_task1\_report.pdf
├── src/
│   ├── **init**.py
│   ├── data\_fetch.py
│   ├── data\_cleaning.py
│   ├── eda.py
│   └── utils.py
├── tests/
│   └── test\_data\_pipeline.py
└── README.md

````

---

## Setup

1. **Clone the repository:**
```bash
git clone https://github.com/emegua19/TimeSeries-Trading-Optimization.git
cd week11_portfolio_forecasting
````

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

### Required Packages

* yfinance
* pandas
* numpy
* matplotlib
* seaborn
* statsmodels
* pmdarima
* scikit-learn
* python-docx

---

## Task 1: Preprocess and Explore Data

**Notebook:** `notebooks/01_data_eda.ipynb`

**Description:**

* Fetches, cleans, and analyzes financial data for TSLA, BND, and SPY (2015-07-01 to 2025-07-31)
* Performs **EDA**, **stationarity testing**, **outlier detection**, and **risk metric calculation**

**Outputs:**

* `data/raw/`: Raw CSV files (TSLA\_raw\.csv, BND\_raw\.csv, SPY\_raw\.csv, test.csv)
* `data/processed/`: Processed dataset (`processed_task1.csv`) and risk metrics (`risk_metrics.csv`)
* `reports/figures/`: EDA plots (closing\_prices.png, daily\_returns.png, rolling\_volatility.png)
* `reports/interim/`: Interim report PDF summarizing data preprocessing, EDA, outliers, stationarity, risk metrics, and future work

**Key Results:**

* **Dataset shape:** 7,605 rows (2,535 per ticker)
* **Stationarity:** Prices are **non-stationary**, returns are **stationary** (ADF p-values < 0.05)
* **Risk Metrics:**

  * TSLA → VaR: -5.47%, Sharpe: 0.7108
  * BND → VaR: -0.49%, Sharpe: -0.3715
  * SPY → VaR: -1.72%, Sharpe: 0.5748

**Interim Report:** See `reports/interim/interim_task1_report.pdf` for detailed results and visualizations.

---

## Future Work

* **Task 2:** Fit **ARIMA** models using differenced prices (non-stationary) and stationary returns from `data/processed/processed_task1.csv`
* **Task 3:** Train **machine learning models** (LSTM, Random Forest) using scaled prices and returns, addressing outliers
* **Task 4:** Optimize **portfolio weights** for TSLA, BND, SPY using risk metrics (VaR, Sharpe Ratio) from `data/processed/risk_metrics.csv`
* **Task 5:** Compile a **final report** with forecasting results, portfolio recommendations, and visualizations

---

## Notes

* All code is modularized in `src/`
* Tests are in `tests/test_data_pipeline.py`
* Run:

```bash
pytest tests/
```

to verify data pipeline functionality

* **Interim submission:** Task 1 completed as of **August 10, 2025**, with all outputs committed to the `task-1` branch
* For issues or contributions, see the [GitHub repository](https://github.com/emegua19/TimeSeries-Trading-Optimization)


