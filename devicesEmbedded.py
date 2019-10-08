import random
import asyncio
from actorio import Actor, Message, DataMessage, ask, EndMainLoop, Reference
from mqtt import *

print("Subscribing to topic", "microscope/light_sheet_microscope/UI/list_of_devices")
client.subscribe("microscope/light_sheet_microscope/UI/list_of_devices")
client.loop_stop()  # stop the loop

def readFile(fname):
	try:
		with open(fname, "r") as f:
			for item in f:
				print("List of devices added: " + item)
				devicesEmbedded = (item + ".py") 
				de = __import__(devicesEmbedded)
	except:
		print("No devices added yet")
readFile("list_of_devices.txt")