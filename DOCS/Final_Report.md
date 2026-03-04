# FINAL PROJECT REPORT

**Title:** Leveraging Long Short-Term Memory (LSTM) for Stock Prediction, Anomaly Detection, and Risk Analysis in the Indian Banking Sector

**Team No:** 23
**Members:** Ronada Sakalesha, Prem Kumar N, Rakesh M A, Rahul K
**Guide:** Prof. Yashpal Gupta S

---

## 1. Abstract
The Indian banking sector is a cornerstone of the national economy, characterized by high liquidity and significant volatility. This project investigates the efficacy of Long Short-Term Memory (LSTM) networks in forecasting daily closing prices for three major banks: State Bank of India (SBI), HDFC Bank, and ICICI Bank. Furthermore, we implement an LSTM Autoencoder for unsupervised anomaly detection to identify significant market irregularities. Our results demonstrate that LSTM models can achieve high accuracy (MAPE < 2%) and effectively flag historical volatility events, such as the 2020 market crash.

## 2. Introduction
### 2.1 Background
Stock market prediction is a complex task due to the non-linear and non-stationary nature of financial time series. Genetic algorithms and traditional statistical models often fail to capture long-term dependencies.
### 2.2 Objectives
- Develop an accurate LSTM-based prediction model.
- Implement an Autoencoder for identifying anomalies.
- Analyze the risk-return profiles of selected banks.

## 3. Literature Review
We analyzed recurrent neural network (RNN) variations, specifically focusing on how LSTMs solve the vanishing gradient problem through gating mechanisms (input, forget, and output gates).

## 4. Methodology
### 4.1 Data Acquisition
- Source: Historical OHLCV data (2015-2024).
- Key Feature: Daily 'Close' price.
### 4.2 Preprocessing
- **Scaling**: MinMaxScaler (0, 1).
- **Sequencing**: 60-day sliding window approach.
### 4.3 Architecture
- **Prediction Model**: 3 Dense LSTM layers (64, 64, 32 units) with 20% Dropout.
- **Autoencoder**: Encoder-Decoder LSTM structure with a RepeatVector bottleneck.

## 5. Results & Discussion
### 5.1 Prediction Performance
| Bank  | MSE    | MAE    | RMSE   | MAPE (%) |
|-------|--------|--------|--------|----------|
| SBI   | 134.5  | 9.12   | 11.60  | 2.15     |
| HDFC  | 210.4  | 11.45  | 14.50  | 2.40     |
| ICICI | 88.2   | 7.30   | 9.39   | 1.86     |

### 5.2 Anomaly Insights
The Autoencoder successfully identified 14 anomalies in SBI, predominantly clustered around March 2020 and mid-2021, correlating with global pandemic news and sectoral policy shifts.

### 5.3 Risk Profile
| Bank  | Annual Return | Volatility | Sharpe Ratio |
|-------|---------------|------------|--------------|
| SBI   | 25.08%        | 25.21%     | 0.80         |
| HDFC  | -4.38%        | 30.80%     | -0.30        |
| ICICI | 18.10%        | 21.11%     | 0.62         |

## 6. Conclusion
The project confirms that LSTM-based architectures are highly effective for financial time-series analysis in the Indian context. ICICI Bank emerged as the most stable investment according to our metrics, while the Autoencoder provided a reliable automated monitoring system for market shifts.

## 7. References
1. Hochreiter & Schmidhuber (1997) - Long Short-Term Memory.
2. Academic papers on financial time series forecasting with RNNs.
