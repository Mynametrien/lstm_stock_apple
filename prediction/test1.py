from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import load_model
import yfinance as yf

def prediction_the_price():
    ticker = yf.Ticker("AAPL")
    data = ticker.history(period="120d")
    data = data.copy()

    # Lấy cột Adj Close
    data = data['Close']

    # Scale dữ liệu
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data.values.reshape(-1, 1))

    # Tạo input đầu vào mô hình
    X_input = scaled_data[-100:].reshape(1, 100, 1)

    # Load mô hình
    model_path = "C:\\Users\\admin\\OneDrive\\Desktop\\test\\lstm_stock_apple\\prediction\\model.keras"
    model = load_model(model_path)

    # Dự đoán
    prediction = model.predict(X_input)

    # Scale ngược để lấy giá trị thực
    predicted_price = scaler.inverse_transform(prediction)[0][0]
    print(f"Giá dự đoán cho ngày mai: {predicted_price:.2f} USD")

prediction_the_price()
