import cv2
import numpy as np

cap = cv2.VideoCapture(0)

lower_blue = np.array([100,150,0])
upper_blue = np.array([140,255,255])

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()