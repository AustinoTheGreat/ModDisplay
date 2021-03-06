# MQTT Publish Demo
# Publish two messages, to two different topics

#import mqtt_publish_demo.py
from gpiozero import InputDevice
from time import sleep
import time
import board
import busio
import adafruit_msa301
import paho.mqtt.publish as publish
import subprocess
import re
from mpu6050 import mpu6050

# Don't need the class, realized after I made it
class Pi:
    def __init__(self, number, mA, mB, IMU):
        self.number = number
        self.mA = mA
        self.mB = mB
        self.IMU = IMU
        
mSensor1 = InputDevice(17)
mSensor2 = InputDevice(18)

# i2c = busio.I2C(board.SCL, board.SDA)
# msa = adafruit_msa301.MSA301(i2c)
sensor = mpu6050(0x68)

p1 = Pi(1, False, False, 1)

def mqttInfo():
    #msgs = [{'topic':"RPi/1", 'payload':p1.mA}, ("RPi/1", p1.mB, 0, False), ("RPi/1", p1.IMU, 0, False)]
    #publish.multiple(msgs, hostname="test.mosquitto.org")
    publish.single("RPi/" + p1.number, p1.number + p1.mA[0] + p1.mB[0] + p1.IMU + "/"
                   + re.match("([^\s]+)", str(subprocess.getstatusoutput("hostname -I")[1])).group(0),
                   hostname = "test.mosquitto.org")



while True:
    #print("%f %f %f" % msa.acceleration)
    #print(msa.acceleration, mSensor1)
    msa = sensor.get_accel_data()
    print(msa)
    if msa["x"] < -7:
        p1.IMU = 2
    elif msa["x"] > 7:
        p1.IMU = 1
    elif msa["y"] < -7:
        p1.IMU = 4
    elif msa["y"] > 7:
        p1.IMU = 3
    p1.IMU = str(p1.IMU)
    p1.number = str(p1.number)
    p1.mA = str(mSensor1.is_active)
    p1.mB = str(mSensor2.is_active)
    
    print(p1.number + p1.mA[0] + p1.mB[0] + p1.IMU + "/" +
          re.match("([^\s]+)", str(subprocess.getstatusoutput("hostname -I")[1])).group(0))
    mqttInfo()
    
    time.sleep(10)
    
print("Done")
