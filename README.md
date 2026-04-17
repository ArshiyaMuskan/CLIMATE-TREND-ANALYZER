
# 🌍 Climate Trend Analyzer

An end-to-end Data Science & Machine Learning project that analyzes historical climate data, detects trends and anomalies, and forecasts future temperature using multiple models including Linear Regression, ARIMA, and LSTM.

---

## 🚀 Project Overview

The **Climate Trend Analyzer** is designed to:

- 📊 Analyze historical climate data  
- 📈 Identify long-term trends  
- 🚨 Detect anomalies  
- 🤖 Forecast future temperatures using ML & DL models  
- 🌐 Provide an interactive dashboard using Streamlit  

---

## 🧠 Models Used

| Model              | Description |
|-------------------|------------|
| Linear Regression | Baseline trend prediction |
| ARIMA             | Time series forecasting |
| LSTM (TensorFlow) | Deep learning-based prediction |

---

## 📉 Evaluation Metric

We use **RMSE (Root Mean Squared Error)** to compare model performance.

Example:

```

Linear: 1.22
ARIMA: 1.16
LSTM: 1.23

```

---

## 🏗️ Project Structure

```

DS CLIMATE TREND ANALYZER/
│
├── app/
│   └── app.py                # Streamlit Dashboard
│
├── data/
│   ├── raw/
│   │   └── climate_data.csv
│   └── simulate_data.py
│
├── outputs/
│   ├── forecast_results.csv
│   ├── forecast_comparison.png
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── analysis.py
│   ├── anomaly.py
│   ├── forecasting.py
│   ├── lstm.py
│   └── visualization.py
│
├── main.py
├── requirements.txt
└── README.md

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/climate-trend-analyzer.git
cd climate-trend-analyzer
````

---

### 2️⃣ Create virtual environment

```bash
python -m venv tf_env
tf_env\Scripts\activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### 🔹 Run backend pipeline

```bash
python main.py
```

---

### 🔹 Run Streamlit Dashboard

```bash
python -m streamlit run app/app.py
```

---

## 🌐 Live Demo

👉 http://localhost:8501/

---

## 📊 Features

* ✔️ Data preprocessing & cleaning
* ✔️ Trend analysis
* ✔️ Anomaly detection
* ✔️ Multi-model forecasting
* ✔️ RMSE comparison
* ✔️ Interactive dashboard


## 🔮 Future Enhancements

* 📡 Real-time climate API integration
* 🌍 Multi-region analysis
* 📊 Advanced visualizations
* ⚡ Model optimization (hyperparameter tuning)
* ☁️ Cloud deployment with CI/CD

---

## 🛠️ Tech Stack

* Python 🐍
* Pandas & NumPy
* Matplotlib
* Scikit-learn
* Statsmodels (ARIMA)
* TensorFlow (LSTM)
* Streamlit

---

## 🤝 Contribution

Contributions are welcome! Feel free to fork and improve the project.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👩‍💻 Author

**Arshiya Muskan**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
```

