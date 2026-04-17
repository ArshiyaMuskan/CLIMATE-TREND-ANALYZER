import matplotlib.pyplot as plt
import pandas as pd

def plot_forecasts(df, forecast_df):
    plt.figure(figsize=(12,6))

    plt.plot(df.index, df['Temperature'], label='Actual')

    future_index = pd.date_range(start=df.index[-1], periods=len(forecast_df))

    plt.plot(future_index, forecast_df['Linear'], '--', label='Linear')
    plt.plot(future_index, forecast_df['ARIMA'], '--', label='ARIMA')
    plt.plot(future_index, forecast_df['LSTM'], '--', label='LSTM')

    plt.legend()
    plt.title("Forecast Comparison")

    plt.savefig("outputs/forecast_comparison.png")
    plt.show()