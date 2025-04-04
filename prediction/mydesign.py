# Form implementation generated from reading ui file 'designer.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(867, 505)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chonfile = QtWidgets.QPushButton(parent=self.centralwidget)
        self.chonfile.setGeometry(QtCore.QRect(660, 120, 93, 28))
        self.chonfile.setObjectName("chonfile")
        self.dubao = QtWidgets.QPushButton(parent=self.centralwidget)
        self.dubao.setGeometry(QtCore.QRect(660, 180, 93, 28))
        self.dubao.setObjectName("dubao")
        self.vebd = QtWidgets.QPushButton(parent=self.centralwidget)
        self.vebd.setGeometry(QtCore.QRect(660, 240, 160, 28))
        self.vebd.setObjectName("Vebd")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(230, 160, 291, 41))
        self.textEdit.setObjectName("textEdit")
        self.dubao_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dubao_2.setGeometry(QtCore.QRect(120, 170, 111, 16))
        self.dubao_2.setObjectName("dubao_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 867, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.chonfile.clicked.connect(self.Handle_the_file)
        self.dubao.clicked.connect(self.prediction_the_price)
        self.vebd.clicked.connect(self.plot_graph)
        self.path=""
        self.prediction=0
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.filepath=""

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chonfile.setText(_translate("MainWindow", "Chon file "))
        self.dubao.setText(_translate("MainWindow", "Du bao"))
        self.dubao_2.setText(_translate("MainWindow", "Du bao ngay mai "))
        self.vebd.setText("Ve bieu do duong")
    #
    def Handle_the_file(self):
        dialog = QFileDialog()
        dialog.exec()
        dialog.setNameFilter( "CSV Files (*.csv)")
        path =dialog.selectedFiles()
        self.filepath = path[0]
        print(self.filepath)

    def prediction_the_price(self):
        df =pd.read_csv(self.filepath)
        data_test = df[:-1]
        print(df)
        data = data_test["Adj Close"].values
        model_path = "C:\\Users\\admin\\OneDrive\\Desktop\\test\\lstm_stock_apple\\prediction\\model.keras"
        X_input = data[-100:].reshape(1, 100, 1)
        print(X_input)
        model = load_model(model_path)
        self.prediction = model.predict(X_input)
        print(f"Predicted value for the day after tomorrow: {self.prediction}")
        self.textEdit.setText(str(self.prediction[0][0]*100))

    def plot_graph(self):
     
        df=pd.read_csv(self.filepath)
        data=df[-100:]
        data= data["Adj Close"]
        data= data.reset_index(drop=True)
        full_data = np.append(data, self.prediction)
        dates = np.arange(1, len(full_data) + 1)  # Trục thời gian giả định (số ngày)

        # Vẽ biểu đồ
        plt.figure(figsize=(12, 6))
        plt.plot(dates[:-1], data, label="Actual Adj Close", color='blue')  # Dữ liệu thực tế
        plt.scatter(dates[-1], self.prediction*100, color='red', label="Tomorrow's Predictions")  # Giá trị dự đoán
        plt.axvline(x=len(dates)-1, color='red', linestyle='--', label="The line separating today from tomorrow")  # Điểm phân chia dự đoán

        # Thêm thông tin vào biểu đồ
        plt.title("Adj Close vs Tomorrow's Predictions")
        plt.xlabel("Days")
        plt.ylabel("Adj Close Value")
        plt.legend()
        print(data)

        plt.show()
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
