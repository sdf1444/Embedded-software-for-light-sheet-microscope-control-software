from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from stages2 import *
from mqtt import *
import json
import time
import sys

class SubWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(SubWindow, self).__init__(parent)
        self.setMinimumSize(QSize(379, 268))

        self.ui = Ui_Stage()
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
# class SubWindow(QWidget):
#     def __init__(self, parent = None):
#         super(SubWindow, self).__init__(parent)
#         self.setMinimumSize(QSize(300, 200))
#         label = QLabel("Stages",  self)
        
#         self.Button = QtWidgets.QPushButton("ON",self)        
#         self.Button.clicked.connect(self.on)        
#         self.Button.setGeometry(QtCore.QRect(10, 40, 81, 23))

#         self.Button2 = QtWidgets.QPushButton("OFF",self)  
#         self.Button2.clicked.connect(self.off)              
#         self.Button2.setGeometry(QtCore.QRect(10, 40, 81, 23))
#         self.Button2.move(120,40)

#         self.fileName_UI = "stages"

#     def on(self):
#         client = device()
#         client.run()

#         client.loop_start()
#         print("Connected to broker")
#         time.sleep(1)
#         print("Subscribing to topic", "microscope/light_sheet_microscope/UI")
#         client.subscribe("microscope/light_sheet_microscope/UI")        
#         print("Publishing message to topic", "microscope/light_sheet_microscope/UI")
#         client.publish("microscope/light_sheet_microscope/UI", json.dumps({"type": "device", "payload":{"name": self.fileName_UI, "cmd": "stages turning on"}}, indent=2))
#         time.sleep(1)
#         self.Button.setStyleSheet("background-color: green")

#         listofdevices = []
#         listofdevices.append(self.fileName_UI)
#         with open("list_of_devices_currently_active.txt", "a+") as myfile:
#             for item in listofdevices:
#                 myfile.write(item + "\n")
#         print("\n" + item + " added to device list" + "\n" + "\n" + "List of devices currently active:")

#         def readFile(fname):
#             try:
#                 with open(fname, "r") as f:
#                     for item in f:
#                         print(item)
#             except:
#                 print("No devices added yet")
#         readFile("list_of_devices_currently_active.txt")

#     def off(self):
#         client = device()
#         client.run()

#         client.loop_start()
#         print("Connected to broker")
#         time.sleep(1)
#         print("Subscribing to topic", "microscope/light_sheet_microscope/UI/state")        
#         client.subscribe("microscope/light_sheet_microscope/UI/state")
#         print("Publishing message to topic", "microscope/light_sheet_microscope/UI/state")
#         client.publish("Publishing message to topic", "microscope/light_sheet_microscope/UI/state", json.dumps({"type": "device", "payload":{"name": "stages", "state": "turning off"}}))
#         time.sleep(1)
#         print("Device turned off")
#         self.Button.setStyleSheet("background-color:")

#         with open("list_of_devices_currently_active.txt", "r") as f:
#             lines = f.readlines()

#         with open("list_of_devices_currently_active.txt", "w") as f:
#             for line in lines:
#                 if line.strip("\n") != "laser":
#                     f.write(line)
#         print("Laser removed from device list" + "\n\n" + "List of devices currently active")

#         def readFile(fname):
#             try:
#                 with open(fname, "r") as f:
#                     for item in f:
#                         print(item)
#             except:
#                 print("No devices added yet")
#         readFile("list_of_devices_currently_active.txt")

#     def closeEvent(self, event):
#         self.close()