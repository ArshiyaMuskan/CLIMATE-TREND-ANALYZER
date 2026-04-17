import pandas as pd
import numpy as np
import os

# ✅ Create folder FIRST
os.makedirs("data/raw", exist_ok=True)

dates = pd.date_range(start="2000-01-01", periods=300)

temperature = 20 + np.sin(np.arange(300)/12) + np.random.normal(0,1,300)

df = pd.DataFrame({
    "Date": dates,
    "Temperature": temperature
})

# ✅ THEN save file
df.to_csv("data/raw/climate_data.csv", index=False)

print("Dataset created successfully!")