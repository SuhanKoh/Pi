from __future__ import print_function
from pivideostream import PiVideoStream
from imutils.video import FPS
from picamera.array import PiRGBArray
from picamera import PiCamera
import imutils
import time
import cv2

piVidSteam = PiVideoStream()
vs = piVidSteam.start()
face_cascade = cv2.CascadeClassifier('/home/pi/Desktop/faces.xml')
time.sleep(2.0)

while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    #Convert to grayscale
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #Look for faces in the image using the loaded cascade file
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    print("Found "+str(len(faces))+" face(s)")

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