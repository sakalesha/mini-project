# Project Summary: LSTM Stock Prediction & Anomaly Detection

## Project Overview
**Title:** Leveraging Long Short - Term Memory (LSTM) for Stock Prediction, Anomaly Detection, and Risk Analysis in the Indian Banking Sector

**Team No:** 23
**Team Members:**
- Ronada Sakalesha (ENG23CS0165)
- Prem Kumar N (ENG23CS0146)
- Rakesh M A (ENG23CS0157)
- Rahul K (ENG23CS0152)

**Guide:** Prof. Yashpal Gupta S
**Department:** Computer Science and Engineering, School of Engineering
**Academic Year:** 2025-26

## Objective
The primary goal of this project is to apply the **Long Short-Term Memory (LSTM)** algorithm to analyze and predict stock price movements within the Indian banking sector. 

### Key Components:
1. **Stock Price Prediction:** Forecasting future prices for major banks like State Bank of India (SBI), HDFC Bank, and ICICI Bank.
2. **Anomaly Detection:** Identifying unusual or irregular price movements that could indicate market volatility or specific events.
3. **Risk Analysis:** Evaluating the stability and risk associated with these banks based on historical data and detected anomalies.

## Technology Stack
- **Language:** Python
- **Algorithm:** LSTM (Long Short-Term Memory)
- **Sector Focus:** Indian Banking Sector (SBI, HDFC, ICICI)

## Folder Structure
- `data/`: Raw and processed stock data.
- `ml/`: Python scripts for modeling and analysis (data loaders, model definition).
- `notebooks/`: Jupyter notebooks for exploratory data analysis.
- `results/`: Storage for trained model weights and visualization plots.
- `DOCS/`: Project documents and roadmap.

## Current Progress Status (As of Week 3)
The project is currently tracking strictly according to the detailed `CHECKLIST.md`. 
The following phases have been completed:

### **Week 1: Project Setup & Literature Review (Foundation Phase) - [COMPLETE]**
* Designed complete project folder structure.
* Prepared preliminary project proposal.
* Studied the LSTM architecture algorithms and mapped out Indian Bank data sources.

### **Week 2: Data Collection & Preprocessing (Data Acquisition Phase) - [COMPLETE]**
* Collected historical OHLCV dataset for SBI, HDFC, and ICICI.
* Conducted Exploratory Data Analysis (EDA) on closing price trends.
* Formulated Sectoral Correlation Analysis amongst the three target banks.

### **Week 3: LSTM Model Development (Model Building Phase) - [COMPLETE]**
* Implemented the **Data Pipeline** (including Zero padding, Missing value handles, `MinMaxScaler` normalization, and generating a 60-day Sliding Window).
* Hand-developed the **LSTM Architecture** using Keras (3 Sequential LSTM layers with 20% Dropout in each step to prevent model overfitting). 
* Prepared tuning constraints alongside Model Checkpoint hooks using documentation standardized against external research guidelines on prediction hyperparameters (`DOCS/Hyperparameter_Config.md`). The operational code is now bundled cleanly inside `notebooks/Stock_Prediction_LSTM.ipynb`.
