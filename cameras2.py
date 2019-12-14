# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cameras.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import os
import configparser
import time
import json
from mqtt import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(468, 336)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 6, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 5, 1, 1, 2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 6, 1, 1, 1)
        self.lineEdit_2.returnPressed.connect(self.leftCamera)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 5, 4, 1, 3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 8, 1, 1, 1)
        self.lineEdit_4.returnPressed.connect(self.topROI)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 8, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 6, 6, 1, 2)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 9, 7, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 8, 2, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 6, 4, 1, 2)
        self.lineEdit_3.returnPressed.connect(self.rightCamera)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 9, 3, 1, 2)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 8, 7, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 4, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 8, 3, 1, 2)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 10, 0, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 9, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 1, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 3, 6, 1, 2)
        self.lineEdit_8.returnPressed.connect(self.delay)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 3, 8, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 9, 1, 1, 1)
        self.lineEdit_5.returnPressed.connect(self.widthROI)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 8, 5, 1, 1)
        self.lineEdit_6.returnPressed.connect(self.leftROI)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 9, 5, 1, 1)
        self.lineEdit_7.returnPressed.connect(self.heightROI)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 6, 1, 2)
        self.lineEdit.returnPressed.connect(self.exposureTime)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setMaximum(5000)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 2, 0, 1, 6)
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setChecked(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 0, 0, 1, 1)
        self.pushButton_10.clicked.connect(self.on)
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.clicked.connect(self.stop)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 0, 2, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def exposureTime(self):
    	if not os.path.exists("cameras.ini"):
    		textboxValue = self.lineEdit.text()

    		client = device()
    		client.run()
    		client.loop_start()
    		print("\n" + "Connected to broker")
    		time.sleep(1)
    		print("Subscribing to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.subscribe("microscope/light_sheet_microscope/UI/cameras")
    		print("Publishing message to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.publish("microscope/light_sheet_microscope/UI/cameras", json.dumps({"type": "device", "payload":{"name": "cameras", "exposure time": textboxValue, "cmd": "set exposure time of cameras"}}, indent=2))
    		time.sleep(1)
    		client.loop_stop()

    		print("Exposure time: " + textboxValue + "ms")

    		config = configparser.RawConfigParser()

    		f = open("cameras.ini", "w")
    		config.add_section("Exposure")
    		config.set("Exposure", "time", textboxValue + "ms")
    		config.write(f)

    	else:
    		textboxValue = self.lineEdit.text()

    		client = device()
    		client.run()

    		client.loop_start()
    		print("\n" + "Connected to broker")
    		time.sleep(1)
    		print("Subscribing to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.subscribe("microscope/light_sheet_microscope/UI/cameras")
    		print("Publishing message to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.publish("microscope/light_sheet_microscope/UI/cameras", json.dumps({"type": "device", "payload":{"name": "cameras", "exposure time": textboxValue, "cmd": "set exposure time of cameras"}}, indent=2))
    		time.sleep(1)
    		client.loop_stop()

    		print("Exposure time: " + textboxValue + "ms")

    		config = configparser.RawConfigParser()
    		config.read("cameras.ini")

    		f = open("cameras.ini", "w")
    		try:
    			config.add_section("Exposure")
    		except Exception as e:
    			pass
    		try:
    			config.set("Exposure", "time", textboxValue + "ms")
    		except Exception as e:
    			pass
    		config.write(f)

    def delay(self):
    	if not os.path.exists("cameras.ini"):
    		textboxValue2 = self.lineEdit_8.text()

    		client = device()
    		client.run()

    		client.loop_start()
    		print("\n" + "Connected to broker")
    		time.sleep(1)
    		print("Subscribing to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.subscribe("microscope/light_sheet_microscope/UI/cameras")
    		print("Publishing message to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.publish("microscope/light_sheet_microscope/UI/cameras", json.dumps({"type": "device", "payload":{"name": "cameras", "delay": textboxValue2, "cmd": "set delay of cameras"}}, indent=2))
    		time.sleep(1)
    		client.loop_stop()
    		
    		print("Delay: " + textboxValue2 + "ms")

    		config = configparser.RawConfigParser()

    		f = open("cameras.ini", "w")
    		config.add_section("Delay")
    		config.set("Delay", "time", textboxValue + "ms")
    		config.write(f)    	

    	else:
    		textboxValue2 = self.lineEdit_8.text()

    		client = device()
    		client.run()

    		client.loop_start()
    		print("\n" + "Connected to broker")
    		time.sleep(1)
    		print("Subscribing to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.subscribe("microscope/light_sheet_microscope/UI/cameras")
    		print("Publishing message to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.publish("microscope/light_sheet_microscope/UI/cameras", json.dumps({"type": "device", "payload":{"name": "cameras", "delay": textboxValue2, "cmd": "set delay of cameras"}}, indent=2))
    		time.sleep(1)
    		client.loop_stop()

    		print("Delay: " + textboxValue2 + "ms")

    		config = configparser.RawConfigParser()
    		config.read("cameras.ini")

    		f = open("cameras.ini", "w")
    		try:
    			config.add_section("Delay")
    		except Exception as e:
    			pass
    		try:
    			config.set("Delay", "time", textboxValue2 + "ms")
    		except Exception as e:
    			pass
    		config.write(f)

    def leftCamera(self):
    	if not os.path.exists("cameras.ini"):
    		leftMode = self.comboBox.currentText()
    		textboxValue3 = self.lineEdit_2.text()

    		client = device()
    		client.run()

    		client.loop_start()
    		print("\n" + "Connected to broker")
    		time.sleep(1)
    		print("Subscribing to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.subscribe("microscope/light_sheet_microscope/UI/cameras")
    		print("Publishing message to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.publish("microscope/light_sheet_microscope/UI/cameras", json.dumps({"type": "device", "payload":{"name": "cameras", "left camera mode": leftMode, "left camera lines": textboxValue3 + "px", "cmd": "set left camera mode and left camera lines"}}, indent=2))
    		time.sleep(1)
    		client.loop_stop()
    		print("Left camera mode: " + leftMode)
    		print("Left camera lines: " + textboxValue3 + "px")

    		config = configparser.RawConfigParser()

    		f = open("cameras.ini", "w")
    		config.add_section("Left camera")
    		config.set("Left camera", "mode", leftMode)
    		config.set("Left camera", "lines", textboxValue3 + "px")
    		config.write(f)

    	else:
    		leftMode = self.comboBox.currentText()
    		textboxValue3 = self.lineEdit_2.text()

    		client = device()
    		client.run()

    		client.loop_start()
    		print("\n" + "Connected to broker")
    		time.sleep(1)
    		print("Subscribing to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.subscribe("microscope/light_sheet_microscope/UI/cameras")
    		print("Publishing message to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.publish("microscope/light_sheet_microscope/UI/cameras", json.dumps({"type": "device", "payload":{"name": "cameras", "left camera mode": leftMode, "left camera lines": textboxValue3 + "px", "cmd": "set left camera mode and left camera lines"}}, indent=2))
    		time.sleep(1)
    		client.loop_stop()
    		print("Left camera mode: " + leftMode)
    		print("Left camera lines: " + textboxValue3 + "px")

    		config = configparser.RawConfigParser()
    		config.read("cameras.ini")

    		f = open("cameras.ini", "w")
    		try:
    			config.add_section("Left camera")
    		except Exception as e:
    			pass
    		try:
    			config.set("Left camera", "mode", leftMode)
    		except Exception as e:
    			pass
    		try:
    			config.set("Left camera", "lines", textboxValue3 + "px")
    		except Exception as e:
    			pass
    		config.write(f)   	    	

    def rightCamera(self):
    	if not os.path.exists("cameras.ini"):
    		rightMode = self.comboBox_2.currentText()
    		textboxValue4 = self.lineEdit_3.text()

    		client = device()
    		client.run()

    		client.loop_start()
    		print("\n" + "Connected to broker")
    		time.sleep(1)
    		print("Subscribing to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.subscribe("microscope/light_sheet_microscope/UI/cameras")
    		print("Publishing message to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.publish("microscope/light_sheet_microscope/UI/cameras", json.dumps({"type": "device", "payload":{"name": "cameras", "right camera mode": rightMode, "right camera lines": textboxValue4 + "px", "cmd": "set right camera mode and right camera lines"}}, indent=2))
    		time.sleep(1)
    		client.loop_stop()
    		print("Right camera mode: " + rightMode)
    		print("Right camera lines: " + textboxValue4 + "px")

    		config = configparser.RawConfigParser()

    		f = open("cameras.ini", "w")
    		config.add_section("Right camera")
    		config.set("Right camera", "mode", rightMode)
    		config.set("Right camera", "lines", textboxValue4 + "px")
    		config.write(f)

    	else:
    		rightMode = self.comboBox_2.currentText()
    		textboxValue4 = self.lineEdit_3.text()

    		client = device()
    		client.run()

    		client.loop_start()
    		print("\n" + "Connected to broker")
    		time.sleep(1)
    		print("Subscribing to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.subscribe("microscope/light_sheet_microscope/UI/cameras")
    		print("Publishing message to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.publish("microscope/light_sheet_microscope/UI/cameras", json.dumps({"type": "device", "payload":{"name": "cameras", "right camera mode": rightMode, "right camera lines": textboxValue4 + "px", "cmd": "set right camera mode and right camera lines"}}, indent=2))
    		time.sleep(1)
    		client.loop_stop()
    		print("Right camera mode: " + rightMode)
    		print("Right camera lines: " + textboxValue4 + "px")

    		config = configparser.RawConfigParser()
    		config.read("cameras.ini")

    		f = open("cameras.ini", "w")
    		try:
    			config.add_section("Right camera")
    		except Exception as e:
    			pass
    		try:
    			config.set("Right camera", "Mode", rightMode)
    		except Exception as e:
    			pass
    		try:
    			config.set("Right camera", "Lines", textboxValue4 + "px")
    		except Exception as e:
    			pass
    		config.write(f)

    def topROI(self):
    	if not os.path.exists("cameras.ini"):
    		textboxValue5 = self.lineEdit_4.text()

    		client = device()
    		client.run()

    		client.loop_start()
    		print("\n" + "Connected to broker")
    		time.sleep(1)
    		print("Subscribing to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.subscribe("microscope/light_sheet_microscope/UI/cameras")
    		print("Publishing message to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.publish("microscope/light_sheet_microscope/UI/cameras", json.dumps({"type": "device", "payload":{"name": "cameras", "top ROI": textboxValue5 + "px", "cmd": "set top ROI"}}, indent=2))
    		time.sleep(1)
    		client.loop_stop()
    		print("Top ROI: " + textboxValue5 + "px")

    		config = configparser.RawConfigParser()

    		f = open("cameras.ini", "w")
    		config.add_section("Top ROI")
    		config.set("Top ROI", "ROI", textboxValue5 + "px")
    		config.write(f)

    	else:
    		textboxValue5 = self.lineEdit_4.text()

    		client = device()
    		client.run()

    		client.loop_start()
    		print("\n" + "Connected to broker")
    		time.sleep(1)
    		print("Subscribing to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.subscribe("microscope/light_sheet_microscope/UI/cameras")
    		print("Publishing message to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.publish("microscope/light_sheet_microscope/UI/cameras", json.dumps({"type": "device", "payload":{"name": "cameras", "top ROI": textboxValue5 + "px", "cmd": "set top ROI"}}, indent=2))
    		time.sleep(1)
    		client.loop_stop()
    		print("Top ROI: " + textboxValue5 + "px")

    		config = configparser.RawConfigParser()
    		config.read("cameras.ini")

    		f = open("cameras.ini", "w")
    		try:
    			config.add_section("Top ROI")
    		except Exception as e:
    			pass
    		try:
    			config.set("Top ROI", "ROI", textboxValue5 + "px")
    		except Exception as e:
    			pass
    		config.write(f)

    def leftROI(self):
    	if not os.path.exists("cameras.ini"):
    		textboxValue6 = self.lineEdit_6.text()

    		client = device()
    		client.run()

    		client.loop_start()
    		print("\n" + "Connected to broker")
    		time.sleep(1)
    		print("Subscribing to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.subscribe("microscope/light_sheet_microscope/UI/cameras")
    		print("Publishing message to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.publish("microscope/light_sheet_microscope/UI/cameras", json.dumps({"type": "device", "payload":{"name": "cameras", "left ROI": textboxValue6 + "px", "cmd": "set left ROI"}}, indent=2))
    		time.sleep(1)
    		client.loop_stop()
    		print("Left ROI: " + textboxValue6 + "px")

    		config = configparser.RawConfigParser()

    		f = open("cameras.ini", "w")
    		config.add_section("Left ROI")
    		config.set("Left ROI", "ROI", textboxValue6 + "px")
    		config.write(f)

    	else:
    		textboxValue6 = self.lineEdit_6.text()

    		client = device()
    		client.run()

    		client.loop_start()
    		print("\n" + "Connected to broker")
    		time.sleep(1)
    		print("Subscribing to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.subscribe("microscope/light_sheet_microscope/UI/cameras")
    		print("Publishing message to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.publish("microscope/light_sheet_microscope/UI/cameras", json.dumps({"type": "device", "payload":{"name": "cameras", "left ROI": textboxValue6 + "px", "cmd": "set left ROI"}}, indent=2))
    		time.sleep(1)
    		client.loop_stop()
    		print("Left ROI: " + textboxValue6 + "px")

    		config = configparser.RawConfigParser()
    		config.read("cameras.ini")

    		f = open("cameras.ini", "w")
    		try:
    			config.add_section("Left ROI")
    		except Exception as e:
    			pass
    		try:
    			config.set("Left ROI", "ROI", textboxValue6 + "px")
    		except Exception as e:
    			pass
    		config.write(f)

    def widthROI(self):
    	if not os.path.exists("cameras.ini"):
    		textboxValue7 = self.lineEdit_5.text()

    		client = device()
    		client.run()

    		client.loop_start()
    		print("\n" + "Connected to broker")
    		time.sleep(1)
    		print("Subscribing to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.subscribe("microscope/light_sheet_microscope/UI/cameras")
    		print("Publishing message to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.publish("microscope/light_sheet_microscope/UI/cameras", json.dumps({"type": "device", "payload":{"name": "cameras", "width ROI": textboxValue7 + "px", "cmd": "set width ROI"}}, indent=2))
    		time.sleep(1)
    		client.loop_stop()
    		print("Width ROI: " + textboxValue7 + "px")

    		config = configparser.RawConfigParser()

    		f = open("cameras.ini", "w")
    		config.add_section("Width ROI")
    		config.set("Width ROI", "ROI", textboxValue7 + "px")
    		config.write(f)

    	else:
    		textboxValue7 = self.lineEdit_5.text()

    		client = device()
    		client.run()

    		client.loop_start()
    		print("\n" + "Connected to broker")
    		time.sleep(1)
    		print("Subscribing to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.subscribe("microscope/light_sheet_microscope/UI/cameras")
    		print("Publishing message to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.publish("microscope/light_sheet_microscope/UI/cameras", json.dumps({"type": "device", "payload":{"name": "cameras", "width ROI": textboxValue7 + "px", "cmd": "set width ROI"}}, indent=2))
    		time.sleep(1)
    		client.loop_stop()
    		print("Width ROI: " + textboxValue7 + "px")

    		config = configparser.RawConfigParser()
    		config.read("cameras.ini")

    		f = open("cameras.ini", "w")
    		try:
    			config.add_section("Width ROI")
    		except Exception as e:
    			pass
    		try:
    			config.set("Width ROI", "ROI", textboxValue7 + "px")
    		except Exception as e:
    			pass
    		config.write(f)

    def heightROI(self):
    	if not os.path.exists("cameras.ini"):
    		textboxValue8 = self.lineEdit_7.text()

    		client = device()
    		client.run()

    		client.loop_start()
    		print("\n" + "Connected to broker")
    		time.sleep(1)
    		print("Subscribing to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.subscribe("microscope/light_sheet_microscope/UI/cameras")
    		print("Publishing message to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.publish("microscope/light_sheet_microscope/UI/cameras", json.dumps({"type": "device", "payload":{"name": "cameras", "height ROI": textboxValue8 + "px", "cmd": "set height ROI"}}, indent=2))
    		time.sleep(1)
    		client.loop_stop()
    		print("Height ROI: " + textboxValue8 + "px")

    		config = configparser.RawConfigParser()

    		f = open("cameras.ini", "w")
    		config.add_section("Cameras")
    		config.set("Height ROI", "ROI", textboxValue8 + "px")
    		config.write(f)

    	else:
    		textboxValue8 = self.lineEdit_7.text()

    		client = device()
    		client.run()

    		client.loop_start()
    		print("\n" + "Connected to broker")
    		time.sleep(1)
    		print("Subscribing to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.subscribe("microscope/light_sheet_microscope/UI/cameras")
    		print("Publishing message to topic", "microscope/light_sheet_microscope/UI/cameras")
    		client.publish("microscope/light_sheet_microscope/UI/cameras", json.dumps({"type": "device", "payload":{"name": "cameras", "height ROI": textboxValue8 + "px", "cmd": "set height ROI"}}, indent=2))
    		time.sleep(1)
    		client.loop_stop()
    		print("Height ROI: " + textboxValue8 + "px")

    		config = configparser.RawConfigParser()
    		config.read("cameras.ini")

    		f = open("cameras.ini", "w")
    		try:
    			config.add_section("Height ROI")
    		except Exception as e:
    			pass
    		try:
    			config.set("Height ROI", "ROI", textboxValue8 + "px")
    		except Exception as e:
    			pass
    		config.write(f)

    def stop(self):
        client = device()
        client.run()

        client.loop_start()
        print("\n" + "Connected to broker")
        time.sleep(1)
        print("Subscribing to topic", "microscope/light_sheet_microscope/UI/cameras")
        client.subscribe("microscope/light_sheet_microscope/UI/cameras")
        print("Publishing message to topic", "microscope/light_sheet_microscope/UI/cameras")
        client.publish("microscope/light_sheet_microscope/UI/cameras", json.dumps({"type": "device", "payload":{"name": "cameras", "cmd": "device turning off"}}, indent=2))
        time.sleep(1)
        client.loop_stop()

        print("Cameras turning off")

        self.pushButton_11.clicked.disconnect(self.stop)
        self.pushButton_10.setChecked(False)
        self.lineEdit.clear()
        self.lineEdit.returnPressed.disconnect(self.exposureTime)
        self.lineEdit_8.clear()
        self.lineEdit_8.returnPressed.disconnect(self.delay)
        self.lineEdit_2.clear()
        self.lineEdit_2.returnPressed.disconnect(self.leftCamera)
        self.lineEdit_3.clear()
        self.lineEdit_3.returnPressed.disconnect(self.rightCamera)
        self.lineEdit_4.clear()
        self.lineEdit_4.returnPressed.disconnect(self.topROI)
        self.lineEdit_5.clear()
        self.lineEdit_5.returnPressed.disconnect(self.widthROI)
        self.lineEdit_6.clear()
        self.lineEdit_6.returnPressed.disconnect(self.leftROI)
        self.lineEdit_7.clear()
        self.lineEdit_7.returnPressed.disconnect(self.heightROI)

    def on(self):
    	if self.pushButton_10.isChecked():
    		if os.path.exists("cameras.ini"):
    			config = configparser.RawConfigParser()
    			config.read("cameras.ini")

    			client = device()
    			client.run()

    			client.loop_start()
    			print("\n" + "Connected to broker")
    			time.sleep(1)
    			print("Subscribing to topic", "microscope/light_sheet_microscope/UI/cameras")
    			client.subscribe("microscope/light_sheet_microscope/UI/cameras")
    			print("Publishing message to topic", "microscope/light_sheet_microscope/UI/cameras")
    			client.publish("microscope/light_sheet_microscope/UI/cameras", json.dumps({"type": "device", "payload":{"name": "cameras", "cmd": "cameras turning on"}}, indent=2))
    			time.sleep(1)
    			client.loop_stop()
    			print("Cameras turned on")
    			self.pushButton_11.clicked.connect(self.stop)
    			self.pushButton_10.setCheckable(True)

    			self.lineEdit.returnPressed.connect(self.exposureTime)
    			self.lineEdit_8.returnPressed.connect(self.delay)
    			self.lineEdit_2.returnPressed.connect(self.leftCamera)
    			self.lineEdit_3.returnPressed.connect(self.rightCamera)
    			self.lineEdit_4.returnPressed.connect(self.topROI)
    			self.lineEdit_5.returnPressed.connect(self.widthROI)
    			self.lineEdit_6.returnPressed.connect(self.leftROI)
    			self.lineEdit_7.returnPressed.connect(self.heightROI)

    		else:
    			config = configparser.RawConfigParser()
    			config.read("cameras.ini")

    			client = device()
    			client.run()

    			client.loop_start()
    			print("\n" + "Connected to broker")
    			time.sleep(1)
    			print("Subscribing to topic", "microscope/light_sheet_microscope/UI/cameras")
    			client.subscribe("microscope/light_sheet_microscope/UI/cameras")
    			print("Publishing message to topic", "microscope/light_sheet_microscope/UI/cameras")
    			client.publish("microscope/light_sheet_microscope/UI/cameras", json.dumps({"type": "device", "payload":{"name": "cameras", "cmd": "cameras turning on"}}, indent=2))
    			time.sleep(1)
    			client.loop_stop()
    			print("Cameras turned on")
    			self.pushButton_11.clicked.connect(self.stop)
    			self.pushButton_10.setCheckable(True)

    			self.lineEdit.returnPressed.connect(self.exposureTime)
    			self.lineEdit_8.returnPressed.connect(self.delay)
    			self.lineEdit_2.returnPressed.connect(self.leftCamera)
    			self.lineEdit_3.returnPressed.connect(self.rightCamera)
    			self.lineEdit_4.returnPressed.connect(self.topROI)
    			self.lineEdit_5.returnPressed.connect(self.widthROI)
    			self.lineEdit_6.returnPressed.connect(self.leftROI)
    			self.lineEdit_7.returnPressed.connect(self.heightROI)   			


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "px"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Program"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Shutter Priority"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Aperture Priority"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Manual"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Program"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Shutter Priority"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Aperture Priority"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Manual"))
        self.pushButton.setText(_translate("MainWindow", "ms"))
        self.pushButton_3.setText(_translate("MainWindow", "px"))
        self.pushButton_7.setText(_translate("MainWindow", "px"))
        self.pushButton_4.setText(_translate("MainWindow", "px"))
        self.label_7.setText(_translate("MainWindow", "Lines"))
        self.label_10.setText(_translate("MainWindow", "Width"))
        self.label_3.setText(_translate("MainWindow", "Mode"))
        self.label_12.setText(_translate("MainWindow", "Height"))
        self.pushButton_6.setText(_translate("MainWindow", "px"))
        self.label_4.setText(_translate("MainWindow", "Left"))
        self.label_6.setText(_translate("MainWindow", "Right"))
        self.label.setText(_translate("MainWindow", "Exposure Time"))
        self.label_11.setText(_translate("MainWindow", "Left"))
        self.pushButton_8.setText(_translate("MainWindow", "Reset Crop ROI"))
        self.label_9.setText(_translate("MainWindow", "Top"))
        self.pushButton_5.setText(_translate("MainWindow", "px"))
        self.label_2.setText(_translate("MainWindow", "Delay"))
        self.label_8.setText(_translate("MainWindow", "Crop ROI"))
        self.pushButton_9.setText(_translate("MainWindow", "ms"))
        self.pushButton_10.setText(_translate("MainWindow", "ON"))
        self.pushButton_11.setText(_translate("MainWindow", "OFF"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())