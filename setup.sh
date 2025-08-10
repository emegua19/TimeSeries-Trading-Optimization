#!/bin/bash

# Project root
PROJECT_NAME="week11_portfolio_forecasting"

# Create directories
mkdir -p $PROJECT_NAME/{data/raw,data/processed,data/external}
mkdir -p $PROJECT_NAME/notebooks
mkdir -p $PROJECT_NAME/src
mkdir -p $PROJECT_NAME/tests
mkdir -p $PROJECT_NAME/reports/{interim,final,figures}
mkdir -p $PROJECT_NAME/.github/workflows

# Create empty Python package files
touch $PROJECT_NAME/src/__init__.py
touch $PROJECT_NAME/tests/__init__.py

# Create placeholder notebooks
touch $PROJECT_NAME/notebooks/01_data_eda.ipynb
touch $PROJECT_NAME/notebooks/02_modeling.ipynb
touch $PROJECT_NAME/notebooks/03_optimization.ipynb
touch $PROJECT_NAME/notebooks/04_backtesting.ipynb

# Create placeholder Python scripts
touch $PROJECT_NAME/src/data_fetch.py
touch $PROJECT_NAME/src/data_cleaning.py
touch $PROJECT_NAME/src/eda.py
touch $PROJECT_NAME/src/utils.py
touch $PROJECT_NAME/tests/test_data_pipeline.py

# Create README.md
cat <<EOL > $PROJECT_NAME/README.md
# Week 11 Portfolio Forecasting

This project implements time series forecasting and portfolio optimization for GMF Investments.

## Structure
- **data/**: Raw, processed, and external datasets
- **notebooks/**: Jupyter notebooks for each task
- **src/**: Python source code
- **tests/**: Unit tests for CI
- **reports/**: Interim and final reports
- **.github/workflows/**: CI configuration

## Getting Started
1. Install dependencies: \`pip install -r requirements.txt\`
2. Run tests: \`pytest\`
3. Open notebooks in Jupyter: \`jupyter notebook\`
EOL

# Create requirements.txt
cat <<EOL > $PROJECT_NAME/requirements.txt
yfinance
pandas
numpy
matplotlib
seaborn
statsmodels
pmdarima
scikit-learn
jupyter
pytest
flake8
EOL

# Create .gitignore
cat <<EOL > $PROJECT_NAME/.gitignore
__pycache__/
*.py[cod]
*.egg
*.egg-info/
*.pyo
*.pyd
build/
develop-eggs/
dist/
eggs/
lib/
lib64/
parts/
sdist/
var/
*.log
*.tmp
.ipynb_checkpoints
.env
.venv
env/
venv/
ENV/
*.env
*.venv
.vscode/
.idea/
data/raw/
data/processed/
data/external/
reports/interim/*.pdf
reports/final/*.pdf
reports/figures/
.DS_Store
Thumbs.db
EOL

# Create CI workflow file
cat <<EOL > $PROJECT_NAME/.github/workflows/ci.yml
name: CI - Week 11 Portfolio Forecasting

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build-test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
          pip install pytest

      - name: Run tests
        run: |
          pytest --maxfail=1 --disable-warnings -q

      - name: Lint with flake8
        run: |
          pip install flake8
          flake8 src/ --max-line-length=100 --ignore=E203,W503
EOL

echo "✅ Project structure for $PROJECT_NAME created successfully!"
