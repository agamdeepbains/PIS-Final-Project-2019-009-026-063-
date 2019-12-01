import cv2
import numpy as np
import serial
import time

ArduinoSerial = serial.Serial('COM7',9600)

cap = cv2.VideoCapture(1)
fps = int(cap.get(5))
ret, frame1 = cap.read()
ret, frame2 = cap.read()
ret, initial = cap.read()
print(frame1.shape)
i=0
ctrl=False
while cap.isOpened():
    objs = cv2.absdiff(frame1, initial)
    objgray = cv2.cvtColor(objs, cv2.COLOR_BGR2GRAY)
    objblur = cv2.GaussianBlur(objgray, (5,5), 5)
    _, objthresh = cv2.threshold(objblur, 30, 255, cv2.THRESH_BINARY)
    objeroded =cv2.erode(objthresh, None, iterations=15)
    objdilated = cv2.dilate(objeroded, None, iterations=5)
    objcontours, _ = cv2.findContours(objdilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    t=0
    for contour in objcontours:
        if cv2.contourArea(contour) > 200:
            t+=1
    cv2.putText(objs, str(t).format('Left'), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
    cv2.imshow("Image", frame1)
    cv2.imshow("Objects", objs)
    cv2.imshow("ObjGray", objgray)
    cv2.imshow("ObjThresh", objthresh)
    cv2.imshow("ObjEroded", objeroded)
    cv2.imshow("ObjDilated", objdilated)
    print(t)
    frame1 = frame2
    ret, frame2 = cap.read()
    if cv2.waitKey(40) == 27:
        break
    if t==0:
        ArduinoSerial.write(b'a')
    elif t==1:
        ArduinoSerial.write(b'b')
    elif t==2:
        ArduinoSerial.write(b'c')
    elif t==3:
        ArduinoSerial.write(b'd')
    elif t==4:
        ArduinoSerial.write(b'e')
    elif t==5:
        ArduinoSerial.write(b'f')
    elif t==6:
        ArduinoSerial.write(b'g')
    elif t==7:
        ArduinoSerial.write(b'h')
    elif t==8:
        ArduinoSerial.write(b'i')
    elif t==9:
        ArduinoSerial.write(b'j')
    elif t==10:
        ArduinoSerial.write(b'k')

cv2.destroyAllWindows()
cap.release()