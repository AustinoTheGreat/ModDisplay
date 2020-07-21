
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
from PIL import Image
import crop_flex
import ftptesting
import ftplib
import keyboard
import sys
import video_crop
from termios import tcflush, TCIFLUSH
import time, sys


MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
# MQTT_TOPICS = [("RPi/0", 0)]
MQTT_TOPICS = [("RPi/0", 0), ("RPi/1", 0)]
width = 0
height = 0
orientation = "n"
userMsg = "type=/status=/vid=/"


picPath = input("Enter your file's full directory path or enter d to use default: ")
if (picPath == "d"):
    picPath = "pic/large.jpg"
if (picPath[-3: ] == "jpg"):
    userMsg = "type=pic/status=new/vid=/"
elif (picPath[-3: ] == "mov"):
    userMsg = "type=vid/status=new/vid=play/"

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
    publish.single("RPi/Master", "type=pic/status=load", hostname = "test.mosquitto.org")
    client.subscribe(MQTT_TOPICS)

def fileTransfer(height, width, IMU, orientation, picPath):
    global userMsg
    if (userMsg[5] == "p"):
        crop_flex.main(height, width, IMU, orientation, picPath)
        for counter in range(0, len(MQTT_TOPICS)):
            if (pi[counter].ip != "0"):
                filename = ("display" + str(pi[counter].posX) + str(pi[counter].posY) + ".jpg")
                print(filename)
                print(pi[counter].ip)

                ftptesting.main("image.jpg", pi[counter].ip, "pi", "password", "export/" + filename)
    elif (userMsg[5] == "v"):
        video_crop.main(height, width, IMU, orientation, picPath)
        for counter in range(0, len(MQTT_TOPICS)):
            if (pi[counter].ip != "0"):
                filename = ("display" + str(pi[counter].posX) + str(pi[counter].posY) + ".mp4")
                print(filename)
                print(pi[counter].ip)

                ftptesting.main("video.mp4", pi[counter].ip, "pi", "password", "export/" + filename)






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
    global userMsg

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
                
                fileTransfer(height, width, pi[i].IMU, orientation, picPath)
                # crop_flex.main(height, width, pi[i].IMU, orientation, picPath)
                # for counter in range(0, len(MQTT_TOPICS)):
                #     if (pi[counter].ip != "0"):
                #         filename = ("display" + str(pi[counter].posX) + str(pi[counter].posY) + ".jpg")
                #         print(filename)
                #         print(pi[counter].ip)

                #         ftptesting.main("image.jpg", pi[counter].ip, "pi", "password", "export/" + filename)


            elif (numInUse != 0 and nextPos != "nn" and pi[i].inUse == False):
                pi[i].inUse = True
                numInUse = numInUse + 1
                pi[i].posX = int(nextPos[0])
                pi[i].posY = int(nextPos[1])
                
                userMsg = userMsg.replace("old", "new")

                fileTransfer(height, width, pi[i].IMU, orientation, picPath)
                # crop_flex.main(height, width, pi[i].IMU, orientation, picPath)
                # for counter in range(0, len(MQTT_TOPICS)):
                #     if (pi[counter].ip != "0"):
                #         filename = ("display" + str(pi[counter].posX) + str(pi[counter].posY) + ".jpg")
                #         print(filename)
                #         print(pi[counter].ip)

                #         ftptesting.main("image.jpg", pi[counter].ip, "pi", "password", "export/" + filename)
    

    tcflush(sys.stdin, TCIFLUSH)
    print("Press c to continue: ")
    if keyboard.read_key() == "n":
        picPath = input("Please enter your new file's path: ")
        if (picPath[-3: ] == "jpg"):
            userMsg = "type=pic/status=new/vid=/"
        elif (picPath[-3: ] == "mov"):
            userMsg = "type=vid/status=new/vid=play/"
        fileTransfer(height, width, pi[i].IMU, orientation, picPath)
    elif keyboard.read_key() == "q":
        userMsg = "type=qui/status=old/vid=play/"
        publish.single("RPi/Master", userMsg, hostname = "test.mosquitto.org")
        sys.exit()
    elif userMsg[5] == "v" and keyboard.read_key() == "p":
        userMsg = "type=vid/status=old/vid=play/"
    elif userMsg[5] == "v" and keyboard.read_key() == "f":
        userMsg = "type=vid/status=old/vid=free/"


    # try:
    #     if keyboard.is_pressed("n"):
    #         picPath = input("Please enter your new file's path: ")
    #         if (picPath[-3: ] == "jpg"):
    #             userMsg = "type=pic/status=new/vid=/"
    #         elif (picPath[-3: ] == "mov"):
    #             userMsg = "type=vid/status=new/vid=play/"
    #         fileTransfer(height, width, pi[i].IMU, orientation, picPath)
    #     elif keyboard.is_pressed("q"):
    #         sys. exit()
    #     elif keyboard.is_pressed("p") and userMsg[5] == "v":
    #         userMsg = "type=vid/status=old/vid=play/"
    #     elif keyboard.is_pressed("f") and userMsg[5] == "v":
    #         userMsg = "type=vid/status=old/vid=free/"
    # except:
    #     pass
        


    # try:
    #     if keyboard.is_pressed("q"):
    #         userMsg = "type=pic/status=unload"
    #     else:
    #         userMsg = "type=pic/status=load"
    # except:
    #     print("nothing")
    printPos()  
    print(userMsg)
    publish.single("RPi/Master", userMsg, hostname = "test.mosquitto.org")
    if userMsg[16] == "n":
        userMsg = userMsg.replace("new", "old")
    # print("end")


# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)

# https://github.com/eclipse/paho.mqtt.python
client.loop_forever()
