from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import numpy as np

# Function to fit LSTM model and make predictions
def fit_lstm(data):
    scaler = MinMaxScaler()
    data_normalized = scaler.fit_transform(np.array(data).reshape(-1, 1))

    time_steps = 3
    X, y = create_dataset(data_normalized, time_steps)

    X = np.reshape(X, (X.shape[0], X.shape[1], 1))

    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(X.shape[1], 1)))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')

    model.fit(X, y, epochs=50, batch_size=1, verbose=2)

    train_predict = model.predict(X)
    predictions_lstm = scaler.inverse_transform(train_predict)

    plt.figure(figsize=(10, 6))
    plt.plot(data.values, label='Actual')
    plt.plot(np.arange(time_steps, len(data)), predictions_lstm, color='purple', label='LSTM Predictions')
    plt.title('LSTM Model for Stock Prediction')
    plt.legend()
    plt.show()

    mse = mean_squared_error(data.values[time_steps:], predictions_lstm)
    print("MSE for LSTM:", mse)

# Apply LSTM to each dataset
fit_lstm(ibm['Close'])
fit_lstm(aapl['Close'])
fit_lstm(fb['Close'])
fit_lstm(googl['Close'])
