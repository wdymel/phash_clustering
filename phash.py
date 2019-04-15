import numpy as np
import cv2.cv2 as cv2

try:
    from cv2 import cv2
except ImportError:
    pass

xd = cv2.imread('xd.jpg', cv2.IMREAD_GRAYSCALE)
if xd is None:
    raise RuntimeError

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', xd)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("test")
