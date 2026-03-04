# LSTM Research & Architecture Study (Member 2)

## 1. LSTM Architecture Overview
Long Short-Term Memory (LSTM) is a specialized type of Recurrent Neural Network (RNN) designed to learn long-term dependencies. Unlike traditional RNNs, LSTMs have a "cell state" that allows information to flow through with minimal changes, governed by three unique "gates."

### Core Components & Gate Mechanisms

| Component | Function | Role in Stock Prediction |
| :--- | :--- | :--- |
| **Cell State ($C_t$)** | The "memory" of the network that carries information across time steps. | Stores long-term price trends and historical market context. |
| **Forget Gate ($f_t$)** | Decides what information to discard from the cell state using a sigmoid function. | Filters out market noise or outdated news that no longer impacts current prices. |
| **Input Gate ($i_t$)** | Decides which new values to update in the cell state. | Incorporates new relevant data (e.g., today's closing price, recent earnings report). |
| **Output Gate ($o_t$)** | Decides what the next hidden state (output) should be based on the cell state. | Produces the actual price prediction or feature representation for the next layer. |

---

## 2. Relevant Research Papers (2020-2025)

### Paper 1: Hybrid LSTM-ARIMA for Indian Commercial Banks (2024)
- **Focus:** SBI, HDFC Bank, ICICI Bank, Axis Bank.
- **Key Finding:** Hybrid models consistently outperform standalone LSTM/ARIMA, achieving a MAPE below 3% for predicting daily closing prices.

### Paper 2: Comparative Analysis of Deep Learning Models in Indian Market (2024)
- **Focus:** HDFC, ICICI, Reliance, and Nifty Index.
- **Key Finding:** LSTM demonstrated superior ability to capture non-linear patterns in the highly volatile Indian market compared to GRU and RNN.

### Paper 3: Sectoral Profitability Analysis using LSTM Regression (2021)
- **Focus:** Sectoral indices with a spotlight on HDFC Bank.
- **Key Finding:** Optimized LSTM architectures effectively predicted future price movements during the high-volatility post-COVID period (Jan-Aug 2021).

### Paper 4: NSE Bank Index Prediction using LSTM (2025 - Expected)
- **Focus:** Nifty Bank Index.
- **Key Finding:** LSTMs are highly effective at capturing the unique "seasonal" patterns and regulatory-impacted trends specific to the Indian banking sector.

### Paper 5: Multi-Filtered LSTM Approach (2022)
- **Focus:** Integrating technical indicators (RSI, MACD) with LSTM for SBI and HDFC.
- **Key Finding:** Using technical indicators as additional features significantly reduces Mean Squared Error (MSE).

---

## 3. Recommended Approach for our Project
Based on the research, we should:
1. Use **MinMaxScaler** for normalization (0 to 1 range).
2. Use **dropout layers** (0.2-0.3) to prevent overfitting on the training data.
3. Consider a **window size of 60 days** (looking back at 2 months of data to predict the next day).
4. Use **Adam optimizer** and **MSE loss** as the standard configuration.
