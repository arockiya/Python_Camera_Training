import cv2
import numpy as np

cap = cv2.VideoCapture(0)

lower_blue = np.array([100,150,0])
upper_blue = np.array([140,255,255])

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    cv2.imshow('frame',hsv)
    cv2.imshow('mask',mask)
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()