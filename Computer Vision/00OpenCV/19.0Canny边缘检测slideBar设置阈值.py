"""
cv2.Canny()边界检测：
    参数一:输入二值化图
    参数二：
    参数三：
    参数四：用来计算图像梯度的 Sobel卷积核的大小，默认值为 3
    参数五：L2gradient，它可以用来设定求梯度大小的方程


"""
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
img = cv2.GaussianBlur(img, (5, 5), 0)

cv2.namedWindow("Canny_slideBar", cv2.WINDOW_NORMAL)
cv2.createTrackbar("minVal", "Canny_slideBar", 0, 255, onCannyThreshold)
cv2.createTrackbar("maxVal", "Canny_slideBar", 0, 255, onCannyThreshold)

cv2.waitKey(0)
cv2.destroyAllWindows()


# Canny边缘检测算法可以分为以下5个步骤：：
# 1、使用高斯滤波器，以平滑图像，滤除噪声。
#
# 2、计算图像中每个像素点的梯度强度和方向。
#
# 3、应用非极大值（Non-Maximum Suppression）抑制，以消除边缘检测带来的杂散响应。
#
# 4、应用双阈值（Double-Threshold）检测来确定真实的和潜在的边缘。
#
# 5、通过抑制孤立的弱边缘最终完成边缘检测。

# 一：高斯平滑滤波
#       高斯卷积核大小的选择将影响Canny检测器的性能。尺寸越大，检测器对噪声的敏感度越低，但是边缘检测的定位误差也将略有增加。
#       一般5x5是一个比较不错的trade off。

# 二：非极大值抑制
# 一种边缘稀疏技术，非极大值抑制的作用在于“瘦”边。
