from __future__ import print_function
from pivideostream import PiVideoStream
from picamera.array import PiRGBArray
from picamera import PiCamera
import Weathered.weathered
import imutils
import time
import cv2
import threading

WEATHER_COOLDOWN = 60 # 60 sec
piVidSteam = PiVideoStream()
vs = piVidSteam.start()
face_cascade = cv2.CascadeClassifier('/home/pi/Desktop/faces.xml')
time.sleep(2.0)
last_forecast_request_time = 0

while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    #Convert to grayscale
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #Look for faces in the image using the loaded cascade file
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    if len(faces) > 0:
        temp = time.time()
        if (temp - last_forecast_request_time >= WEATHER_COOLDOWN):
            last_forecast_request_time = temp
            threading.Thread(target=Weathered.weathered.get_weather).start()
            
    #Draw a rectangle around every found face
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)

    #Show the frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()
vs.stop()
