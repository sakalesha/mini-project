# Project Proposal & Planning (Member 4)

## 1. Project Objectives
The objective of this project is to build a robust system for **Stock Market Prediction, Anomaly Detection, and Risk Analysis** focusing on the Indian Banking Sector (SBI, HDFC, ICICI Bank) using **LSTM** networks.

### Specific Goals:
- Develop an LSTM model with high prediction accuracy (low MAPE/RMSE).
- Implement an Anomaly Detection system to identify irregular price movements.
- Provide a comparative risk-return analysis for investors.

## 2. Project Scope
- **Data Universe:** 3-5 years of historical OHLCV data for `SBIN.NS`, `HDFCBANK.NS`, and `ICICIBANK.NS`.
- **Target Variable:** Next-day Closing Price.
- **Algorithm:** Long Short-Term Memory (LSTM) and LSTM Autoencoders.
- **Output:** Prediction plots, Anomaly charts, and a Risk Assessment report.

## 3. Project Timeline (Gantt Chart)

| Week | Phase | Key Milestone |
| :--- | :--- | :--- |
| **W1** | **Foundation** | Env Setup, Literature Review, Project Proposal |
| **W2** | **Data** | EDA, Data Cleaning, and Preprocessing (MinMaxScaler) |
| **W3** | **Architecture** | LSTM Model Design & Hyperparameter Tuning |
| **W4** | **Prediction** | Training on SBI/HDFC/ICICI and Accuracy Metrics |
| **W5** | **Anomaly** | LSTM Autoencoder Training & Threshold Setting |
| **W6** | **Risk** | Sharpe Ratio, Volatility, and Comparative Analysis |
| **W7** | **Final** | Report Completion, PPT, and Final Demonstration |

## 4. Resource Plan
- **Tools:** Python (TensorFlow, Keras, yfinance), Git/GitHub.
- **Hardware:** Local PC / Google Colab for GPU acceleration.
- **Collaboration:** Weekly team stand-ups and shared GitHub repository.

## 5. Risk Assessment
- **Market Volatility:** Sudden news can break historical patterns; Anomaly Detection is our mitigation.
- **Overfitting:** Addressed via Dropout layers and Early Stopping.
- **Data Quality:** Mitigation via robust preprocessing and validation scripts.
