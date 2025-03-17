import numpy as np
import cv2
my_img = np.zeros((400, 400, 3), dtype="uint8")
# Writing text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(my_img, 'Tutorials Point', (50, 50),
            font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)
cv2.imshow('Window', my_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
