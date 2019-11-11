import paho.mqtt.client as mqtt
import os
import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, uic, QtCore
from mqtt import *
import json
import time

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
	PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
	PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self)
        super(MainWindow, self).__init__(parent)
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        self.setMinimumSize(QSize(800, 600))
        self.setWindowTitle("PyQt button example - pythonprogramminglanguage.com")

        client = device()
        client.run()

        client.loop_start()
        print("Connected to broker")
        time.sleep(1)
        print("Subscribing to topic", "microscope/light_sheet_microscope/UI/devices")
        client.subscribe("microscope/light_sheet_microscope/UI/devices")
        print("Publishing message to topic", "microscope/light_sheet_microscope/UI/devices")
        client.publish("microscope/light_sheet_microscope/UI/devices", json.dumps({"type": "system", "payload":{"cmd": "get all devices"}}, indent=2))
        time.sleep(1)                        

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Devices')

        def readFile(fname):
            try:
                with open(fname, "r") as f:
                    for item in f:
                        deviceImport = fileMenu.addAction(item)
                        deviceImport.triggered.connect(self.importbutton)       
            except:
                print("No devices active")
        readFile("list_of_device(s)_currently_active.txt") 
    
    def importbutton(self):
        if not os.path.exists("laser.ini"):
            client = device()
            client.run()

            client.loop_start()
            print("\n" + "Connected to broker")
            time.sleep(1)
            print("Subscribing to topic", "microscope/light_sheet_microscope/UI/add device")
            client.subscribe("microscope/light_sheet_microscope/UI/add device")
            print("Publishing message to topic", "microscope/light_sheet_microscope/UI/add device")
            client.publish("microscope/light_sheet_microscope/UI/add device", json.dumps({"type": "system", "payload":{"cmd": "init device panel"}}, indent=2))
            time.sleep(1)
            client.loop_stop()        
            sender = self.sender()        
            self.fileName_UI = sender.text()
            self.loadGUI()
            print("Device panel initialised" + "\n")
        else:
            if os.path.exists("laser.ini"):
                client = device()
                client.run()

                client.loop_start()
                print("\n" + "Connected to broker")
                time.sleep(1)
                print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser")
                client.subscribe("microscope/light_sheet_microscope/UI/laser")
                print("Publishing message to topic", "microscope/light_sheet_microscope/UI/laser")
                client.publish("microscope/light_sheet_microscope/UI/laser", json.dumps({"type": "device", "payload":{"name": "laser", "cmd": "set config"}}, indent=2))
                time.sleep(1)
                client.loop_stop()
                sender = self.sender()        
                self.fileName_UI = sender.text()
                self.loadGUI()
                print("Laser config set" + "\n")

    def loadGUI(self):
        module = __import__(self.fileName_UI.rstrip("\n"))
        my_class = getattr(module, "SubWindow")
        
        sub = QMdiSubWindow()
        
        sub.setWidget(my_class())
        sub.setWindowTitle(self.fileName_UI)
        self.mdi.addSubWindow(sub)
        sub.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    # publishedMessage = mainWin.getGUIFilename()
    sys.exit(app.exec_())