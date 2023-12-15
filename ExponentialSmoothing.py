from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import pandas as pd
import matplotlib.pyplot as plt

# Load data
ibm = pd.read_csv('IBM_stock.csv', parse_dates=True, index_col='Date')
aapl = pd.read_csv('Apple_stock.csv', parse_dates=True, index_col='Date')
fb = pd.read_csv('Facebook_stock.csv', parse_dates=True, index_col='Date')
googl = pd.read_csv('Google_stock.csv', parse_dates=True, index_col='Date')

# Function to fit ARIMA model and make predictions
def fit_arima(data):
    model = ARIMA(data, order=(5, 1, 2))  # Adjust order as needed
    arima_fit = model.fit()

    # Make predictions
    predictions = arima_fit.predict(start=len(data), end=len(data) + 10, dynamic=False)

    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(data, label='Actual')
    plt.plot(predictions, color='red', label='ARIMA Predictions')
    plt.title('ARIMA Model for Stock Prediction')
    plt.legend()
    plt.show()

    # Calculate MSE
    mse = mean_squared_error(data[-10:], predictions)
    print("MSE for ARIMA:", mse)

# Apply ARIMA to each dataset
fit_arima(ibm['Close'])
fit_arima(aapl['Close'])
fit_arima(fb['Close'])
fit_arima(googl['Close'])
