# MQTT Publish Demo
# Publish two messages, to two different topics

#import mqtt_publish_demo.py
from gpiozero import InputDevice
from time import time, sleep
import time
import board
import busio
import adafruit_msa301
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import subprocess
import re
# from mpu6050 import mpu6050
from subprocess import Popen, check_call
import os
from omxplayer.player import OMXPlayer as omxplayer

MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "RPi/Master"
status = False
curTime = "0"
pauseState = "t"
player = "" # omxplayer("/home/pi/ftp/files/video.mp4")

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    mqttInfo()
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    global status
    global curTime
    global pauseState
    global player
    msg = msg.payload.decode("UTF-8")
    print(msg)
    if (msg[16] == "n" and status == False):
        if (msg[5] == "p"):
            print("please work")
            rc = Popen("DISPLAY=:0 chromium 'file:///home/pi/ftp/files/image.jpg' --kiosk", shell = True)
        elif (msg[5] == "v"):
            player = omxplayer("/home/pi/ftp/files/video.mp4")
            # rc = Popen("DISPLAY=:0 chromium 'file:///home/pi/ftp/files/video.mp4' --kiosk", shell = True)
            player.play()
            sleep(0.3)
            player.pause()
        status = True
    elif (msg[16] == "n" and status == True):
        if (msg[34] == "p"):
            Popen("killall -KILL chromium", shell = True)
        elif (msg[34] == "v"):
            print("start")
            player.quit()
            # Popen("killall omxplayer", shell = True)
            print("end")
            
        if (msg[5] == "p"):
            rc = Popen("DISPLAY=:0 chromium 'file:///home/pi/ftp/files/image.jpg' --kiosk", shell = True)
        elif (msg[5] == "v"):

            #rc = Popen("DISPLAY=:0 chromium 'file:///home/pi/ftp/files/video.mp4' --kiosk", shell = True)
            player = omxplayer("/home/pi/ftp/files/video.mp4")
            player.play()
            sleep(0.3)
            player.pause()
    
    elif (msg[5] == "q"):
        # Popen("killall -KILL chromium", shell = True)
        # Popen("killall omxplayer", shell = True)
        
        if (msg[34] == "p"):
            Popen("killall -KILL chromium", shell = True)
        elif (msg[34] == "v"):
        #    pass
            player.quit()
        sys.exit()
    elif (msg[24] == "f" and msg[5] == "v" and msg[16] == "o" and status == True):
        print("here")
        curTime = str(player.position())
        pauseState = "t"
        player.pause()
    elif (pauseState == "t" and msg[24] == "p" and msg[5] == "v" and msg[16] == "o" and status == True):
        print("AYEEE")
        # curTime = msg.split("/")[4]
        # player = player.seek(float(curTime))
        player.play()
        pauseState = "f"
    elif (msg[16] == "a" and msg[5] == "v"):
        print("YAY")
        # Popen("killall omxplayer", shell = True)
        #if (player.can_quit() == True):
        #    player.quit()
        player = omxplayer("/home/pi/ftp/files/video.mp4")
        curTime = msg.split("/")[4]
        print(curTime)
        status = True
        player.set_position(float(curTime))
        # player.play()
        sleep(0.5)
        player.pause()
        pauseState = "t"
        # sleep(3)
    
    if (msg[5] == "v"):
        curTime = str(player.position())
    mqttInfo()
  
  
# Don't need the class, realized after I made it
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
# sensor = mpu6050(0x68)

p1 = Pi(0, False, False, 1)

def mqttInfo():
    #msgs = [{'topic':"RPi/1", 'payload':p1.mA}, ("RPi/1", p1.mB, 0, False), ("RPi/1", p1.IMU, 0, False)]
    #publish.multiple(msgs, hostname="test.mosquitto.org")
    # msa = sensor.get_accel_data()
    print(msa.acceleration)
    if msa.acceleration[1] < -7:
        p1.IMU = 2
    elif msa.acceleration[1] > 7:
        p1.IMU = 1
    elif msa.acceleration[0] < -7:
        p1.IMU = 4
    elif msa.acceleration[0] > 7:
        p1.IMU = 3
    p1.IMU = str(p1.IMU)
    p1.number = str(p1.number)
    p1.mA = str(mSensor1.is_active)
    p1.mB = str(mSensor2.is_active)
    
    print(p1.number + p1.mA[0] + p1.mB[0] + p1.IMU + "/" +
          re.match("([^\s]+)", str(subprocess.getstatusoutput("hostname -I")[1])).group(0))

    publish.single("RPi/" + p1.number, p1.number + p1.mA[0] + p1.mB[0] + p1.IMU + "/"
                   + re.match("([^\s]+)", str(subprocess.getstatusoutput("hostname -I")[1])).group(0)
                   + "/" + curTime + "/" + pauseState,
                   hostname = "broker.hivemq.com")


# while True:
    
    #print("%f %f %f" % msa.acceleration)
    #print(msa.acceleration, mSensor1)
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_forever()
