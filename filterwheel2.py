# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filterwheel.ui'
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
        MainWindow.resize(322, 161)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 0, 2, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 5, 0, 2, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.gridLayout.addWidget(self.comboBox_4, 5, 2, 2, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton.clicked.connect(self.on)
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setObjectName("pushButton2")
        self.gridLayout.addWidget(self.pushButton2, 0, 2, 1, 2)
        self.pushButton2.setChecked(True)
        self.pushButton2.clicked.connect(self.stop)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 5, 1, 2, 1)
        self.checkBox_2.setCheckable(True)
        self.checkBox_2.clicked.connect(self.link2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 2, 1, 2, 1)
        self.checkBox.setCheckable(True)
        self.checkBox.clicked.connect(self.link)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(6, "")
        self.gridLayout.addWidget(self.comboBox_2, 2, 2, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def link(self):
        if not os.path.exists("filter wheel.ini"):
            if self.checkBox.isChecked():
                leftFilterWheel = self.comboBox.currentText()
                rightFilterWheel = self.comboBox_2.currentText()

                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/filter wheel")
                client.subscribe("microscope/light_sheet_microscope/UI/filter wheel")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/filter wheel")
                client.publish("microscope/light_sheet_microscope/UI/filter wheel", json.dumps({"type": "device", "payload":{"name": "filter wheel", "left filter wheel": leftFilterWheel, "right filter wheel": rightFilterWheel, "cmd": "set filter wheels"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("Left filter wheel set") 
                print("Right filter wheel set")

                config = configparser.RawConfigParser()

                f = open("filter wheel.ini", "w")
                config.add_section("Filter wheels")
                config.set("Filter wheels", "left filter wheel", leftFilterWheel)
                config.set("Filter wheels", "right filter wheel", rightFilterWheel)
                config.write(f)
        else:
            leftFilterWheel = self.comboBox.currentText()
            rightFilterWheel = self.comboBox_2.currentText()

            client = device()
            client.run()

            client.loop_start()
            print("\n" + "Connected to broker")
            time.sleep(1)
            print("Subscribing to topic", "microscope/light_sheet_microscope/UI/filter wheel")
            client.subscribe("microscope/light_sheet_microscope/UI/filter wheel")
            print("Publishing message to topic", "microscope/light_sheet_microscope/UI/filter wheel")
            client.publish("microscope/light_sheet_microscope/UI/filter wheel", json.dumps({"type": "device", "payload":{"name": "filter wheel", "left filter wheel": leftFilterWheel, "right filter wheel": rightFilterWheel, "cmd": "set filter wheels"}}, indent=2))
            time.sleep(1)
            client.loop_stop()
            print("Left filter wheel set") 
            print("Right filter wheel set")

            config = configparser.RawConfigParser()
            config.read("filter wheel.ini")

            f = open("filter wheel.ini", "w")
            try:
                config.add_section("Filter wheels")
            except Exception as e:
                pass
            try:
                config.set("Filter wheels", "left filter wheel", leftFilterWheel)
            except Exception as e:
                pass
            try:
                config.set("Filter wheels", "right filter wheel", rightFilterWheel)
            except Exception as e:
                pass
            config.write(f)

    def link2(self):
        if not os.path.exists("filter wheel.ini"):
            if self.checkBox.isChecked():
                leftMagnificationChanger = self.comboBox_3.currentText()
                rightMagnificationChanger = self.comboBox_4.currentText()

                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/filter wheel")
                client.subscribe("microscope/light_sheet_microscope/UI/filter wheel")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/filter wheel")
                client.publish("microscope/light_sheet_microscope/UI/filter wheel", json.dumps({"type": "device", "payload":{"name": "filter wheel", "left filter wheel magnification changer": leftMagnificationChanger, "right filter wheel magnification changer": rightMagnificationChanger, "cmd": "set magnification of left and right filter wheels"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                print("Left filter wheel magnification set") 
                print("Right filter wheel magnification set")

                config = configparser.RawConfigParser()

                f = open("filter wheel.ini", "w")
                config.add_section("Filter wheels")
                config.set("Filter wheels", "left magnification changer", leftMagnificationChanger)
                config.set("Filter wheels", "right magnification changer", rightMagnificationChanger)
                config.write(f)
        else:
            leftMagnificationChanger = self.comboBox_3.currentText()
            rightMagnificationChanger = self.comboBox_4.currentText()

            client = device()
            client.run()

            client.loop_start()
            print("\n" + "Connected to broker")
            time.sleep(1)
            print("Subscribing to topic", "microscope/light_sheet_microscope/UI/filter wheel")
            client.subscribe("microscope/light_sheet_microscope/UI/filter wheel")
            print("Publishing message to topic", "microscope/light_sheet_microscope/UI/filter wheel")
            client.publish("microscope/light_sheet_microscope/UI/filter wheel", json.dumps({"type": "device", "payload":{"name": "filter wheel", "left filter wheel magnification changer": leftMagnificationChanger, "right filter wheel magnification changer": rightMagnificationChanger, "cmd": "set magnification of left and right filter wheels"}}, indent=2))            
            time.sleep(1)
            client.loop_stop()
            print("Left filter wheel magnification set") 
            print("Right filter wheel magnification set")

            config = configparser.RawConfigParser()
            config.read("filter wheel.ini")

            f = open("filter wheel.ini", "w")
            try:
                config.add_section("Filter wheels")
            except Exception as e:
                pass
            try:
                config.set("Filter wheels", "left magnification changer", leftMagnificationChanger)
            except Exception as e:
                pass
            try:
                config.set("Filter wheels", "right magnification changer", rightMagnificationChanger)
            except Exception as e:
                pass
            config.write(f)

    def stop(self):
        client = device()
        client.run()

        client.loop_start()
        print("\n" + "Connected to broker")
        time.sleep(1)
        print("Subscribing to topic", "microscope/light_sheet_microscope/UI/filter wheel")
        client.subscribe("microscope/light_sheet_microscope/UI/filter wheel")
        print("Publishing message to topic", "microscope/light_sheet_microscope/UI/filter wheel")
        client.publish("microscope/light_sheet_microscope/UI/filter wheel", json.dumps({"type": "device", "payload":{"name": "filter wheel", "cmd": "device turning off"}}, indent=2))
        time.sleep(1)
        client.loop_stop()
        print("Filter wheel turning off")
        
        self.pushButton2.clicked.disconnect(self.stop)
        self.pushButton.setChecked(False)
        self.checkBox.setChecked(False)
        self.checkBox.setCheckable(False)
        self.checkBox.clicked.disconnect(self.link)
        self.checkBox_2.setChecked(False)
        self.checkBox_2.setCheckable(False)
        self.checkBox_2.clicked.disconnect(self.link2)

    def on(self):
        if os.path.exists("filter wheel.ini"):
            config = configparser.RawConfigParser()
            config.read("filter wheel.ini")
            
            client = device()
            client.run()

            client.loop_start()
            print("\n" + "Connected to broker")
            time.sleep(1)
            print("Subscribing to topic", "microscope/light_sheet_microscope/UI/filter wheel")
            client.subscribe("microscope/light_sheet_microscope/UI/filter wheel")
            print("Publishing message to topic", "microscope/light_sheet_microscope/UI/filter wheel")
            client.publish("microscope/light_sheet_microscope/UI/filter wheel", json.dumps({"type": "device", "payload":{"name": "filter wheel", "cmd": "filter wheel turning on"}}, indent=2))
            time.sleep(1)
            client.loop_stop()
            print("Filter wheel turning on")
            
            self.pushButton2.clicked.connect(self.stop)
            self.pushButton.setChecked(True)
            self.checkBox.setChecked(True)
            self.checkBox.setCheckable(True)
            self.checkBox.clicked.connect(self.link)
            self.checkBox_2.setChecked(True)
            self.checkBox_2.setCheckable(True)
            self.checkBox_2.clicked.connect(self.link2)

        else:
            client = device()
            client.run()

            client.loop_start()
            print("\n" + "Connected to broker")
            time.sleep(1)
            print("Subscribing to topic", "microscope/light_sheet_microscope/UI/filter wheel")
            client.subscribe("microscope/light_sheet_microscope/UI/filter wheel")
            print("Publishing message to topic", "microscope/light_sheet_microscope/UI/filter wheel")
            client.publish("microscope/light_sheet_microscope/UI/filter wheel", json.dumps({"type": "device", "payload":{"name": "filter wheel", "cmd": "filter wheel turning on"}}, indent=2))
            time.sleep(1)
            client.loop_stop()
            print("Filter wheel turning on")
            
            self.pushButton2.clicked.connect(self.stop)
            self.pushButton.setChecked(True)
            self.checkBox.setChecked(True)
            self.checkBox.setCheckable(True)
            self.checkBox.clicked.connect(self.link)
            self.checkBox_2.setChecked(True)
            self.checkBox_2.setCheckable(True)
            self.checkBox_2.clicked.connect(self.link2)            

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox.setItemText(5, _translate("MainWindow", "6"))
        self.label_3.setText(_translate("MainWindow", "Left magnification changer"))
        self.label_2.setText(_translate("MainWindow", "Right filter wheel"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "22.2x"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "22.2x"))
        self.label_4.setText(_translate("MainWindow", "Right magnification changer"))
        self.label.setText(_translate("MainWindow", "Left filter wheel"))
        self.pushButton.setText(_translate("MainWindow", "ON"))
        self.pushButton2.setText(_translate("MainWindow", "OFF"))
        self.label_5.setText(_translate("MainWindow", "link"))
        self.label_6.setText(_translate("MainWindow", "link"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "6"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())