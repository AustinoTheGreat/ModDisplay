# https://www.youtube.com/watch?v=Pb3FLznsdwI&t=449s

import paho.mqtt.client as mqtt
from PIL import Image
import crop_flex
import ftptesting
import ftplib


MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPICS = [("RPi/0", 0), ("RPi/1", 0)]
width = 0
height = 0
orientation = "n"

picPath = input("Enter your picture's full directory path or enter d to use default: ")
if (picPath == "d"):
    picPath = "pic/original-image.jpg"

#Use this class to store multiple Pi
class Pi:
    def __init__(self, number, mA, mB, IMU, ip, posX, posY, inUse):
        self.number = number
        self.mA = mA
        self.mB = mB
        self.IMU = IMU
        self.ip = ip
        self.posX = posX
        self.posY = posY
        self.inUse = inUse
pi = []
nextPos = "nn"
numInUse = 0

for i in range(0, len(MQTT_TOPICS)):
    print(i)
    pi.append(Pi(i, "F", "F", "1", "0", 0, 0, False))

# p1 = Pi(1, "F", "F", "1")
# p2 = Pi(2, "F", "F", "1")

def printPos():
    for x in pi:
        print("Pi Number: " + str(x.number) + " Pos: (X Y) " + str(x.posX) + " " + str(x.posY) + " State: " + str(x.inUse))

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_TOPICS)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global pi
    global nextPos
    global numInUse
    global width
    global height
    global orientation
    global height
    global width
    global picPath

    msg = msg.payload.decode('UTF-8')
    print(msg)

    for i in range(0, len(MQTT_TOPICS)):
        if(msg[0] == str(i)):
            prevA = pi[i].mA
            prevB = pi[i].mB

            pi[i].mA = msg[1]
            pi[i].mB = msg[2]
            pi[i].IMU = msg[3]
            pi[i].ip = msg.partition("/")[2]
            print(pi[i].ip)

            if (prevA != pi[i].mA):
                print("A change: " + str(i))
                if (pi[i].IMU == "1" or pi[i].IMU == "2"):
                    nextPos = str(pi[i].posX + 1) + str(pi[i].posY)
                    if (pi[i].posX + 1 >= width):
                        width = width + 1
                elif (pi[i].IMU == "3" or pi[i].IMU == "4"):
                    nextPos = str(pi[i].posX) + str(pi[i].posY + 1)
                    if (pi[i].posY + 1 >= height):
                        height = height + 1
            elif (prevB != pi[i].mB):
                print("B change: " + str(i))
                if (pi[i].IMU == "1" or pi[i].IMU == "2"):
                    nextPos = str(pi[i].posX) + str(pi[i].posY + 1)
                    if (pi[i].posY + 1 >= height):
                        height = height + 1
                elif (pi[i].IMU == "3" or pi[i].IMU == "4"):
                    nextPos = str(pi[i].posX + 1) + str(pi[i].posY)
                    if (pi[i].posX + 1 >= width):
                        width = width + 1

            if (numInUse == 0 and nextPos == "nn"):
                pi[i].inUse = True
                numInUse = numInUse + 1
                height = 1
                width = 1
                if (pi[i].IMU == "1" or pi[i].IMU == "2"):
                    orientation = "h"
                elif (pi[i].IMU == "3" or pi[i].IMU == "4"):
                    orientation = "v"
                crop_flex.main(height, width, pi[i].IMU, orientation, picPath)

                for counter in range(0, len(MQTT_TOPICS)):

                        for h in range(0, height):

                            for w in range(0, width):

                                if (str(pi[counter].posX) + str(pi[counter].posY) == str(h) + str(w)):

                                    filename = ("display" + str(pi[counter].posX) + str(pi[counter].posY) + ".jpg")

                                    ftptesting.main(filename, pi[counter].ip, "pi", "raspberry", "export/" + filename)


            elif (numInUse != 0 and nextPos != "nn" and pi[i].inUse == False):
                pi[i].inUse = True
                numInUse = numInUse + 1
                pi[i].posX = int(nextPos[0])
                pi[i].posY = int(nextPos[1])
                crop_flex.main(height, width, pi[i].IMU, orientation, picPath)

                for counter in range(0, len(MQTT_TOPICS)):

                        for h in range(0, height):

                            for w in range(0, width):

                                if (str(pi[counter].posX) + str(pi[counter].posY) == str(h) + str(w)):

                                    filename = ("display" + str(pi[counter].posX) + str(pi[counter].posY) + ".jpg")

                                    ftptesting.main(filename, pi[counter].ip, "pi", "raspberry", "export/" + filename)




    printPos()
    # print("end")


# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)

# https://github.com/eclipse/paho.mqtt.python
client.loop_forever()