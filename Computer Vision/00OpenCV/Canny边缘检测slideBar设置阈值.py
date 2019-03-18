import cv2
import numpy as np
from matplotlib import pyplot as plt
minVal = 0
maxVal = 255


def onCannyThreshold(x):
    global minVal, maxVal
    minVal = cv2.getTrackbarPos("minVal", "Canny_slideBar")
    maxVal = cv2.getTrackbarPos("maxVal", "Canny_slideBar")
    edges = cv2.Canny(img, minVal, maxVal)
    cv2.imshow("Canny_slideBar", edges)

    plt.subplot(121), plt.imshow(img, cmap="gray"), plt.title("Original Image")
    plt.subplot(122), plt.imshow(edges, cmap="gray"), plt.title("Edge Image")
    plt.show()


img = cv2.imread("./image/girl001.jpg", 0)

cv2.namedWindow("Canny_slideBar", cv2.WINDOW_NORMAL)
cv2.createTrackbar("minVal", "Canny_slideBar", 0, 255, onCannyThreshold)
cv2.createTrackbar("maxVal", "Canny_slideBar", 0, 255, onCannyThreshold)

cv2.waitKey(0)
cv2.destroyAllWindows()
