# Week-wise Project Checklist: LSTM Stock Prediction

## Week 1: Project Setup & Literature Review (Foundation Phase)
- [ ] **Member 1: Environment Setup**
    - [ ] Install Python, Jupyter Notebook, Anaconda
    - [ ] Set up libraries (TensorFlow/Keras, NumPy, Pandas, Matplotlib)
    - [x] Create project folder structure & Shared Repository (Git/Drive)
- [x] **Member 2: Literature Study - LSTM**
    - [x] Study reference paper & LSTM architecture
    - [x] Document LSTM gate mechanisms (Input, Forget, Output)
    - [x] Compile 5-7 relevant research papers
- [x] **Member 3: Domain Research & Metrics** <!-- id: 9 -->
    - [x] Research Indian banking sector (SBI, HDFC, ICICI)
    - [x] Study risk analysis metrics (SD, Sharpe Ratio)
    - [x] Identify data sources (Yahoo Finance, NSE, BSE)
- [x] **Member 4: Project Planning**
    - [x] Create detailed project timeline (Gantt chart)
    - [x] Define scope and objectives
    - [x] Prepare preliminary project proposal
- [x] **Week 1 Deliverables (COMPLETE):** Configured environment, Literature review doc, Project proposal draft

---

## Week 2: Data Collection & Preprocessing (Data Acquisition Phase)
- [x] **Member 1: Data Collection**
    - [x] Collect 3+ years of OHLCV data for SBI, HDFC, ICICI
    - [x] Save raw data in CSV format
- [x] **Member 2: Data Exploration**
    - [x] Perform EDA & Visualize stock price trends
    - [x] Generate correlation matrices between stocks
- [x] **Member 3: Data Cleaning**
    - [x] Handle missing values & Remove duplicates
    - [x] Validate data integrity across all banks
- [x] **Member 4: Data Preprocessing**
    - [x] Normalize/Scale data (MinMaxScaler)
    - [x] Create Train-Test split (80:20) & Sequence windowing
- [x] **Week 2 Deliverables (COMPLETE):** Clean CSV files, EDA report, Preprocessed data for LSTM

---

## Week 3: LSTM Model Development (Model Building Phase)
- [x] **Member 1: Data Pipeline**
    - [x] Implement sliding window approach (e.g., 60-day)
    - [x] Reshape data for LSTM (samples, timesteps, features)
- [x] **Member 2: LSTM Architecture**
    - [x] Design LSTM model (2-3 layers, Dropout for regularization)
    - [x] Implement using Keras/TensorFlow
- [x] **Member 3: Hyperparameter Tuning**
    - [x] Select optimizer (Adam) & Loss function (MSE)
    - [x] Fine-tune learning rate, batch size, and epochs
- [x] **Member 4: Model Training Setup**
    - [x] Set up callbacks (EarlyStopping, ModelCheckpoint)
    - [x] Document architecture and parameters
- [x] **Week 3 Deliverables (COMPLETE):** Model architecture code, Diagram, Hyperparameter config

---

## Week 4: Stock Price Prediction (Prediction Implementation)
- [x] **Member 1: SBI Model Training**
    - [x] Train & Save SBI model weights
    - [x] Generate training history plots
- [x] **Member 2: HDFC & ICICI Training**
    - [x] Train & Save HDFC/ICICI model weights
    - [x] Create comparative training plots
- [x] **Member 3: Prediction Generation**
    - [x] Generate predictions & Inverse transform scale
    - [x] Forecast future prices (7-30 days)
- [x] **Member 4: Performance Metrics**
    - [x] Calculate MSE, MAE, RMSE, MAPE for each bank
    - [x] Create performance comparison table
- [x] **Week 4 Deliverables:** Trained models, Prediction plots, Metrics report

---

## Week 5: Anomaly Detection Implementation (Anomaly Detection Phase)
- [x] **Member 1: LSTM Autoencoder Design**
    - [x] Design Encoder-Decoder architecture
- [x] **Member 2: Autoencoder Training**
    - [x] Train on normal data & Save models
- [x] **Member 3: Anomaly Detection Logic**
    - [x] Set threshold (mean + 2*SD)
    - [x] Visualize anomalies on price charts (Red Dots)
- [x] **Member 4: Anomaly Analysis**
    - [x] Correlate anomalies with real-world events (COVID, Elections)
    - [x] Document findings with explanations
- [x] **Week 5 Deliverables:** Autoencoder models, Anomaly visualizations, Analysis report

---

## Week 6: Risk Analysis & Evaluation (Risk Assessment Phase)
- [x] **Member 1: Risk Metrics Calculation**
    - [x] Calculate Daily Returns & Standard Deviation
    - [x] Compute Sharpe Ratio & Beta vs NIFTY
- [x] **Member 2: Volatility Analysis**
    - [x] Calculate 30-day Rolling Volatility
    - [x] Identify high volatility periods
- [x] **Member 3: Comparative Risk Analysis**
    - [x] Compare risk profiles (SBI vs HDFC vs ICICI)
    - [x] Create risk-return scatter plots
- [x] **Member 4: Final Model Evaluation**
    - [x] Consolidate all metrics into evaluation tables
    - [x] Document strengths and limitations
- [x] **Week 6 Deliverables:** Risk report, Volatility plots, Investment recommendations

---

## Week 7: Documentation & Presentation (Final Deliverables)
- [ ] **Member 1: Code Documentation**
    - [ ] Clean code, add comments, and create README.md
    - [ ] Prepare final code package & requirements.txt
- [ ] **Member 2: Project Report Writing**
    - [ ] Write Introduction, Methodology, Results, and Conclusion
    - [ ] Format report to IEEE/academic standards
- [ ] **Member 3: Presentation Preparation**
    - [ ] Create PPT slides (15-20 slides)
    - [ ] Prepare demo video/live demo
- [ ] **Member 4: Final Integration & Testing**
    - [ ] Perform end-to-end system testing
    - [ ] Prepare final submission package
- [ ] **Week 7 Deliverables:** 20-30 page report, Presentation slides, Complete source code
