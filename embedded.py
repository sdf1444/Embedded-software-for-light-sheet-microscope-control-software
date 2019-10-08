import paho.mqtt.client as mqtt
from mqtt2 import *
import os
import time
import json

def start():
    try:
        os.remove("list_of_devices_currently_active.txt")
        os.remove("laserConfig.json")
        print("Awaiting device(s) to be activated")
    except:
        print("Awaiting device(s) to be activated")
start()
	
devices = list(map(str,input("Device(s) to be activated: ").split(",")))

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

def active_devices():
    for item in devices:
        device = (item + "Embedded")
        deviceImport = __import__(device)

    with open("list_of_device(s)_currently_active.txt", "a+") as myfile:
        for item in devices:
            myfile.write(item + "\n")

active_devices()

def readFile(fname):    
    print("List of device(s) currently active:")
    try:
        with open(fname, "r") as f:
            for item in f:
                print(item.rstrip("\n"))
    except:
        print("No device(s) added yet")
readFile("list_of_device(s)_currently_active.txt")

client = embedded()
client.run()

# client.loop_start()
print("Connected to broker")
time.sleep(1)
print("Subscribing to topic", "microscope/light_sheet_microscope/UI/laser")
client.subscribe("microscope/light_sheet_microscope/UI/laser")
client.loop_forever()