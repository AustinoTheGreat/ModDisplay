# MQTT Publish Demo
# Publish two messages, to two different topics

#import mqtt_publish_demo.py
from gpiozero import InputDevice
from time import sleep
import time
import board
import busio
import adafruit_msa301


class Pi:
    def __init__(self, number, mA, mB, IMU):
        self.number = number
        self.mA = mA
        self.mB = mB
        self.IMU = IMU
        
mSensor1 = InputDevice(17)
mSensor2 = InputDevice(18)
i2c = busio.I2C(board.SCL, board.SDA)
msa = adafruit_msa301.MSA301(i2c)


while True:
    print("%f %f %f" % msa.acceleration)
    time.sleep(1)
print("Done")
