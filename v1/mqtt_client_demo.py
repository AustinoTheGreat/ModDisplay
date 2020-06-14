# MQTT Client demo
# Continuously monitor two different MQTT topics for data,
# check if the received data matches two predefined 'commands'
# https://www.youtube.com/watch?v=Pb3FLznsdwI&t=449s
 
import paho.mqtt.client as mqtt
from PIL import Image
import crop
#import rotate

#Use this class to store multiple P5
class Pi:
    def __init__(self, number, mA, mB, IMU):
        self.number = number
        self.mA = mA
        self.mB = mB
        self.IMU = IMU
 
p1 = Pi(1, False, False, 1)
path = "old_campus.jpg"
img = Image.open(path)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.

    client.subscribe("RPi/1")

 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

    msg = msg.payload.decode('UTF-8')
    print(msg)
    p1.mA = msg[0]
    p1.mB = msg[1]
    p1.IMU = msg[2]
    if (p1.mA == "T"):
        p1.mA = 1
    else:
        p1.mA = 0
    if (p1.mB == "T"):
        p1.mB = 1
    else:
        p1.mB = 0
    crop.main(img, p1.mA, p1.mB, p1.IMU)

    #rotate.main(img, p1.IMU)





     
    # print(msg.topic+" "+str(msg.payload))
    # print(str(msg.payload))
 
# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect("test.mosquitto.org", 1883, 60)

# https://github.com/eclipse/paho.mqtt.python
client.loop_forever()
