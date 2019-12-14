import paho.mqtt.client as mqtt
from mqtt2 import *
import os
import time
import json
import configparser

class embedded:
    def start():
        try:
            os.remove("list_of_device(s)_currently_active.txt")
            os.remove("laser.ini")
            print("Activating device(s)")
        except:
            print("Activating devices(s)")

        config = configparser.RawConfigParser()
        config.read("config.ini")
        devices = config.sections()

        global client
        client = embedded()
        client.run()

        client.loop_start()
        print("Connected to broker")
        time.sleep(1)
        print("Subscribing to topic", "microscope/light_sheet_microscope/UI")
        client.subscribe("microscope/light_sheet_microscope/UI")
        print("Publishing message to topic", "microscope/light_sheet_microscope/UI")
        client.publish("microscope/light_sheet_microscope/UI", json.dumps({"type": "system", "payload":{"name": devices, "cmd": "activating device(s)"}}, indent=2))
        time.sleep(1)
        return devices

    def import_devices(devices):
        for item in devices:
            device = (item + "Embedded")
            deviceImport = __import__(device)

        with open("list_of_device(s)_currently_active.txt", "a+") as myfile:
            for item in devices:
                myfile.write(item + "\n")

    devices = start()
    import_devices(devices)

    def readFile(fname):    
        print("List of device(s) currently active:")
        try:
            with open(fname, "r") as f:
                for item in f:
                    print(item.rstrip("\n"))
        except:
            print("No device(s) added yet")
    readFile("list_of_device(s)_currently_active.txt")

client.loop_forever()