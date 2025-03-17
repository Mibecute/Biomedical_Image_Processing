import numpy as np
import cv2
my_img = np.zeros((350, 350, 3), dtype="uint8")
# creating for line
cv2.line(my_img, (202, 220), (100, 160), (0, 20, 200), 10)
cv2.imshow('Window', my_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
