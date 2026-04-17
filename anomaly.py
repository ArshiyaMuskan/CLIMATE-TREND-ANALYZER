def detect_anomalies(df):
    mean = df['Temperature'].mean()
    std = df['Temperature'].std()

    df['Anomaly'] = ((df['Temperature'] - mean).abs() > 2*std)
    return df