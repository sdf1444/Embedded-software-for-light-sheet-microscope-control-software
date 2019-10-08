from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from laser2 import *
from mqtt import *
import json
import time
import sys

class SubWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(SubWindow, self).__init__(parent)
        self.setMinimumSize(QSize(379, 268))

        self.ui = Ui_Laser()
        self.ui.setupUi(self)

def main():
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QtWidgets.QApplication(sys.argv)
    application = SubWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
        
    #     self.Button = QtWidgets.QPushButton("Turn off", self)
    #     self.Button.setStyleSheet("background-color:")        
    #     self.Button.clicked.connect(self.off)        
    #     self.Button.setGeometry(QtCore.QRect(10, 40, 81, 23))

    #     self.button1 = QPushButton("ON", self)
    #     self.button1.setCheckable(True)
    #     self.button1.setStyleSheet("QPushButton {background-color:;} QPushButton:checked{background-color: red;} QPushButton:pressed {background-color:;}")
    #     self.button1.move(10, 100)
    #     self.button1.resize(100, 32)

    #     self.button2 = QPushButton("ON", self)
    #     self.button2.setCheckable(True)
    #     self.button2.setStyleSheet("QPushButton {background-color:;} QPushButton:checked{background-color: green;} QPushButton:pressed {background-color:;}")
    #     self.button2.move(110, 100)
    #     self.button2.resize(100, 32)

    #     self.button3 = QPushButton("ON", self)
    #     self.button3.setCheckable(True)
    #     self.button3.setStyleSheet("QPushButton {background-color:;} QPushButton:checked{background-color: blue;} QPushButton:pressed {background-color:;}")
    #     self.button3.move(210, 100)
    #     self.button3.resize(100, 32)

    #     self.button4 = QPushButton("ON", self)
    #     self.button4.setCheckable(True)
    #     self.button4.setStyleSheet("QPushButton {background-color:;} QPushButton:checked{background-color: orange;} QPushButton:pressed {background-color:;}")
    #     self.button4.move(310, 100)
    #     self.button4.resize(100, 32)

    #     self.button5 = QPushButton("ON", self)
    #     self.button5.setCheckable(True)
    #     self.button5.setStyleSheet("QPushButton {background-color:;} QPushButton:checked{background-color: brown;} QPushButton:pressed {background-color:;}")
    #     self.button5.move(410, 100)
    #     self.button5.resize(100, 32)

    #     self.button6 = QPushButton("ON", self)
    #     self.button6.setCheckable(True)
    #     self.button6.setStyleSheet("QPushButton {background-color:;} QPushButton:checked{background-color: yellow;} QPushButton:pressed {background-color:;}")
    #     self.button6.move(510, 100)
    #     self.button6.resize(100, 32)

    #     self.button7 = QPushButton("ON", self)
    #     self.button7.setCheckable(True)
    #     self.button7.setStyleSheet("QPushButton {background-color:;} QPushButton:checked{background-color: purple;} QPushButton:pressed {background-color:;}")
    #     self.button7.move(610, 100)
    #     self.button7.resize(100, 32)
    #     self.fileName_UI = "laser"

    # def on(self):
    #     client = device()
    #     client.run()

    #     client.loop_start()
    #     print("Connected to broker")
    #     time.sleep(1)
    #     print("Subscribing to topic", "microscope/light_sheet_microscope/UI")
    #     client.subscribe("microscope/light_sheet_microscope/UI")        
    #     print("Publishing message to topic", "microscope/light_sheet_microscope/UI")
    #     client.publish("microscope/light_sheet_microscope/UI", json.dumps({"type": "device", "payload":{"name": self.fileName_UI, "cmd": "laser turning on"}}, indent=2))
    #     time.sleep(1)
    #     client.loop_stop()

    #     listofdevices = []
    #     listofdevices.append(self.fileName_UI)
    #     with open("list_of_devices_currently_active.txt", "a+") as myfile:
    #         for item in listofdevices:
    #             myfile.write(item + "\n")
    #     print("\n" + item + " added to device list" + "\n" + "\n" + "List of devices currently active:")

    #     def readFile(fname):
    #         try:
    #             with open(fname, "r") as f:
    #                 for item in f:
    #                     print(item)
    #         except:
    #             print("No devices added yet")
    #     readFile("list_of_devices_currently_active.txt")
    #     self.Button.setStyleSheet("background-color:")

    # def off(self):
    #     client = device()
    #     client.run()

    #     client.loop_start()
    #     print("Connected to broker")
    #     time.sleep(1)
    #     print("Subscribing to topic", "microscope/light_sheet_microscope/UI/states")
    #     client.subscribe("microscope/light_sheet_microscope/UI/states")     
    #     print("Publishing message to topic", "microscope/light_sheet_microscope/UI/states")
    #     client.publish("microscope/light_sheet_microscope/UI/states", json.dumps({"type": "device", "payload":{"name": self.fileName_UI, "cmd": "laser turning off"}}, indent=2))
    #     time.sleep(1)
    #     client.loop_stop()
    #     print("Device turned off")
    #     self.Button.setText("Turn on")
    #     self.Button.setStyleSheet("background-color: green")

    #     with open("list_of_devices_currently_active.txt", "r") as f:
    #         lines = f.readlines()

    #     with open("list_of_devices_currently_active.txt", "w") as f:
    #         for line in lines:
    #             if line.strip("\n") != "laser":
    #                 f.write(line)
    #     print("Laser removed from device list" + "\n\n" + "List of devices currently active")

    #     def readFile(fname):
    #         try:
    #             with open(fname, "r") as f:
    #                 for item in f:
    #                     print(item)
    #         except:
    #             print("No devices added yet")
    #     readFile("list_of_devices_currently_active.txt")

    # def closeEvent(self, event):
    #     self.close()