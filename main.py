from src.data_loader import load_data
from src.preprocessing import clean_data
from src.analysis import trend_analysis
from src.anomaly import detect_anomalies
from src.forecasting import forecast
from src.visualization import plot_forecasts

# Load
df = load_data("data/raw/climate_data.csv")

# Process
df = clean_data(df)
df = trend_analysis(df)
df = detect_anomalies(df)

# Forecast
forecast_df = forecast(df)

# Plot
plot_forecasts(df, forecast_df)

print("✅ Project executed successfully!")