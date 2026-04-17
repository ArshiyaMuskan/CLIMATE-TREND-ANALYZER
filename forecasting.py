import pandas as pd
import numpy as np

TARGET_COL = 'Temperature'

# ===============================
# Linear Regression
# ===============================
def linear_forecast(df):
    df = df.copy()

    df['day'] = df.index.day
    df['month'] = df.index.month
    df['day_of_year'] = df.index.dayofyear

    X = df[['day', 'month', 'day_of_year']]
    y = df[TARGET_COL]

    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(X, y)

    future = pd.date_range(start=df.index[-1], periods=30)

    future_df = pd.DataFrame({
        'day': future.day,
        'month': future.month,
        'day_of_year': future.dayofyear
    })

    return model.predict(future_df)


# ===============================
# ARIMA
# ===============================
def arima_forecast(df):
    from statsmodels.tsa.arima.model import ARIMA

    model = ARIMA(df[TARGET_COL], order=(5,1,0))
    model_fit = model.fit()

    return model_fit.forecast(steps=30).values


# ===============================
# LSTM
# ===============================
def lstm_forecast(df):
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import LSTM, Dense
    from sklearn.preprocessing import MinMaxScaler

    data = df[TARGET_COL].values.reshape(-1,1)

    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(data)

    X, y = [], []
    time_step = 10

    for i in range(time_step, len(data_scaled)):
        X.append(data_scaled[i-time_step:i])
        y.append(data_scaled[i])

    X, y = np.array(X), np.array(y)

    model = Sequential([
        LSTM(50, input_shape=(X.shape[1],1)),
        Dense(1)
    ])

    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=5, verbose=0)

    last_seq = data_scaled[-time_step:]
    preds = []

    for _ in range(30):
        pred = model.predict(last_seq.reshape(1,time_step,1), verbose=0)
        preds.append(pred[0][0])
        last_seq = np.append(last_seq[1:], pred, axis=0)

    return scaler.inverse_transform(np.array(preds).reshape(-1,1)).flatten()


# ===============================
# RMSE
# ===============================
from sklearn.metrics import mean_squared_error

def rmse(actual, pred):
    return np.sqrt(mean_squared_error(actual, pred))


# ===============================
# MAIN FORECAST
# ===============================
def forecast(df):
    print("\n📊 Running Forecast Models...\n")

    df = df.copy()
    df.index = pd.to_datetime(df.index)

    if TARGET_COL not in df.columns:
        raise ValueError(f"Column {TARGET_COL} not found. Available: {list(df.columns)}")

    lr_pred = linear_forecast(df)
    arima_pred = arima_forecast(df)
    lstm_pred = lstm_forecast(df)

    # RMSE
    actual = df[TARGET_COL].values[-30:]

    print("\n📉 RMSE:")
    print("Linear:", rmse(actual, lr_pred[:30]))
    print("ARIMA:", rmse(actual, arima_pred[:30]))
    print("LSTM:", rmse(actual, lstm_pred[:30]))

    results = pd.DataFrame({
        'Linear': lr_pred,
        'ARIMA': arima_pred,
        'LSTM': lstm_pred
    })

    results.to_csv("outputs/forecast_results.csv", index=False)

    print("\n✅ Forecast saved!")

    return results