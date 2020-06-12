# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish
from gpiozero import InputDevice
from time import sleep
mSensor1 = InputDevice(17)


if mSensor1.is_active() == True:
    publish.single("RPi/1-mA", 1, hostname="test.mosquitto.org")
elif mSensor1.is_active() == False:
    publish.single("RPi/1-mA", 0, hostname="test.mosquitto.org")
print("Done")