# Domain Research & Risk Metrics Study (Member 3)

## 1. Indian Banking Sector Overview
The Indian banking sector is a critical component of the national economy, characterized by a mix of Public Sector Banks (PSBs) and Private Sector Banks. Our project focuses on the leaders of these categories.

### Target Banks Profile (2024-2025)
- **HDFC Bank:** India's largest private sector bank. Known for best-in-class profitability and steady loan growth.
- **ICICI Bank:** A major private sector rival to HDFC, consistently delivering high returns and robust asset quality.
- **State Bank of India (SBI):** The largest public sector bank in India. Demonstrates strong growth in Net Interest Income (NII) and has shown a significant upside in recent market evaluations.

---

## 2. Risk Analysis Metrics
To evaluate the stability and performance of these stocks, we will use the following standard risk metrics:

| Metric | Definition | Purpose in our Project |
| :--- | :--- | :--- |
| **Standard Deviation (SD)** | Measures the volatility or dispersion of stock returns from the average. | Quantifies the "spread" of price movements to identify risk levels. |
| **Sharpe Ratio** | The ratio of excess return (above risk-free rate) to the standard deviation. | Determines if the returns of the bank stock justify the risk taken. |
| **Beta (β)** | Measures the stock's sensitivity/volatility relative to the broader market (e.g., NIFTY 50). | Indicates if the bank's price moves in line with or more aggressively than the market. |

---

## 3. Data Sources Identification
For our LSTM-based prediction and risk analysis, we require high-quality historical OHLCV (Open, High, Low, Close, Volume) data.

### Primary Data Source: Yahoo Finance
- **Tool:** `yfinance` Python library (already in `requirements.txt`).
- **Tickers:**
  - `SBIN.NS` (State Bank of India - NSE)
  - `HDFCBANK.NS` (HDFC Bank - NSE)
  - `ICICIBANK.NS` (ICICI Bank - NSE)
- **Reliability:** Provides free, reliable historical daily data spanning multiple years.

### Secondary/Reference Sources:
- **NSE (National Stock Exchange):** [nseindia.com](https://www.nseindia.com) for official historical reports.
- **BSE (Bombay Stock Exchange):** [bseindia.com](https://www.bseindia.com) for corporate announcements and fundamental data.

---

## 4. Work Plan for Member 3
1. **Week 2:** Assist in validating data integrity and identifying outliers in the raw CSV files.
2. **Week 5:** Help define the anomaly threshold based on the Standard Deviation (Mean + 2*SD).
3. **Week 6:** Lead the calculation of Sharpe Ratio and Volatility metrics for all three banks.
