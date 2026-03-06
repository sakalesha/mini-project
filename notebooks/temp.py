import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Set plotting style
sns.set_theme(style="whitegrid")
%matplotlib inline

# Create results directory
os.makedirs("../results/plots", exist_ok=True)
# ----
def perform_eda(file_path, bank_name):
    print(f"--- EDA for {bank_name} ---")
    df = pd.read_csv(file_path, thousands=',')
    
    # Preprocessing for EDA: Convert DATE to datetime and sort
    df['DATE'] = pd.to_datetime(df['DATE'], format='%d-%b-%Y')
    df = df.sort_values('DATE')
    
    print(f"Data range: {df['DATE'].min()} to {df['DATE'].max()}")
    print(f"Total records: {len(df)}")
    
    # Plotting Closing Price
    plt.figure(figsize=(12, 5))
    plt.plot(df['DATE'], df['CLOSE'], label=f'{bank_name} Close Price', color='blue')
    plt.title(f'{bank_name} Closing Price Trend')
    plt.xlabel('Date')
    plt.ylabel('Price (INR)')
    plt.legend()
    plt.show()

# Paths to raw data
banks = {'SBI': '../data/raw/SBI.csv', 'HDFC': '../data/raw/HDFC.csv', 'ICICI': '../data/raw/ICICI.csv'}

for name, path in banks.items():
    if os.path.exists(path):
        perform_eda(path, name)
    else:
        print(f"File not found: {path}")
# ----
print("--- Sectoral Correlation Analysis ---")
close_prices = {}

for name, path in banks.items():
    if os.path.exists(path):
        df = pd.read_csv(path, thousands=',')
        df['DATE'] = pd.to_datetime(df['DATE'], format='%d-%b-%Y')
        df['CLOSE'] = pd.to_numeric(df['CLOSE'], errors='coerce')
        df = df.dropna().groupby('DATE').mean(numeric_only=True) # Handle duplicates
        close_prices[name] = df['CLOSE']

# Combine and calculate correlation matrix
combined_df = pd.concat(close_prices.values(), axis=1, keys=close_prices.keys(), join='inner')
print(f"Aligned records for correlation: {len(combined_df)}")

if not combined_df.empty:
    plt.figure(figsize=(8, 6))
    sns.heatmap(combined_df.corr(), annot=True, cmap='RdYlGn', fmt=".2f")
    plt.title('Stock Price Correlation Heatmap')
    plt.show()
# ----
def prepare_data(file_path, target_col='CLOSE', window_size=60):
    print(f"--- Preparing data from {file_path} ---")
    df = pd.read_csv(file_path, thousands=',')
    
    # 1. Cleaning: Convert date, sort, and handle duplicates
    df['DATE'] = pd.to_datetime(df['DATE'], format='%d-%b-%Y')
    df = df.sort_values('DATE')
    df['CLOSE'] = pd.to_numeric(df['CLOSE'], errors='coerce')
    df = df.dropna(subset=[target_col])
    df = df.groupby('DATE').mean(numeric_only=True) # Ensure one record per day
    
    data = df[target_col].values.reshape(-1, 1)
    
    # 2. Normalization: Scale features to (0, 1) range for LSTM efficiency
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data)
    
    # 3. Sliding Window Creation
    X, y = [], []
    for i in range(window_size, len(scaled_data)):
        X.append(scaled_data[i-window_size:i, 0])
        y.append(scaled_data[i, 0])
    
    X, y = np.array(X), np.array(y)
    X = np.reshape(X, (X.shape[0], X.shape[1], 1)) # LSTM input format: [samples, time steps, features]
    
    print(f"Processed {len(y)} sequences with window size {window_size}")
    return X, y, scaler

# Prepare training sequences for SBI stock
X_sbi, y_sbi, sbi_scaler = prepare_data('../data/raw/SBI.csv', window_size=60)

print(f"X_sbi shape: {X_sbi.shape}")
print(f"y_sbi shape: {y_sbi.shape}")
# ----
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

def create_lstm_model(input_shape):
    model = Sequential()
    # First LSTM layer
    model.add(LSTM(units=50, return_sequences=True, input_shape=input_shape))
    model.add(Dropout(0.2))
    
    # Second LSTM layer
    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.2))
    
    # Third LSTM layer
    model.add(LSTM(units=50))
    model.add(Dropout(0.2))
    
    # Output layer
    model.add(Dense(units=1))
    
    # Compile the model with Adam optimizer and Mean Squared Error loss
    # Compile the model with Adam optimizer (lr=0.001) and Mean Squared Error loss
    from tensorflow.keras.optimizers import Adam
    optimizer = Adam(learning_rate=0.001)
    model.compile(optimizer=optimizer, loss='mean_squared_error', metrics=['mse', 'mae'])
    return model

input_shape = (X_sbi.shape[1], X_sbi.shape[2])
model = create_lstm_model(input_shape)
model.summary()
# ----
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

epochs = 50
batch_size = 32

# Define callbacks
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
model_checkpoint = ModelCheckpoint('../results/sbi_lstm_model.h5', monitor='val_loss', save_best_only=True)

print("Starting model training for SBI...")
history = model.fit(
    X_sbi, y_sbi,
    epochs=epochs,
    batch_size=batch_size,
    validation_split=0.1,
    callbacks=[early_stopping, model_checkpoint],
    verbose=1
)
# ----
def plot_training_history(history, bank_name):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    # Plot MSE Loss
    ax1.plot(history.history['loss'], label='Train Loss (MSE)')
    ax1.plot(history.history['val_loss'], label='Val Loss (MSE)')
    ax1.set_title(f'{bank_name} Model Loss')
    ax1.set_ylabel('Loss')
    ax1.set_xlabel('Epoch')
    ax1.legend()
    
    # Plot MAE
    if 'mae' in history.history:
        ax2.plot(history.history['mae'], label='Train MAE')
        ax2.plot(history.history['val_mae'], label='Val MAE')
    elif 'mean_absolute_error' in history.history:
        ax2.plot(history.history['mean_absolute_error'], label='Train MAE')
        ax2.plot(history.history['val_mean_absolute_error'], label='Val MAE')
    ax2.set_title(f'{bank_name} Mean Absolute Error')
    ax2.set_ylabel('MAE')
    ax2.set_xlabel('Epoch')
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig(f'../results/plots/{bank_name.lower()}_training_history.png')
    plt.show()

plot_training_history(history, 'SBI')
# ----
def train_and_evaluate(bank_name, file_path):
    print(f"\n{'='*40}")
    print(f"Training Pipeline for {bank_name}")
    print(f"{'='*40}")
    
    # 1. Prepare Data
    X, y, scaler = prepare_data(file_path, window_size=60)
    
    # 2. Compile Model
    input_shape = (X.shape[1], X.shape[2])
    model = create_lstm_model(input_shape)
    
    # 3. Setup Callbacks
    early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
    checkpoint_path = f'../results/{bank_name.lower()}_lstm_model.keras'
    model_checkpoint = ModelCheckpoint(checkpoint_path, monitor='val_loss', save_best_only=True)
    
    # 4. Train Model
    history = model.fit(
        X, y,
        epochs=50,
        batch_size=32,
        validation_split=0.1,
        callbacks=[early_stopping, model_checkpoint],
        verbose=1
    )
    
    # 5. Plot History
    plot_training_history(history, bank_name)
    
    return model, scaler, history

# Run for HDFC
hdfc_model, hdfc_scaler, hdfc_hist = train_and_evaluate('HDFC', '../data/raw/HDFC.csv')

# Run for ICICI
icici_model, icici_scaler, icici_hist = train_and_evaluate('ICICI', '../data/raw/ICICI.csv')
# ----
from tensorflow.keras.models import load_model

def test_data(file_path, window_size=60):
    df = pd.read_csv(file_path, thousands=',')
    df['DATE'] = pd.to_datetime(df['DATE'], format='%d-%b-%Y')
    df = df.sort_values('DATE')
    df['CLOSE'] = pd.to_numeric(df['CLOSE'], errors='coerce')
    df = df.dropna(subset=['CLOSE'])
    df = df.groupby('DATE').mean(numeric_only=True)
    data = df['CLOSE'].values.reshape(-1, 1)
    
    # Train-test split (80-20)
    train_size = int(len(data) * 0.8)
    test_data = data[train_size - window_size:]
    
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaler.fit(data[:train_size]) # Fit only on train
    scaled_test = scaler.transform(test_data)
    
    X_test, y_test = [], []
    for i in range(window_size, len(scaled_test)):
        X_test.append(scaled_test[i-window_size:i, 0])
        y_test.append(scaled_test[i, 0])
        
    X_test, y_test = np.array(X_test), np.array(y_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    
    # Also return dates for plotting
    dates = df.index[train_size:].values
    return X_test, y_test, scaler, dates

def predict_and_plot(bank_name, file_path):
    print(f"\n{'='*40}")
    print(f"Generating Predictions for {bank_name}")
    print(f"{'='*40}")
    
    X_test, y_test, scaler, dates = test_data(file_path)
    
    # Load model and predict
    model_path = f'../results/{bank_name.lower()}_lstm_model.keras'
    try:
        model = load_model(model_path)
    except FileNotFoundError:
        print(f"Error: Model {model_path} not found. Train first.")
        return None, None, None
        
    predictions = model.predict(X_test)
    
    # Inverse transform
    predictions_inv = scaler.inverse_transform(predictions)
    y_test_inv = scaler.inverse_transform(y_test.reshape(-1, 1))
    
    # Plot Predictions vs Actuals
    plt.figure(figsize=(14, 6))
    plt.plot(dates, y_test_inv, color='blue', label=f'Actual {bank_name} Price')
    plt.plot(dates, predictions_inv, color='red', label=f'Predicted {bank_name} Price')
    plt.title(f'{bank_name} Stock Price Prediction (Test Data)')
    plt.xlabel('Date')
    plt.ylabel('Price (INR)')
    plt.legend()
    plt.savefig(f'../results/plots/{bank_name.lower()}_predictions.png')
    plt.show()
    
    return predictions_inv, y_test_inv, dates

# Generate for all banks
sbi_pred, sbi_actual, sbi_dates = predict_and_plot('SBI', '../data/raw/SBI.csv')
hdfc_pred, hdfc_actual, hdfc_dates = predict_and_plot('HDFC', '../data/raw/HDFC.csv')
icici_pred, icici_actual, icici_dates = predict_and_plot('ICICI', '../data/raw/ICICI.csv')
# ----
from sklearn.metrics import mean_squared_error, mean_absolute_error

def calculate_metrics(y_true, y_pred, bank_name):
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    
    return {
        'Bank': bank_name,
        'MSE': mse,
        'MAE': mae,
        'RMSE': rmse,
        'MAPE (%)': mape
    }

metrics_list = []
if sbi_pred is not None: metrics_list.append(calculate_metrics(sbi_actual, sbi_pred, 'SBI'))
if hdfc_pred is not None: metrics_list.append(calculate_metrics(hdfc_actual, hdfc_pred, 'HDFC'))
if icici_pred is not None: metrics_list.append(calculate_metrics(icici_actual, icici_pred, 'ICICI'))

metrics_df = pd.DataFrame(metrics_list)
print("\n--- Performance Metrics Comparison ---")
print(metrics_df)
metrics_df.to_csv('../results/performance_metrics.csv', index=False)
print("\nMetrics saved to results/performance_metrics.csv")
# ----
from tensorflow.keras.layers import RepeatVector, TimeDistributed

def create_autoencoder(input_shape):
    model = Sequential([
        # Encoder
        LSTM(64, activation='relu', input_shape=input_shape, return_sequences=True),
        LSTM(32, activation='relu', return_sequences=False),
        RepeatVector(input_shape[0]),
        # Decoder
        LSTM(32, activation='relu', return_sequences=True),
        LSTM(64, activation='relu', return_sequences=True),
        TimeDistributed(Dense(input_shape[1]))
    ])
    model.compile(optimizer='adam', loss='mae')
    return model

print("LSTM Autoencoder architecture defined.")
# ----
def prepare_ae_data(file_path, window_size=60):
    # We need the full scaled data as 3D sequences for the Autoencoder
    df = pd.read_csv(file_path, thousands=',')
    df['DATE'] = pd.to_datetime(df['DATE'], format='%d-%b-%Y')
    df = df.sort_values('DATE')
    df['CLOSE'] = pd.to_numeric(df['CLOSE'], errors='coerce')
    df = df.dropna(subset=['CLOSE'])
    df = df.groupby('DATE').mean(numeric_only=True)
    data = df['CLOSE'].values.reshape(-1, 1)
    
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data)
    
    X = []
    for i in range(window_size, len(scaled_data)):
        X.append(scaled_data[i-window_size:i])
    
    X = np.array(X)
    return X, scaler, df.index[window_size:]

print("Autoencoder data preparation function defined.")
# ----
from tensorflow.keras.models import load_model

def detect_anomalies(bank_name, file_path):
    print(f"\n{'='*40}")
    print(f"Detecting Anomalies for {bank_name}")
    print(f"{'='*40}")
    
    X, scaler, dates = prepare_ae_data(file_path)
    model_path = f'../results/models/{bank_name.lower()}_autoencoder.keras'
    model = load_model(model_path)
    
    # Predict (reconstruct)
    X_pred = model.predict(X)
    
    # Calculate reconstruction MAE loss
    reconstruction_loss = np.mean(np.abs(X_pred - X), axis=(1, 2))
    
    # Define threshold (mean + 3*std is often used for outlier detection)
    threshold = np.mean(reconstruction_loss) + 3 * np.std(reconstruction_loss)
    print(f"Threshold set at: {threshold:.4f}")
    
    # Identify anomalies
    anomalies = reconstruction_loss > threshold
    print(f"Number of anomalies detected: {np.sum(anomalies)}")
    
    # Plot
    # Get actual closing prices corresponding to the sequences (last element of each sequence)
    actual_prices = scaler.inverse_transform(X[:, -1, :])
    anomaly_prices = actual_prices[anomalies]
    anomaly_dates = dates[anomalies]
    
    plt.figure(figsize=(15, 7))
    plt.plot(dates, actual_prices, label='Closing Price', color='blue')
    plt.scatter(anomaly_dates, anomaly_prices, color='red', label='Anomaly', s=50)
    plt.title(f'{bank_name} Stock Price Anomalies')
    plt.xlabel('Date')
    plt.ylabel('Price (INR)')
    plt.legend()
    plt.savefig(f'../results/plots/{bank_name.lower()}_anomalies.png')
    plt.show()
    
    return anomaly_dates, anomaly_prices, threshold

# Run for all banks
sbi_anom_dates, sbi_anom_prices, sbi_thresh = detect_anomalies('SBI', '../data/raw/SBI.csv')
hdfc_anom_dates, hdfc_anom_prices, hdfc_thresh = detect_anomalies('HDFC', '../data/raw/HDFC.csv')
icici_anom_dates, icici_anom_prices, icici_thresh = detect_anomalies('ICICI', '../data/raw/ICICI.csv')
# ----
