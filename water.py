# 수분감지센서

import time
from pyfirmata import Arduino, util
import paho.mqtt.client as mqtt

board = Arduino('/dev/ttyACM0')

mqttc = mqtt.Client()
brocker_address = "192.168.0.228"
mqttc.connect(brocker_address)

def message(client, userdata, msg): #sub
    print("message received")
    print("message topic= ", msg)
    print("message retain flag= ",message.retain)
mqttc.loop_start()

it = util.Iterator(board)
it.start()
board.analog[1].enable_reporting()

while True:
    try:
        time.sleep(1)
        sensor_value = board.analog[1].read()
        sensor_r=round(sensor_value,1)

        if sensor_value is not None:
            print("water value : ", sensor_r*1000)
    
        mqttc.publish('yj',sensor_r,2)
    except:
        break
mqttc.loop_stop()
