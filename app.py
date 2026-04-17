import streamlit as st
import pandas as pd
from src.forecasting import forecast

# Title
st.title("🌍 Climate Trend Analyzer")

# Load data
df = pd.read_csv("data/raw/climate_data.csv", parse_dates=['Date'], index_col='Date')

# Show historical data
st.subheader("📊 Historical Temperature")
st.line_chart(df['Temperature'])

# Forecast button
if st.button("🚀 Run Forecast"):
    with st.spinner("Running models..."):
        results = forecast(df)

    st.success("✅ Forecast Completed!")

    st.subheader("📈 Forecast Results")
    st.write(results)

    st.line_chart(results)