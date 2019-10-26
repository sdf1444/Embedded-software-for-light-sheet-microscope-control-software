import logging
import paho.mqtt.client as mqtt
import json

class device(mqtt.Client):
    def on_connect(self, mqtt, obj, flags, rc):
        pass

    def on_message(self, mqtt, userdata, message):
        m_decode = str(message.payload.decode("utf-8"))
        print("message recieved= " + m_decode)
        # print("File which you want to import(with .py extension)")
        print("message topic=", message.topic)
        print("message qos=", message.qos)
        print("message retain flag=", message.retain)
        m_in = json.loads(m_decode)

    def run(self):
        self.connect("broker.hivemq.com", 1883, 60)