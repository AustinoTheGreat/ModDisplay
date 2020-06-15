# https://www.youtube.com/watch?v=Pb3FLznsdwI&t=449s
 
import paho.mqtt.client as mqtt
from PIL import Image
import border_adj

MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPICS = [("RPi/0", 0)]
#MQTT_TOPICS = [("RPi/0", 0), ("RPi/1", 0)]

picPath = input("Enter your picture's full directory path or enter d to use default: ")
if (picPath == "d"):
    picPath = "pic/original-image.jpg"

#Use this class to store multiple Pi
class Pi:
    def __init__(self, number, mA, mB, IMU):
        self.number = number
        self.mA = mA
        self.mB = mB
        self.IMU = IMU
pi = []
for i in range(0, len(MQTT_TOPICS)):
    print(i)
    pi.append(Pi(i, "F", "F", "1"))
 
# p1 = Pi(1, "F", "F", "1")
# p2 = Pi(2, "F", "F", "1")

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_TOPICS)

 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

    msg = msg.payload.decode('UTF-8')
    print(msg)

    for i in range(0, len(MQTT_TOPICS)):
        if(msg[0] == str(i)):
            pi[i].mA = msg[1]
            pi[i].mB = msg[2]
            pi[i].IMU = msg[3]
            if (pi[i].mA == "T"):
                pi[i].mA = 1
            else:
                pi[i].mA = 0
            if (pi[i].mB == "T"):
                pi[i].mB = 1
            else:
                pi[i].mB = 0
    for i in range(0, len(MQTT_TOPICS)):
        border_adj.main(pi[i].number, pi[i].mA, pi[i].mB, pi[i].IMU, picPath)

 
# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# https://github.com/eclipse/paho.mqtt.python
client.loop_forever()
