import numpy as np
import cv2
my_img = np.zeros((400, 400, 3), dtype="uint8")
# creating circle
cv2.circle(my_img, (200, 200), 80, (0, 20, 200), 10)
cv2.imshow('Window', my_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
