# MQTT Client demo
# Continuously monitor two different MQTT topics for data,
# check if the received data matches two predefined 'commands'
# https://www.youtube.com/watch?v=Pb3FLznsdwI&t=449s
 
import paho.mqtt.client as mqtt
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.

    client.subscribe("RPi/1-mA")
    
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    m1A = msg.payload
    print(m1A)
     
    # print(msg.topic+" "+str(msg.payload))
    # print(str(msg.payload))
 
# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect("test.mosquitto.org", 1883, 60)

# https://github.com/eclipse/paho.mqtt.python
client.loop_forever()
