import paho.mqtt.client as mqtt
from datetime import datetime

import pyodbc
# SQL server connection
server='DESKTOP-7GQKTPR' 
database='mqtt' 
username='DESKTOP-7GQKTPR\gilbaram' 
cnxn= pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';Trusted_Connection=yes;')
cursor=cnxn.cursor()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("sens1/binary")
    client.subscribe("sens1/test")
    


def on_message(client, userdata, msg):
    m = msg.payload
    #The default size of a timestamp is 26
    ts = m[:26]
    created_at = datetime.fromisoformat(ts.decode())
    received_at = datetime.now()
    data = m[26:]
    cursor.execute("insert into T1 (created_at, received_at, sensor_data) values (?,?,?)",(created_at, received_at, data))
    cnxn.commit()


def on_message_datapackage(client, userdata, msg):
    print(msg.payload)
    received_at = datetime.now()
    m = msg.payload.decode().split(',')
    created_at = datetime.fromisoformat(m[2])
    started_at = datetime.fromisoformat(m[0])
    package_id = int(m[3])
    value = int(m[1])
    cursor.execute("insert into T2 (package_id, started_at, created_at, received_at, sensor_data) values (?,?,?,?,?)",(package_id, started_at, created_at, received_at, value))
    cnxn.commit()


client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.on_connect = on_connect
client.on_message = on_message
client.message_callback_add("sens1/test", on_message_datapackage)
client.loop_forever()
