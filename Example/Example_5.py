import numpy as np
import cv2
my_img = np.zeros((400, 400, 3), dtype="uint8")
# creating for rectangle
cv2.ellipse(my_img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
cv2.imshow('Window', my_img)
# allows us to see image
# until closed forcefully
cv2.waitKey(0)
cv2.destroyAllWindows()
