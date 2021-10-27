import paho.mqtt.client as mqtt
from datetime import datetime

client = mqtt.Client()
client.connect("localhost",1883,60)

t0 = str(datetime.now()).encode('utf-8')
for x in range(0,10000):
    client.publish('test/mps','a')
client.publish('test/mps',t0)


# Messages per second:  14615.289053879264