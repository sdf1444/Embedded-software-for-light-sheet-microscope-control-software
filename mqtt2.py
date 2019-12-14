import logging
import paho.mqtt.client as mqtt
import json
from pynq.overlays.base import BaseOverlay
from pynq.lib import LED, Switch, Button
from pynq.lib import Pmod_ADC, Pmod_DAC
import time
import asyncio

class embedded(mqtt.Client):
    def on_connect(self, mqtt, obj, flags, rc):
        pass

    def on_message(self, mqtt, userdata, message):
        asyncio.set_event_loop(asyncio.new_event_loop())
        m_decode = str(message.payload.decode("utf-8"))
        print("\n" + "message recieved= " + m_decode)
        print("message topic=", message.topic)
        print("message qos=", message.qos)
        print("message retain flag=", message.retain)
        m_in = json.loads(m_decode)
        if message.topic == "microscope/light_sheet_microscope/UI/laser/445nm":
        	print("LED 0 flashing")
        	base = BaseOverlay("base.bit")
        	led0 = base.leds[0]
        	for i in range(20):
        		led0.toggle()
        		time.sleep(.1)
        
        if message.topic == "microscope/light_sheet_microscope/UI/laser/488nm":
        	print("LED 0 flashing")
        	base = BaseOverlay("base.bit")
        	led0 = base.leds[0]
        	for i in range(20):
        		led0.toggle()
        		time.sleep(.1)

        if message.topic == "microscope/light_sheet_microscope/UI/laser/515nm":
        	print("LED 0 flashing")
        	base = BaseOverlay("base.bit")
        	led0 = base.leds[0]
        	for i in range(20):
        		led0.toggle()
        		time.sleep(.1)

        if message.topic == "microscope/light_sheet_microscope/UI/laser/561nm":
            base = BaseOverlay("base.bit")
            led0 = base.leds[0]
            for i in range(20):
                led0.toggle()
                time.sleep(.1)

        if message.topic == "microscope/light_sheet_microscope/UI/laser/594nm":
            print("LED 0 flashing")
            base = BaseOverlay("base.bit")
            led0 = base.leds[0]
            for i in range(20):
                led0.toggle()
                time.sleep(.1)

        if message.topic == "microscope/light_sheet_microscope/UI/laser/638nm":
            print("LED 0 flashing")
            base = BaseOverlay("base.bit")
            led0 = base.leds[0]
            for i in range(20):
                led0.toggle()
                time.sleep(.1)

        if message.topic == "microscope/light_sheet_microscope/UI/laser" and m_in["payload"]["cmd"] == "device turning off":
        	print("Laser turning off")
        	client.loop_stop()

        if message.topic == "microscope/light_sheet_microscope/UI/laser/445nm" and m_in["payload"]["cmd"] == "set intensity of laser":
            dac = Pmod_DAC(base.PMODA)
            dac.write(0.6)

    def run(self):
        self.connect("broker.hivemq.com", 1883, 60)