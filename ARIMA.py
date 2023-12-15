import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

# Load the stock data
ibm_data = pd.read_csv('IBM_stock.csv', index_col='Date', parse_dates=True)['Close']
aapl_data = pd.read_csv('Apple_stock.csv', index_col='Date', parse_dates=True)['Close']
fb_data = pd.read_csv('Facebook_stock.csv', index_col='Date', parse_dates=True)['Close']
googl_data = pd.read_csv('Google_stock.csv', index_col='Date', parse_dates=True)['Close']

# Estimate the parameters for each stock using the AIC criterion
ibm_model = ARIMA(ibm_data, order=(1, 1, 1)).fit()
aapl_model = ARIMA(aapl_data, order=(2, 1, 0)).fit()
fb_model = ARIMA(fb_data, order=(1, 1, 2)).fit()
googl_model = ARIMA(googl_data, order=(2, 1, 1)).fit()

# Print the summary of the models
print("Summary of ARIMA model for IBM:")
print(ibm_model.summary())

print("Summary of ARIMA model for AAPL:")
print(aapl_model.summary())

print("Summary of ARIMA model for FB:")
print(fb_model.summary())

print("Summary of ARIMA model for GOOGL:")
print(googl_model.summary())

# Make predictions and evaluate the performance
# (This part is not included in the original question, but can be added to compare the performance of ARIMA with other models)
