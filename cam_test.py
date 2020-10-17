import cv2
import numpy as np

cap = cv2.VideoCapture(0)



while(True):
    ret, frame = cap.read()
    if ret:
        cv2.imshow(frame)
    else:
        break

#test
#

print('fix by Jason')
print('hello world GG')
