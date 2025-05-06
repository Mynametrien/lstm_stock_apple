
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
from PyQt6 import QtCore, QtGui, QtWidgets
from    PyQt6.QtWidgets import QFileDialog
from sklearn.preprocessing import MinMaxScaler

import yfinance as yf
def prediction_the_price():
        ticker = yf.Ticker("AAPL")
        data = ticker.history(period="100d")  # lấy nhiều hơn 100d để có cổ tức
        data = data.copy()

        # Khởi tạo cột "Adjustment Factor"
        data['Adj Factor'] = 1.0

        # Duyệt từ ngày mới nhất về ngày cũ
        dates = data.index[::-1]  # đảo ngược thời gian
        for i in range(1, len(dates)):
            today = dates[i - 1]
            prev = dates[i]
            close_today = data.loc[today, 'Close']
            dividend = data.loc[prev, 'Dividends']
            split = data.loc[prev, 'Stock Splits']
            split_factor = split if split != 0 else 1.0
            adj = data.loc[today, 'Adj Factor'] / split_factor * (1 - dividend / close_today)
            data.loc[prev, 'Adj Factor'] = adj
        data['Adj Close'] = data['Close'] * data['Adj Factor']
        print(data['Adj Close'])
        data= data['Adj Close']
        model_path = "C:\\Users\\admin\\OneDrive\\Desktop\\test\\lstm_stock_apple\\prediction\\model.keras"
        X_input = np.array(data.values[-100:]).reshape(1, 100, 1)
        print(X_input)
        model = load_model(model_path)
        prediction = model.predict(X_input)
        #print(f"Predicted value for the day after tomorrow: {self.prediction} ")
       # self.textEdit.setText(str("{:.7f}".format(self.prediction[0][0]*100)) +' ' + 'USD')
       # self.label.setText( "Ngày gần nhất: " + self.ngay_gan_nhat())
        prediction = model.predict(X_input)
       

        print(prediction)
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