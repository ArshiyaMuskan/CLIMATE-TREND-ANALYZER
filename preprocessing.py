import pandas as pd
def clean_data(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.dropna()
    return df