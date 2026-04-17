def trend_analysis(df):
    df['Rolling_Mean'] = df['Temperature'].rolling(window=12).mean()
    return df