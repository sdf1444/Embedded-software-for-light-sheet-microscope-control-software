from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, uic
from mqtt import *
from cameras2 import *
import json
import time

class SubWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(SubWindow, self).__init__(parent)
        self.setMinimumSize(QSize(379, 268))

        self.ui = Ui_Cameras()
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
        # self.Button.setStyleSheet("background-color: green")

        # listofdevices = []
        # listofdevices.append(self.fileName_UI)
        # with open("list_of_devices_currently_active.txt", "a+") as myfile:
        #     for item in listofdevices:
        #         myfile.write(item + "\n")
        # print("\n" + item + " added to device list" + "\n" + "\n" + "List of devices currently active:")

        # def readFile(fname):
        #     try:
        #         with open(fname, "r") as f:
        #             for item in f:
        #                 print(item)
        #     except:
        #         print("No devices added yet")
        # readFile("list_of_devices_currently_active.txt")

    # def off(self):
    #     client = device()
    #     client.run()

    #     client.loop_start()
    #     print("Connected to broker")
    #     time.sleep(1)
    #     print("Subscribing to topic", "microscope/light_sheet_microscope/UI/states")
    #     client.subscribe("microscope/light_sheet_microscope/UI/states")     
    #     print("Publishing message to topic", "microscope/light_sheet_microscope/UI/states")
    #     client.publish("microscope/light_sheet_microscope/UI/states", json.dumps({"type": "device", "payload":{"name": self.fileName_UI, "cmd": "cameras turning off"}}, indent=2))
    #     time.sleep(1)
    #     client.loop_stop()
    #     print("Device turned off")
    #     self.Button.setStyleSheet("background-color:")

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