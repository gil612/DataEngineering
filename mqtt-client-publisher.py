# download mosquitto broker https://mosquitto.org/download/
# start mosquitto broker with default configuration
# https://www.ev3dev.org/docs/tutorials/sending-and-receiving-messages-with-mqtt/
# package paho-mqtt
import paho.mqtt.client as mqtt
import time
from datetime import datetime
import numpy as np
import math
import random
# This is the Publisher


def create_values_time(start):
    signals = []
    ts = []
    m = 0
    for x in range(start, start+1024):
        if x:
            m = x/1024
        else:
            m = x
        sinus_form = math.sin((775*2*math.pi)*m)
        raw_signal =  random.uniform(-20,20)+20470 
        signals.append(raw_signal*sinus_form)
        ts.append(datetime.now())
    
    return np.array(signals,dtype=np.int16), ts


client = mqtt.Client()
client.connect("localhost", 1883, 60)
i = 0


while i < 600:

    v,mt  = create_values_time(i*1024)

    t = str(datetime.now())
    
    b = bytearray()
    b.extend(t.encode('utf-8'))
    b.extend(v.tobytes())
  
    client.publish("sens1/binary", b)
    
    for n in range(0,len(v)):
       client.publish("sens1/test",f"{t},{v[n]},{mt[n]},{i}")
    time.sleep(1)  # sleep for 10 seconds before next call
    i += 1
client.disconnect()
