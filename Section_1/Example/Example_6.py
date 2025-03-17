import numpy as np
import cv2
my_img = np.zeros((400, 400, 3), dtype="uint8")
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(my_img, [pts], True, (0, 255, 255))
cv2.imshow('Window', my_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
