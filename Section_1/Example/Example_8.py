import numpy as np
import cv2
# Read the Image
# Load an color image in grayscale
img = cv2.imread(
    r'C:\Users\duong\Desktop\Biomedical_Image_Processing\Biomedical_Image_Processing\Figure\Figure_1.jpg', 1)
# Display the image
cv2.imshow('image', img)
# key binding function
k = cv2.waitKey(0)
# wait for ESC key to exit
if k == 27:
    cv2.destroyAllWindows()
# wait for 's' key to save and exit
elif k == ord('s'):
    cv2.imwrite('Figure_1.jpg', img)
    cv2.destroyAllWindows()
