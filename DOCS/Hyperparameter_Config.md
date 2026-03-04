# LSTM Hyperparameter Configuration

This document outlines the architecture and hyperparameters chosen for the LSTM model predicting bank stock prices (SBI, HDFC, ICICI). The structure of these hyperparameters references the standards used in stock prediction survey papers.

## 1. Architecture Parameters
These define the structural layers and network size of the models.
* **Hidden layer units:** 50 units per LSTM layer
* **Multi-layer depth:** 3 LSTM layers
* **Sequence length (window size):** 60 days
* **Dropout rate:** 0.2 (applied after each LSTM layer to prevent overfitting)
* **Input Shape:** `(60, 5)` representing 60 timesteps with 5 features (Open, High, Low, Close, Volume)

## 2. Optimization/Learning Parameters
These are the settings tuned during the iterative model training process.
* **Learning rate:** 0.001 (default for Adam optimizer)
* **Batch size:** 32
* **Iteration count (epochs):** 50
* **Momentum / Weight decay:** Handled adaptively by the Adam optimizer
* **Validation Split:** 10% of training data

## 3. Algorithm Specific Parameters
Settings unique to the architecture or learning objective of the LSTM model algorithm.
* **Number of neurons:** 150 total LSTM neurons across the depth (50x3) plus 1 Dense output neuron.
* **Optimization Function:** Adam Optimizer
* **Loss Function:** Mean Squared Error (MSE)
* **Regularization (Callbacks):**
    * **Early Stopping:** Stops if `val_loss` doesn't improve for 10 epochs, restoring best weights.
    * **Model Checkpointing:** Saves the model state when validation loss minimizes.

## 4. Evaluation Metrics
The chosen metrics to evaluate predictive accuracy and generalizability as per reference papers.
* **Error Metrics:** RMSE (Root Mean Squared Error), MAE (Mean Absolute Error), MSE (Mean Squared Error)
* **Statistical Fits:** R-squared
* (Applicable for Anomaly Detection later: Precision, Recall, F1 score)

--- 
This configuration satisfies the deliverables for Week 3 Model Building Phase and is mapped closely to the provided survey papers on prediction model hyperparameters.
