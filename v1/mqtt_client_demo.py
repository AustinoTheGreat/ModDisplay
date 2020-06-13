# MQTT Client demo
# Continuously monitor two different MQTT topics for data,
# check if the received data matches two predefined 'commands'
# https://www.youtube.com/watch?v=Pb3FLznsdwI&t=449s
 
import paho.mqtt.client as mqtt
from PIL import Image
import crop

#Use this class to store multiple P5
class Pi:
    def __init__(self, number, mA, mB, IMU):
        self.number = number
        self.mA = mA
        self.mB = mB
        self.IMU = IMU
 
p1 = Pi(1, False, False, 1)
img = Image.open('old_campus.jpg')
global count
count = 0

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.

    client.subscribe("RPi/1")

 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

    msg = msg.payload.decode('UTF-8')
    #print(msg)
    #print(dMsg)
    # p1.mB = dMsg[1]
    # p1.IMU = dMsg[2]
    # crop.main(p1.mA, p1.mB)
    
    if (count % 3) == 0:
        if msg == "True":
            p1.mA = True
    elif (count % 3) == 1:
        if msg == "True":
            p1.mB = True
    elif (count % 3) == 2:
        p1.IMU = int(msg)
    count = count + 1
    print(p1.mA)
    print(p1.mB)
    print(p1.IMU)




     
    # print(msg.topic+" "+str(msg.payload))
    # print(str(msg.payload))
 
# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect("test.mosquitto.org", 1883, 60)

# https://github.com/eclipse/paho.mqtt.python
client.loop_forever()
