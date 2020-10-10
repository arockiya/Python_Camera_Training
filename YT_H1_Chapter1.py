import cv2
print("Pakage Imported")

img = cv2.imread('Resources/Lenna.png')

cv2.imshow("Output",img)

# Waitkey 0 - infinite time
# waitkey 1- 1 millisecond, 1000 - 1 second
cv2.waitKey(0)