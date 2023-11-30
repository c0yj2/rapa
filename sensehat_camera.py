# 온습도측정 + 카메라

import time
from sense_hat import SenseHat
import cv2

sense = SenseHat()
cap = cv2.VideoCapture(0) #0 or -1
while(cap.isOpened()):
    try:
        ret, img = cap.read()
        if ret:
            cv2.imshow('camera-0', img)
        else:
            print('no camera!')
        if cv2.waitKey(1) & 0xFF == 27: #esc
            break
        time.sleep(1)
        humidity = sense.get_humidity()
        #print("Humidity: %s %%rH" % humidity)
        temp = sense.get_temperature()
        print("Temperature: %s C" % temp)
        if temp>37: //온도가 37도 이상이면
            sense.clear(255,102,0) //LED on(주황색)
        else: 
            sense.clear() //LED off
    except:
        break
cap.release()
cv2.destroyAllWindows()
