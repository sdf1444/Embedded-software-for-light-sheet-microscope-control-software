# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'laser.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from mqtt import *
from PyQt5 import QtCore, QtWidgets
import os
import configparser
import time
import json

class Ui_Laser(object):
    def setupUi(self, Laser):
        Laser.setObjectName("Laser")
        Laser.resize(379, 268)
        Laser.setMinimumSize(QtCore.QSize(379, 268))
        self.centralwidget = QtWidgets.QWidget(Laser)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 6, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 4, 1, 2)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 9, 0, 1, 2)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 8, 8, 1, 2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 8, 4, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 10, 1, 2)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 4, 10, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 7, 4, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 2)
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 9, 2, 1, 2)
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setMaximum(100)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.gridLayout.addWidget(self.verticalSlider, 5, 0, 2, 1)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 7, 8, 1, 2)
        self.verticalSlider_4 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_4.setMaximum(100)
        self.verticalSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_4.setInvertedAppearance(False)
        self.verticalSlider_4.setInvertedControls(False)
        self.verticalSlider_4.setObjectName("verticalSlider_4")
        self.gridLayout.addWidget(self.verticalSlider_4, 6, 6, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 9, 12, 1, 2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 8, 2, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 8, 0, 1, 2)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 4, 6, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 8, 1, 2)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.clicked.connect(self.btnstate4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 6, 1, 2)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.clicked.connect(self.btnstate5)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 3, 8, 1, 2)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 4, 8, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 9, 4, 1, 2)
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 9, 10, 1, 2)
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 7, 10, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 12, 1, 2)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 3, 12, 1, 2)
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 7, 12, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setCheckable(True)
        self.pushButton.clicked.connect(self.btnstate)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 8, 6, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 2)
        self.verticalSlider_6 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_6.setMaximum(100)
        self.verticalSlider_6.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_6.setObjectName("verticalSlider_6")
        self.gridLayout.addWidget(self.verticalSlider_6, 6, 10, 1, 1)
        self.verticalSlider_7 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_7.setMaximum(100)
        self.verticalSlider_7.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_7.setObjectName("verticalSlider_7")
        self.gridLayout.addWidget(self.verticalSlider_7, 6, 12, 1, 1)
        self.verticalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_3.setMaximum(100)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.gridLayout.addWidget(self.verticalSlider_3, 6, 4, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.clicked.connect(self.btnstate3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 4, 1, 2)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 7, 6, 1, 2)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 4, 12, 1, 1)
        self.verticalSlider_5 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_5.setMaximum(100)
        self.verticalSlider_5.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_5.setObjectName("verticalSlider_5")
        self.gridLayout.addWidget(self.verticalSlider_5, 6, 8, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 8, 12, 1, 2)
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 9, 6, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.clicked.connect(self.btnstate2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 2, 1, 2)
        self.verticalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_2.setMaximum(100)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.gridLayout.addWidget(self.verticalSlider_2, 6, 2, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 8, 10, 1, 2)
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 9, 8, 1, 2)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.clicked.connect(self.btnstate6)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 3, 10, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 7, 2, 1, 2)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 4, 4, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setChecked(True)
        self.pushButton_8.clicked.connect(self.on)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 1, 0, 1, 2)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setChecked(True)
        self.pushButton_7.clicked.connect(self.stop)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 1, 2, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 2, 1, 1)
        Laser.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Laser)
        self.statusbar.setObjectName("statusbar")
        Laser.setStatusBar(self.statusbar)
        self.retranslateUi(Laser)
        QtCore.QMetaObject.connectSlotsByName(Laser)
    
    def btnstate(self):
        if not os.path.exists("laser.ini"):
            if self.pushButton.isChecked():
                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/445nm")
                client.subscribe("microscope/light_sheet_microscope/UI/laser/445nm")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/445nm")
                client.publish("microscope/light_sheet_microscope/UI/laser/445nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "445nm", "cmd": "turning on"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("445nm laser turned on")
                
                self.pushButton_9.clicked.connect(self.printValue)
            else:
                self.pushButton_9.clicked.connect(self.printValue)
                self.pushButton_9.clicked.disconnect(self.printValue)
                self.verticalSlider.setValue(0)
                self.lineEdit.clear()
                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/445nm")
                client.subscribe("microscope/light_sheet_microscope/UI/laser/445nm")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/445nm")
                client.publish("microscope/light_sheet_microscope/UI/laser/445nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "445nm", "cmd": "turning off"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("445nm laser turned off")                
        else:
            if self.pushButton.isChecked():
                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/445nm")
                client.subscribe("microscope/light_sheet_microscope/UI/laser/445nm")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/445nm")
                client.publish("microscope/light_sheet_microscope/UI/laser/445nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "445nm", "cmd": "turning on"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("445nm laser turned on")
                
                self.pushButton_9.clicked.connect(self.printValue)
                
                config = configparser.RawConfigParser()
                config.read("laser.ini")
                try:
                    self.verticalSlider.setValue(config.getint("445nm", "intensity"))
                    self.lineEdit.setText(str(config.getint("445nm", "intensity")))
                except Exception as e:
                    pass
            else:
                try:
                    self.pushButton_9.clicked.disconnect(self.printValue)
                except Exception as e:
                    pass
                self.verticalSlider.setValue(0)
                self.lineEdit.clear()
                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/445nm")
                client.subscribe("microscope/light_sheet_microscope/UI/laser/445nm")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/445nm")
                client.publish("microscope/light_sheet_microscope/UI/laser/445nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "445nm", "cmd": "turning off"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("445nm laser turned off")
    
    def btnstate2(self):
        if not os.path.exists("laser.ini"):
            if self.pushButton_2.isChecked():
                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/488nm")
                client.subscribe("microscope/light_sheet_microscope/UI/laser/488nm")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/488nm")
                client.publish("microscope/light_sheet_microscope/UI/laser/488nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "488nm", "cmd": "turned on"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("488nm laser turned on")
                
                self.pushButton_10.clicked.connect(self.printValue2)
            else:
                self.pushButton_10.clicked.connect(self.printValue2)
                self.pushButton_10.clicked.disconnect(self.printValue2)
                self.verticalSlider_2.setValue(0)
                self.lineEdit_3.clear()
                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/488nm")
                client.subscribe("microscope/light_sheet_microscope/UI/laser/488nm")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/488nm")
                client.publish("microscope/light_sheet_microscope/UI/laser/488nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "488nm", "cmd": "turning off"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("488nm laser turned off")    

        else:
            if self.pushButton_2.isChecked():
                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/488nm")
                client.subscribe("microscope/light_sheet_microscope/UI/laser/488nm")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/488nm")
                client.publish("microscope/light_sheet_microscope/UI/laser/488nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "488nm", "cmd": "turning on"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("488nm laser turned on")
                
                self.pushButton_10.clicked.connect(self.printValue2)

                config = configparser.RawConfigParser()
                config.read("laser.ini")
                
                try:
                    self.verticalSlider_2.setValue(config.getint("488nm", "intensity"))
                    self.lineEdit_2.setText(str(config.getint("488nm", "intensity")))
                except Exception as e:
                    pass
            else:
                self.pushButton_10.clicked.connect(self.printValue2)
                self.pushButton_10.clicked.disconnect(self.printValue2)
                self.verticalSlider_2.setValue(0)
                self.lineEdit_2.clear()
                
                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/488nm")
                client.subscribe("microscope/light_sheet_microscope/UI/laser/488nm")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/488nm")
                client.publish("microscope/light_sheet_microscope/UI/laser/488nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "488nm", "cmd": "turning off"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("488nm laser turned off")

    def btnstate3(self):
        if not os.path.exists("laser.ini"):
            if self.pushButton_3.isChecked():
                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/515nm")
                client.subscribe("microscope/light_sheet_microscope/UI/laser/515nm")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/515nm")
                client.publish("microscope/light_sheet_microscope/UI/laser/515nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "515nm", "cmd": "turning on"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("515nm laser turned on")
                
                self.pushButton_11.clicked.connect(self.printValue3)
            else:
                self.pushButton_11.clicked.connect(self.printValue3)
                self.pushButton_11.clicked.disconnect(self.printValue3)
                self.verticalSlider_3.setValue(0)
                self.lineEdit_3.clear()
                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/515nm")
                client.subscribe("microscope/light_sheet_microscope/UI/laser/515nm")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/515nm")
                client.publish("microscope/light_sheet_microscope/UI/laser/515nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "515nm", "cmd": "turning off"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("515nm laser turned off")    
        else:
            if self.pushButton_3.isChecked():
                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/515nm")
                client.subscribe("microscope/light_sheet_microscope/UI/laser/515nm")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/515nm")
                client.publish("microscope/light_sheet_microscope/UI/laser/515nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "515nm", "cmd": "turning on"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("515nm laser turned on")
                
                self.pushButton_11.clicked.connect(self.printValue3)

                config = configparser.RawConfigParser()
                config.read("laser.ini")
                
                try:
                    self.verticalSlider_3.setValue(config.getint("515nm", "intensity"))
                    self.lineEdit_3.setText(str(config.getint("515nm", "intensity")))
                except Exception as e:
                    pass    
            
            else:
                self.pushButton_11.clicked.disconnect(self.printValue3)
                self.verticalSlider_3.setValue(0)
                self.lineEdit_3.clear()

                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/515nm")
                client.subscribe("microscope/light_sheet_microscope/UI/laser/515nm")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/515nm")
                client.publish("microscope/light_sheet_microscope/UI/laser/515nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "515nm", "cmd": "turning off"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("515nm laser turned off")

    def btnstate4(self):
        if not os.path.exists("laser.ini"):
            if self.pushButton_4.isChecked():
                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/561nm")
                client.subscribe("microscope/light_sheet_microscope/UI/laser/561nm")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/561nm")
                client.publish("microscope/light_sheet_microscope/UI/laser/561nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "561nm", "cmd": "turned on"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("561nm laser turned on")
                
                self.pushButton_12.clicked.connect(self.printValue4)
            else:
                self.pushButton_12.clicked.connect(self.printValue4)
                self.pushButton_12.clicked.disconnect(self.printValue4)
                self.verticalSlider_4.setValue(0)
                self.lineEdit_4.clear()
                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/561nm")
                client.subscribe("microscope/light_sheet_microscope/UI/laser/561nm")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/561nm")
                client.publish("microscope/light_sheet_microscope/UI/laser/561nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "561nm", "cmd": "turning off"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("561nm laser turned off")    
        else:
            if self.pushButton_4.isChecked():
                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/561nm")
                client.subscribe("microscope/light_sheet_microscope/UI/laser/561nm")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/561nm")
                client.publish("microscope/light_sheet_microscope/UI/laser/561nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "561nm", "cmd": "turning on"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("561nm laser turned on")
                
                self.pushButton_12.clicked.connect(self.printValue4)

                config = configparser.RawConfigParser()
                config.read("laser.ini")

                try:
                    self.verticalSlider_4.setValue(config.getint("561nm", "intensity"))
                    self.lineEdit_4.setText(str(config.getint("561nm", "intensity")))
                except Exception as e:
                    pass

            else:
                self.pushButton_12.clicked.disconnect(self.printValue4)
                self.verticalSlider_4.setValue(0)
                self.lineEdit_4.clear()

                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/561nm")
                client.subscribe("microscope/light_sheet_microscope/UI/laser/561nm")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/561nm")
                client.publish("microscope/light_sheet_microscope/UI/laser/561nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "561nm", "cmd": "turning off"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("515nm laser turned off")

    def btnstate5(self):
        if not os.path.exists("laser.ini"):
            if self.pushButton_5.isChecked():
                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/594nm")
                client.subscribe("microscope/light_sheet_microscope/UI/laser/594nm")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/594nm")
                client.publish("microscope/light_sheet_microscope/UI/laser/594nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "594nm", "cmd": "turning on"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("594nm laser turned on")
                
                self.pushButton_13.clicked.connect(self.printValue5)
            else:
                self.pushButton_13.clicked.connect(self.printValue5)
                self.pushButton_13.clicked.disconnect(self.printValue5)
                self.verticalSlider_3.setValue(0)
                self.lineEdit_3.clear()
                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/594nm")
                client.subscribe("microscope/light_sheet_microscope/UI/laser/594nm")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/594nm")
                client.publish("microscope/light_sheet_microscope/UI/laser/594nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "594nm", "cmd": "turning off"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("594nm laser turned off")    
        else:
            if self.pushButton_5.isChecked():
                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/594nm")
                client.subscribe("microscope/light_sheet_microscope/UI/laser/594nm")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/594nm")
                client.publish("microscope/light_sheet_microscope/UI/laser/594nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "594nm", "cmd": "turning on"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("594nm laser turned on")

                self.pushButton_13.clicked.connect(self.printValue5)

                config = configparser.RawConfigParser()
                config.read("laser.ini")

                try:
                    self.verticalSlider_5.setValue(config.getint("594nm", "intensity"))
                    self.lineEdit_5.setText(str(config.getint("594nm", "intensity")))
                except Exception as e:
                    pass

            else:
                self.pushButton_13.clicked.disconnect(self.printValue5)
                self.verticalSlider_5.setValue(0)
                self.lineEdit_5.clear()

                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/594nm")
                client.subscribe("microscope/light_sheet_microscope/UI/laser/594nm")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/594nm")
                client.publish("microscope/light_sheet_microscope/UI/laser/594nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "594nm", "cmd": "turning off"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("594nm laser turned off")

    def btnstate6(self):
        if not os.path.exists("laser.ini"):
            if self.pushButton_6.isChecked():
                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/638nm")
                client.subscribe("microscope/light_sheet_microscope/UI/laser/638nm")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/638nm")
                client.publish("microscope/light_sheet_microscope/UI/laser/638nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "638nm", "cmd": "turning on"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("638nm laser turned on")
                
                self.pushButton_14.clicked.connect(self.printValue6)
            else:
                self.pushButton_14.clicked.connect(self.printValue6)
                self.pushButton_14.clicked.disconnect(self.printValue6)
                self.verticalSlider_6.setValue(0)
                self.lineEdit_6.clear()
                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/638nm")
                client.subscribe("microscope/light_sheet_microscope/UI/laser/638nm")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/638nm")
                client.publish("microscope/light_sheet_microscope/UI/laser/638nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "638nm", "cmd": "turning off"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("638nm laser turned off")    
        else:
            if self.pushButton_6.isChecked():
                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/638nm")
                client.subscribe("microscope/light_sheet_microscope/UI/laser/638nm")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/638nm")
                client.publish("microscope/light_sheet_microscope/UI/laser/638nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "638nm", "cmd": "turning on"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("638nm laser turned on")
                
                self.pushButton_14.clicked.connect(self.printValue6)

                config = configparser.RawConfigParser()
                config.read("laser.ini")
                
                try:
                    self.verticalSlider_6.setValue(config.getint("638nm", "intensity"))
                    self.lineEdit_6.setText(str(config.getint("638nm", "intensity")))
                except Exception as e:
                    pass    

            else:
                self.pushButton_14.clicked.disconnect(self.printValue6)
                self.verticalSlider_6.setValue(0)
                self.lineEdit_6.clear()

                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/638nm")
                client.subscribe("microscope/light_sheet_microscope/UI/laser/638nm")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/638nm")
                client.publish("microscope/light_sheet_microscope/UI/laser/638nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "638nm", "cmd": "turning off"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("638nm laser turned off")

    def printValue(self):
        if not os.path.exists("laser.ini"):
            textboxValue = self.lineEdit.text()
            if self.lineEdit.text() == "":
                self.verticalSlider.setValue(0)
            else:
                self.verticalSlider.setValue(int(textboxValue))

            client = device()
            client.run()
            client.loop_start()
            print("\n" + "Connected to broker")
            time.sleep(1)
            print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/445nm")
            client.subscribe("microscope/light_sheet_microscope/UI/laser/445nm")
            print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/445nm")
            client.publish("microscope/light_sheet_microscope/UI/laser/445nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "445nm", "intensity": textboxValue + "%", "cmd": "set intensity of laser"}}, indent=2))
            time.sleep(1)
            client.loop_stop()
            
            print("Intensity: " + textboxValue + "%")

            config = configparser.RawConfigParser()

            f = open("laser.ini", "w")
            config.add_section("445nm")
            config.set("445nm", "intensity", textboxValue + "%")
            config.add_section("Subscriptions")
            config.set("Subscriptions", "445nm", "microscope/light_sheet_microscope/UI/laser/445nm")
            config.write(f)
        
        else:
            textboxValue = self.lineEdit.text()            
            if self.lineEdit.text() == "":
                self.verticalSlider.setValue(0)            
            else:
                self.verticalSlider.setValue(int(textboxValue))
            client = device()
            client.run()

            client.loop_start()
            print("\n" + "Connected to broker")
            time.sleep(1)
            print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/445nm")
            client.subscribe("microscope/light_sheet_microscope/UI/laser/445nm")
            print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/445nm")
            client.publish("microscope/light_sheet_microscope/UI/laser/445nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "445nm", "intensity": textboxValue + "%", "cmd": "set intensity of laser"}}, indent=2))
            time.sleep(1)
            client.loop_stop()

            print("Intensity: " + textboxValue + "%")
            
            config = configparser.RawConfigParser()
            config.read("laser.ini")

            f = open("laser.ini", "w")
            try:
                config.add_section("445nm")
            except Exception as e:
                pass

            try:
                config.set("445nm", "intensity", textboxValue)
            except Exception as e:
                pass
            try:
                config.add_section("Subscriptions")
            except Exception as e:
                pass                
            config.set("Subscriptions", "445nm", "microscope/light_sheet_microscope/UI/laser/445nm")
            config.write(f)
                        
    def printValue2(self):
        if not os.path.exists("laser.ini"):
            textboxValue2 = self.lineEdit_2.text()
            if self.lineEdit_2.text() == "":
                self.verticalSlider_2.setValue(0)
            else:
                self.verticalSlider_2.setValue(int(textboxValue2))

            client = device()
            client.run()
            client.loop_start()
            print("\n" + "Connected to broker")
            time.sleep(1)
            print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/488nm")
            client.subscribe("microscope/light_sheet_microscope/UI/laser/488nm")
            print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/488nm")
            client.publish("microscope/light_sheet_microscope/UI/laser/488nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "488nm", "intensity": textboxValue2 + "%", "cmd": "set intensity of laser"}}, indent=2))
            time.sleep(1)
            client.loop_stop()
            
            print("Intensity: " + textboxValue2 + "%")

            config = configparser.RawConfigParser()

            f = open("laser.ini", "w")
            config.add_section("488nm")
            config.set("488nm", "intensity", textboxValue2 + "%")
            config.add_section("Subscriptions")
            config.set("Subscriptions", "488nm", "microscope/light_sheet_microscope/UI/laser/488nm")
            config.write(f)
        
        else:
            textboxValue2 = self.lineEdit_2.text()            
            if self.lineEdit_2.text() == "":
                self.verticalSlider_2.setValue(0)            
            else:
                self.verticalSlider_2.setValue(int(textboxValue2))
            client = device()
            client.run()

            client.loop_start()
            print("\n" + "Connected to broker")
            time.sleep(1)
            print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/488nm")
            client.subscribe("microscope/light_sheet_microscope/UI/laser/488nm")
            print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/488nm")
            client.publish("microscope/light_sheet_microscope/UI/laser/488nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "488nm", "intensity": textboxValue2 + "%", "cmd": "set intensity of laser"}}, indent=2))
            time.sleep(1)
            client.loop_stop()

            print("Intensity: " + textboxValue2 + "%")
            
            config = configparser.RawConfigParser()
            config.read("laser.ini")

            f = open("laser.ini", "w")
            try:
                config.add_section("488nm")
            except Exception as e:
                pass
            config.set("488nm", "intensity", textboxValue2)
            
            try:
                config.add_section("Subscriptions")
            except Exception as e:
                pass
            config.set("Subscriptions", "488nm", "microscope/light_sheet_microscope/UI/laser/488nm")
            config.write(f)

    def printValue3(self):
        if not os.path.exists("laser.ini"):
            textboxValue3 = self.lineEdit_3.text()
            if self.lineEdit_3.text() == "":
                self.verticalSlider_3.setValue(0)
            else:
                self.verticalSlider_3.setValue(int(textboxValue3))

            client = device()
            client.run()
            client.loop_start()
            print("\n" + "Connected to broker")
            time.sleep(1)
            print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/515nm")
            client.subscribe("microscope/light_sheet_microscope/UI/laser/515nm")
            print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/515nm")
            client.publish("microscope/light_sheet_microscope/UI/laser/515nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "515nm", "intensity": textboxValue3 + "%", "cmd": "set intensity of laser"}}, indent=2))
            time.sleep(1)
            client.loop_stop()
            
            print("Intensity: " + textboxValue3 + "%")

            config = configparser.RawConfigParser()

            f = open("laser.ini", "w")
            config.add_section("515nm")
            config.set("515nm", "intensity", textboxValue3 + "%")
            config.add_section("Subscriptions")
            config.set("Subscriptions", "515nm", "microscope/light_sheet_microscope/UI/laser/515nm")
            config.write(f)
        
        else:
            textboxValue3 = self.lineEdit_3.text()            
            if self.lineEdit_3.text() == "":
                self.verticalSlider_3.setValue(0)            
            else:
                self.verticalSlider_3.setValue(int(textboxValue3))
            client = device()
            client.run()

            client.loop_start()
            print("\n" + "Connected to broker")
            time.sleep(1)
            print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/515nm")
            client.subscribe("microscope/light_sheet_microscope/UI/laser/515nm")
            print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/515nm")
            client.publish("microscope/light_sheet_microscope/UI/laser/515nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "515nm", "intensity": textboxValue3 + "%", "cmd": "set intensity of laser"}}, indent=2))
            time.sleep(1)
            client.loop_stop()

            print("Intensity: " + textboxValue3 + "%")
            
            config = configparser.RawConfigParser()
            config.read("laser.ini")

            f = open("laser.ini", "w")
            try:
                config.add_section("515nm")
            except Exception as e:
                pass
            config.set("515nm", "intensity", textboxValue3)
            try:
                config.add_section("Subscriptions")
            except Exception as e:
                pass
            config.set("Subscriptions", "515nm", "microscope/light_sheet_microscope/UI/laser/445nm")
            config.write(f)

    def printValue4(self):
        if not os.path.exists("laser.ini"):
            textboxValue4 = self.lineEdit_4.text()
            if self.lineEdit_4.text() == "":
                self.verticalSlider_4.setValue(0)
            else:
                self.verticalSlider_4.setValue(int(textboxValue4))

            client = device()
            client.run()

            client.loop_start()
            print("\n" + "Connected to broker")
            time.sleep(1)
            print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/561nm")
            client.subscribe("microscope/light_sheet_microscope/UI/laser/561nm")
            print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/561nm")
            client.publish("microscope/light_sheet_microscope/UI/laser/561nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "561nm", "intensity": textboxValue4 + "%", "cmd": "set intensity of laser"}}, indent=2))
            time.sleep(1)
            client.loop_stop()

            print("Intensity: " + textboxValue4 + "%")
            
            config = configparser.RawConfigParser()

            f = open("laser.ini", "w")
            config.add_section("561nm")
            config.set("561nm", "intensity", textboxValue4)
            config.add_section("Subscriptions")
            config.set("Subscriptions", "561nm", "microscope/light_sheet_microscope/UI/laser/561nm")
            config.write(f)          
        
        else:
            textboxValue4 = self.lineEdit_4.text()            
            if self.lineEdit_4.text() == "":
                self.verticalSlider_4.setValue(0)            
            else:
                self.verticalSlider_4.setValue(int(textboxValue4))
            client = device()
            client.run()

            client.loop_start()
            print("\n" + "Connected to broker")
            time.sleep(1)
            print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/561nm")
            client.subscribe("microscope/light_sheet_microscope/UI/laser/561nm")
            print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/561nm")
            client.publish("microscope/light_sheet_microscope/UI/laser/561nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "561nm", "intensity": textboxValue4 + "%", "cmd": "set intensity of laser"}}, indent=2))
            time.sleep(1)
            client.loop_stop()

            print("Intensity: " + textboxValue4 + "%")
            
            config = configparser.RawConfigParser()
            config.read("laser.ini")

            f = open("laser.ini", "w")
            try:
                config.add_section("561nm")
            except Exception as e:
                pass
            config.set("561nm", "intensity", textboxValue4)
            try:
                config.add_section("Subscriptions")
            except Exception as e:
                pass
            config.set("Subscriptions", "561nm", "microscope/light_sheet_microscope/UI/laser/561nm")
            config.write(f)

    def printValue5(self):
        if not os.path.exists("laser.ini"):
            textboxValue5 = self.lineEdit_5.text()
            if self.lineEdit_5.text() == "":
                self.verticalSlider_5.setValue(0)
            else:
                self.verticalSlider_5.setValue(int(textboxValue5))
            
            client = device()
            client.run()

            client.loop_start()
            print("\n" + "Connected to broker")
            time.sleep(1)
            print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/594nm")
            client.subscribe("microscope/light_sheet_microscope/UI/laser/594nm")
            print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/594nm")
            client.publish("microscope/light_sheet_microscope/UI/laser/594nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "594nm", "intensity": textboxValue5 + "%", "cmd": "set intensity of laser"}}, indent=2))
            time.sleep(1)
            client.loop_stop()

            print("Intensity: " + textboxValue5 + "%")
            
            config = configparser.RawConfigParser()

            f = open("laser.ini", "w")
            config.add_section("594nm")
            config.set("594nm", "intensity", textboxValue5)
            config.add_section("Subscriptions")
            config.set("Subscriptions", "594nm", "microscope/light_sheet_microscope/UI/laser/594nm")
            config.write(f)
        
        else:
            textboxValue5 = self.lineEdit_5.text()            
            if self.lineEdit_5.text() == "":
                self.verticalSlider_5.setValue(0)            
            else:
                self.verticalSlider_5.setValue(int(textboxValue5))
            client = device()
            client.run()

            client.loop_start()
            print("\n" + "Connected to broker")
            time.sleep(1)
            print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/594nm")
            client.subscribe("microscope/light_sheet_microscope/UI/laser/594nm")
            print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/594nm")
            client.publish("microscope/light_sheet_microscope/UI/laser/594nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "594nm", "intensity": textboxValue5 + "%", "cmd": "set intensity of laser"}}, indent=2))
            time.sleep(1)
            client.loop_stop()
            
            print("Intensity: " + textboxValue5 + "%")
            
            config = configparser.RawConfigParser()
            config.read("laser.ini")

            f = open("laser.ini", "w")
            try:
                config.add_section("594nm")
            except Exception as e:
                pass
            config.set("594nm", "intensity", textboxValue5)
            try:
                config.add_section("Subscriptions")
            except Exception as e:
                pass
            config.set("Subscriptions", "594nm", "microscope/light_sheet_microscope/UI/laser/594nm")
            config.write(f)

    def printValue6(self):
        if not os.path.exists("laser.ini"):
            textboxValue6 = self.lineEdit_6.text()
            if self.lineEdit_6.text() == "":
                self.verticalSlider_6.setValue(0)
            else:
                self.verticalSlider_6.setValue(int(textboxValue6))
            
            client = device()
            client.run()

            client.loop_start()
            print("\n" + "Connected to broker")
            time.sleep(1)
            print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/638nm")
            client.subscribe("microscope/light_sheet_microscope/UI/laser/638nm")
            print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/638nm")
            client.publish("microscope/light_sheet_microscope/UI/laser/638nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "638nm", "intensity": textboxValue6 + "%", "cmd": "set intensity of laser"}}, indent=2))
            time.sleep(1)
            client.loop_stop()

            print("Intensity: " + textboxValue6 + "%") 
            
            config = configparser.RawConfigParser()
            config.read("laser.ini")

            f = open("laser.ini", "w")
            config.add_section("638nm")
            config.set("638nm", "intensity", textboxValue6)
            config.add_section("Subscriptions")
            config.set("Subscriptions", "638nm", "microscope/light_sheet_microscope/UI/laser/638nm")
            config.write(f)
        
        else:
            textboxValue6 = self.lineEdit_6.text()            
            if self.lineEdit_6.text() == "":
                self.verticalSlider_6.setValue(0)            
            else:
                self.verticalSlider_6.setValue(int(textboxValue6))
            client = device()
            client.run()

            client.loop_start()
            print("\n" + "Connected to broker")
            time.sleep(1)
            print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser/638nm")
            client.subscribe("microscope/light_sheet_microscope/UI/laser/638nm")
            print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser/638nm")
            client.publish("microscope/light_sheet_microscope/UI/laser/638nm", json.dumps({"type": "device", "payload":{"name": "laser", "wavelength": "638nm", "intensity": textboxValue6 + "%", "cmd": "set intensity of laser"}}, indent=2))
            time.sleep(1)
            client.loop_stop()
            
            print("Intensity: " + textboxValue6 + "%") 
            
            config = configparser.RawConfigParser()
            config.read("laser.ini")

            f = open("laser.ini", "w")
            try:
                config.add_section("638nm")
            except Exception as e:
                pass
            config.set("638nm", "intensity", textboxValue6)
            try:
                config.add_section("Subscriptions")
            except Exception as e:
                pass
            config.set("Subscriptions", "638nm", "microscope/light_sheet_microscope/UI/laser/638nm")
            config.write(f)

    def on(self):
        if self.pushButton_8.isChecked():
            if os.path.exists("laser.ini"):
                config = configparser.RawConfigParser()
                config.read("laser.ini")
                
                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser")
                client.subscribe("microscope/light_sheet_microscope/UI/laser")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser")
                client.publish("microscope/light_sheet_microscope/UI/laser", json.dumps({"type": "device", "payload":{"name": "laser", "cmd": "laser turning on"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("Laser turned on")
                self.pushButton_7.clicked.connect(self.stop)
                self.pushButton.setCheckable(True)
                self.pushButton.clicked.connect(self.btnstate)
                self.pushButton_2.setCheckable(True)
                self.pushButton_2.clicked.connect(self.btnstate2)
                self.pushButton_3.setCheckable(True)
                self.pushButton_3.clicked.connect(self.btnstate3)
                self.pushButton_4.setCheckable(True)
                self.pushButton_4.clicked.connect(self.btnstate4)
                self.pushButton_5.setCheckable(True)
                self.pushButton_5.clicked.connect(self.btnstate5)
                self.pushButton_6.setCheckable(True)
                self.pushButton_6.clicked.connect(self.btnstate6)
                
            else:
                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser")
                client.subscribe("microscope/light_sheet_microscope/UI/laser")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser")
                client.publish("microscope/light_sheet_microscope/UI/laser", json.dumps({"type": "device", "payload":{"name": "laser", "cmd": "laser turning on"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("Laser turned on")                
                
                print("Laser config file does not exist")
                self.pushButton.setCheckable(True)
                self.pushButton.clicked.connect(self.btnstate)
                self.pushButton_2.setCheckable(True)
                self.pushButton_2.clicked.connect(self.btnstate2)
                self.pushButton_3.setCheckable(True)
                self.pushButton_3.clicked.connect(self.btnstate3)
                self.pushButton_4.setCheckable(True)
                self.pushButton_4.clicked.connect(self.btnstate4)
                self.pushButton_5.setCheckable(True)
                self.pushButton_5.clicked.connect(self.btnstate5)
                self.pushButton_6.setCheckable(True)
                self.pushButton_6.clicked.connect(self.btnstate6)
                self.pushButton_7.clicked.connect(self.stop)
        else:
            pass

    def stop(self):
        client = device()
        client.run()

        client.loop_start()
        print("\n" + "Connected to broker")
        time.sleep(1)
        print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser")
        client.subscribe("microscope/light_sheet_microscope/UI/laser")
        print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser")
        client.publish("microscope/light_sheet_microscope/UI/laser", json.dumps({"type": "device", "payload":{"name": "laser", "cmd": "device turning off"}}, indent=2))
        time.sleep(1)
        client.loop_stop()
        self.pushButton_7.clicked.disconnect(self.stop)
        self.pushButton_8.setChecked(False)
        try:
            self.pushButton.setChecked(False)
            self.pushButton.setCheckable(False)
            self.pushButton.clicked.disconnect(self.btnstate)
        except Exception as e:
            pass
        try:
            self.pushButton_9.clicked.disconnect(self.printValue)
        except Exception as e:
            pass
        self.verticalSlider.setValue(0)
        self.lineEdit.clear()        
        # self.pushButton_2.setCheckable(False)
        try:            
            self.pushButton_2.setChecked(False)
            self.pushButton_2.setCheckable(False)
            self.pushButton_2.clicked.disconnect(self.btnstate2)
        except Exception as e:
            pass
        try:
            self.pushButton_10.clicked.disconnect(self.printValue2)
        except Exception as e:
            pass
        self.verticalSlider_2.setValue(0)
        self.lineEdit_2.clear()
        # self.pushButton_3.setCheckable(False)
        try:
            self.pushButton_3.setChecked(False)
            self.pushButton_3.setCheckable(False)
            self.pushButton_3.clicked.disconnect(self.btnstate3)
        except Exception as e:
            pass
        try:
            self.pushButton_11.clicked.disconnect(self.printValue3)
        except Exception as e:
            pass
        self.verticalSlider_3.setValue(0)
        self.lineEdit_3.clear()
        # self.pushButton_4.setCheckable(False)
        try:
            self.pushButton_4.setChecked(False)
            self.pushButton_4.setCheckable(False)
            self.pushButton_4.clicked.disconnect(self.btnstate4)
        except Exception as e:
            pass
        try:
            self.pushButton_12.clicked.disconnect(self.printValue4)
        except Exception as e:
            pass
        self.verticalSlider_4.setValue(0)
        self.lineEdit_4.clear()

        # self.pushButton_5.setCheckable(False)
        try:
            self.pushButton_5.setChecked(False)
            self.pushButton_5.setCheckable(False)
            self.pushButton_5.clicked.disconnect(self.btnstate5)
        except Exception as e:
            pass
        try:
            self.pushButton_13.clicked.disconnect(self.printValue5)
        except Exception as e:
            pass
        self.verticalSlider_5.setValue(0)
        self.lineEdit_5.clear()

        # self.pushButton_6.setCheckable(False)
        try:
            self.pushButton_6.setChecked(False)
            self.pushButton_6.setCheckable(False)
            self.pushButton_6.clicked.disconnect(self.btnstate6)
        except Exception as e:
            pass
        try:
            self.pushButton_14.clicked.disconnect(self.printValue6)
        except Exception as e:
            pass
        self.verticalSlider_6.setValue(0)
        self.lineEdit_6.clear()
        print("Laser turned off")
    
    def retranslateUi(self, Laser):
        _translate = QtCore.QCoreApplication.translate
        Laser.setWindowTitle(_translate("Laser", "MainWindow"))
        self.label_9.setText(_translate("Laser", "0"))
        self.label_4.setText(_translate("Laser", "561nm"))
        self.label_3.setText(_translate("Laser", "515nm"))
        self.pushButton_9.setText(_translate("Laser", "Set"))
        self.label_6.setText(_translate("Laser", "638nm"))
        self.label_18.setText(_translate("Laser", "100"))
        self.label_13.setText(_translate("Laser", "0"))
        self.label.setText(_translate("Laser", "445nm"))
        self.pushButton_10.setText(_translate("Laser", "Set"))
        self.label_17.setText(_translate("Laser", "0"))
        self.pushButton_15.setText(_translate("Laser", "Set"))
        self.label_14.setText(_translate("Laser", "100"))
        self.label_5.setText(_translate("Laser", "594nm"))
        self.pushButton_4.setText(_translate("Laser", "ON"))
        self.pushButton_5.setText(_translate("Laser", "ON"))
        self.label_16.setText(_translate("Laser", "100"))
        self.pushButton_11.setText(_translate("Laser", "Set"))
        self.pushButton_14.setText(_translate("Laser", "Set"))
        self.label_19.setText(_translate("Laser", "0"))
        self.label_7.setText(_translate("Laser", "LED"))
        self.pushButton_7.setText(_translate("Laser", "ON"))
        self.label_20.setText(_translate("Laser", "0"))
        self.pushButton.setText(_translate("Laser", "ON"))
        self.label_2.setText(_translate("Laser", "488nm"))
        self.pushButton_3.setText(_translate("Laser", "ON"))
        self.label_15.setText(_translate("Laser", "0"))
        self.label_21.setText(_translate("Laser", "100"))
        self.pushButton_12.setText(_translate("Laser", "Set"))
        self.pushButton_2.setText(_translate("Laser", "ON"))
        self.pushButton_13.setText(_translate("Laser", "Set"))
        self.pushButton_6.setText(_translate("Laser", "ON"))
        self.label_10.setText(_translate("Laser", "0"))
        self.label_12.setText(_translate("Laser", "100"))
        self.pushButton_8.setText(_translate("Laser", "ON"))
        self.pushButton_7.setText(_translate("Laser", "OFF"))
        self.label_8.setText(_translate("Laser", "100"))
        self.label_11.setText(_translate("Laser", "100"))

        def getConfig():
            if os.path.exists("laser.ini"):
                config = configparser.RawConfigParser()
                config.read("laser.ini")
                try:
                    self.verticalSlider.setValue(config.getint("445nm", "intensity"))
                    print("455nm laser set")
                    self.pushButton.setChecked(True)
                except Exception as e:
                    print("455nm laser not set")

                try:
                    self.lineEdit.setText(str(config.getint("445nm", "intensity")))
                    print("455nm laser textbox set")
                except Exception as e:
                    print("455nm laser textbox not set")

                try:
                    self.verticalSlider_2.setValue(config.getint("488nm", "intensity"))
                    print("488nm laser set")
                    self.pushButton_2.setChecked(True)
                except Exception as e:
                    print("488nm laser not set")

                try:
                    self.lineEdit_2.setText(str(config.getint("488nm", "intensity")))
                    print("488nm laser textbox set")
                except Exception as e:
                    print("488nm laser textbox not set")

                try:
                    self.verticalSlider_3.setValue(config.getint("515nm", "intensity"))
                    print("515nm laser set")
                    self.pushButton_3.setChecked(True)
                except Exception as e:
                    print("515nm laser not set")

                try:
                    self.lineEdit_3.setText(str(config.getint("515nm", "intensity")))
                    print("515nm laser textbox set")
                except Exception as e:
                    print("515nm laser textbox not set")

                try:
                    self.verticalSlider_4.setValue(config.getint("561nm", "intensity"))
                    print("561nm laser set")
                    self.pushButton_4.setChecked(True)
                except Exception as e:
                    print("561nm laser not set")

                try:
                    self.lineEdit_4.setText(str(config.getint("561nm", "intensity")))
                    print("561nm laser textbox set")
                except Exception as e:
                    print("561nm laser textbox not set")

                try:
                    self.verticalSlider_5.setValue(config.getint("594nm", "intensity"))
                    print("594nm laser set")
                    self.pushButton_5.setChecked(True)
                except Exception as e:
                    print("594nm laser not set")

                try:
                    self.lineEdit_5.setText(str(config.getint("594nm", "intensity")))
                    print("594nm laser textbox set")
                except Exception as e:
                    print("594nm laser textbox not set")

                try:
                    self.verticalSlider_6.setValue(config.getint("638nm", "intensity"))
                    print("638nm laser set")
                    self.pushButton_6.setChecked(True)
                except Exception as e:
                    print("638nm laser not set")

                try:
                    self.lineEdit_6.setText(str(config.getint("638nm", "intensity")))
                    print("638nm laser textbox set")
                except Exception as e:
                    print("638nm laser textbox not set")
            else:
                print("Laser on")
                print("Laser config file does not exist")
        getConfig()

    # def printValue7(self):
    # 	textboxValue7 = self.lineEdit_7.text()
    # 	print("hi")
    # 	print(textboxValue7)
    # 	if self.lineEdit_7.text() == "":
    # 		self.verticalSlider_7.setValue(0)
    # 	else:
    # 		self.verticalSlider_7.setValue(int(textboxValue7))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Laser = QtWidgets.QMainWindow()
    ui = Ui_Laser()
    ui.setupUi(Laser)
    Laser.show()
    sys.exit(app.exec_())