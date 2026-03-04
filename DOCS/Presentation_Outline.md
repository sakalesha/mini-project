# FINAL PRESENTATION OUTLINE

**Project Title:** LSTM for Stock Prediction & Anomaly Detection (Indian Banking Sector)
**Team No:** 23
**Target Length:** 15-20 Slides

---

## Slide 1: Title Slide
- Project Title
- Student Names & IDs
- Guide Name & Department

## Slide 2: Introduction
- Importance of stock prediction in the Indian economy.
- Challenges of traditional statistical models.
- Objective: Combining forecasting, anomaly detection, and risk assessment.

## Slide 3: Problem Statement
- High non-linearity in banking stocks.
- Need for automated irregularity detection (Anomalies).
- Bridging the gap between technical metrics and investment risk.

## Slide 4: Literature Review
- Recap of LSTM fundamentals (Gating mechanisms).
- Why LSTM over standard RNNs (Vanishing Gradient).

## Slide 5: Data Collection
- Banks: SBI, HDFC, ICICI.
- Range: 2015-2024 (OHLCV Data).
- Scaling: MinMaxScaler.

## Slide 6: System Architecture (Prediction)
- Sliding Window approach (60 days lookback).
- Multi-layer LSTM model structure (3 Dense layers + Dropout).

## Slide 7: Training & Validation Results
- Showcase MSE, MAE, and MAPE tables.
- **Visual**: Training Loss vs. Validation Loss graph.

## Slide 8: Result Comparisons
- Comparison chart for HDFC vs SBI vs ICICI prediction accuracy.
- Highlight ICICI as the most accurate.

## Slide 9: Anomaly Detection Methodology
- Introduction to Unsupervised Learning with Autoencoders.
- Reconstruction Error logic (MAE > Threshold).

## Slide 10: Anomaly Results (Visual)
- **Visual**: Stock chart with Red Dots marking anomalies.
- Highlight specific clusters from 2020.

## Slide 11: Risk Analysis Metrics
- Annualized Return and Volatility.
- Sharpe Ratio computation.

## Slide 12: Risk-Return Scatter Plot
- **Visual**: Distribution of the 3 banks across the risk-return spectrum.
- Comparison of SBI and ICICI efficiency.

## Slide 13: Technical Stability (Rolling Volatility)
- 30-day Rolling Volatility trends.
- How volatility correlates with detected anomalies.

## Slide 14: Conclusion
- Summary of findings.
- Effectiveness of LSTM for multi-bank analysis.
- Future scope: Multi-modal data integration (Sentiment Analysis).

## Slide 15: Q&A / Bibliography
- Thank you note.
- Key references.
