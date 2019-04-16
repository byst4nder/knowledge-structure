# 思路：
# 基于特征的匹配所处理的图像一般包含的特征有颜色特征、纹理特征、形状特征、空间位置特征等。

# 基于多种颜色来分割图像。

import cv2
import numpy as np
# S1：颜色转化空间：
# 方法一：
# flags = [i for i in dir(cv2) if i.startswith("COLOR_")]
# print(flags[:10])
# 方法二:
# L = []
# for i in dir(cv2):
#     if i.startswith("COLOR_"):
#         print(i)
#         L.append(i)
# print(len(L))
img = cv2.imread("./image/ska07_01.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# gauss = cv2.GaussianBlur(gray, (3, 3), 1)   高斯模糊待测：灰度图分割效果不明显：
# cv2.imshow("hsv", hsv)
# S2:颜色空间之多，逐渐尝试。目前只先使用HSV。

# ROI = hsv[100:, 100:]   # 此处暂时不引入：

lower_val = np.array([0, 0, 0])
upper_val = np.array([255, 255, 255])


def onHSVBlur(x):
    global lower_val
    global upper_val
    switch_flag = cv2.getTrackbarPos(switch_name, "HSVBlur")
    if switch_flag == 0:
        h = cv2.getTrackbarPos("H", "HSVBlur")
        s = cv2.getTrackbarPos("S", "HSVBlur")
        v = cv2.getTrackbarPos("V", "HSVBlur")
        lower_val = np.array([h, s, v])
    else:
        h = cv2.getTrackbarPos("H", "HSVBlur")
        s = cv2.getTrackbarPos("S", "HSVBlur")
        v = cv2.getTrackbarPos("V", "HSVBlur")
        upper_val = np.array([h, s, v])

    # 根据阈值构建掩模。
    mask = cv2.inRange(hsv, lower_val, upper_val)
    # 不等价阈值筛选
    # mask = cv2.threshold(hsv, lower_val, upper_val, cv2.THRESH_BINARY)
    # mask_inv = cv2.bitwise_not(mask)
    # 对原图像和掩模进行位运算。!!!!!!!这个是重点。
    res = cv2.bitwise_and(img, img, mask=mask)

    kernel1 = np.ones((7, 7), np.uint8)
    kernel2 = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(res, kernel1, iterations=1)
    dilation = cv2.dilate(erosion, kernel2, iterations=1)
    # mask_inv = cv2.bitwise_not(dilation)
    opening = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel2)  # 膨胀腐蚀，加开闭运算。去除杂质，平滑。
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel1)

    # cv2.imshow("origin_img", img)
    # cv2.imshow("hsv", hsv)
    cv2.imshow("mask", mask)
    cv2.imshow("HSVBlur", closing)
    print("Lower_Val:", lower_val)
    print("Upper_Val:", upper_val)

    copy = cv2.cvtColor(closing, cv2.COLOR_BGR2GRAY)
    contours, hierarchy = cv2.findContours(copy, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    contours = cv2.drawContours(img, contours, 3, (0, 255, 0), 3)
    cv2.imshow("contours", contours)


cv2.namedWindow("HSVBlur", cv2.WINDOW_NORMAL)
# cv2.namedWindow("HSVBlur")

switch_name = "low:0\nup:1"
cv2.createTrackbar(switch_name, "HSVBlur", 0, 1, onHSVBlur)
cv2.createTrackbar("H", "HSVBlur", 0, 255, onHSVBlur)
cv2.createTrackbar("S", "HSVBlur", 0, 255, onHSVBlur)
cv2.createTrackbar("V", "HSVBlur", 0, 255, onHSVBlur)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Lower_Val: [ 0  0 86]
# Upper_Val: [ 63  78 255]