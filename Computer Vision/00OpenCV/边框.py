import cv2
import numpy as np
from matplotlib import pyplot as plt


BLUE = [255, 0, 0]

img = cv2.imread("./image/opencv_logo2.png")
constant = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)
plt.imshow(constant, "gray")
plt.show()
