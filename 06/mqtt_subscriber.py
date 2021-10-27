import paho.mqtt.client as mqtt
from datetime import datetime

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("test/mps")


msg_counter = 0

def on_message(client, userdata, msg):
    global msg_counter
    if msg_counter < 10000:
        msg_counter +=1
    else:
        t1 = datetime.now() 
        t = msg.payload.decode()
        t0 = datetime.fromisoformat(t)
        print('Messages per second: ', 10000/(t1-t0).total_seconds())
        client.disconnect()

client = mqtt.Client()
client.connect("localhost", 1883, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
