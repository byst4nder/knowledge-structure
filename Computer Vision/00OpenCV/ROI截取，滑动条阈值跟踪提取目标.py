# 颜色空间转换：
# 1、对图像进行颜色空间转换，比如从 BGR 到灰度图，或者从BGR 到 HSV 等。
# 2、创建一个程序用来从一幅图像中获取某个特定颜色的物体。
# 3、cv2.cvtColor(),cv2.inRange()

import cv2
import numpy as np

# 输出颜色转换flag.方式一：
# flags=[i for i in dir(cv2) if i.startswith("COLOR_")]
# print(flags)

# 方式二
# L = []
# for i in dir(cv2):
#     if i.startswith("COLOR_"):
#         print(i)
#         L.append(i)
# print(len(L))

# 物体跟踪：
# S1：
# 方式一：通过电脑自带的  画图工具==>颜色选取器（小滴管状）==>点击编辑颜色查看色调E：饱和度S：亮度L
# 记录数值，然后通过移动位置，多次确定大致范围。进入阈值过虑处理操作。
# 针对blue_shorts.jpg图像，定位short位置，通过颜色实例分割。
# E:141, S:159, L：62
# E:142, S:156, L：95
# E:149, S:123, L: 48
# 方式二：通过颜色转化然后查看ROI的值。还是可以通过画图软件确定ROI的像素范围:
img = cv2.imread("./image/blue_shorts.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cv2.imshow("origin", img)
# cv2.imshow("hsv", hsv)    # 查看HSV中大面积相同的才是可以容易提取的。否则换一种颜色空间！！！！！！！！！！！
# 一个是裤子，一个皮肤。

# ROI = img[600:750, 300:400]
# cv2.imshow("blue_shorts", ROI)
# 第一个参数是高度，第二个参数是宽度。
ROI = hsv[600:750, 300:400]
# print(ROI[10, 10])
# [106 200 111]


# S2:有个大致范围后，然后编写阈值过滤函数，进入筛选，最后只剩一个一个shorts.
lower_val = np.array([0, 0, 0])
upper_val = np.array([255, 255, 255])


def OnMaskBlur(x):
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
    # 等价阈值筛选
    # mask = cv2.threshold(hsv, lower_val, upper_val, cv2.THRESH_BINARY)

    # 对原图像和掩模进行位运算。!!!!!!!这个是重点。
    res = cv2.bitwise_and(img, img, mask=mask)

    # cv2.imshow("origin_img", img)
    cv2.imshow("hsv", hsv)
    cv2.imshow("mask", mask)
    cv2.imshow("HSVBlur", res)
    print("Lower_Val:", lower_val)
    print("Upper_Val:", upper_val)

    # 将目标区域轮廓画出。
    copy = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    contours, hierarchy = cv2.findContours(copy, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    blue_contours = cv2.drawContours(img, contours, 3, (0, 255, 0), 3)
    cv2.imshow("blue_contours", blue_contours)


# 一个调节区调节两个值，所以，需要一个转换开关。
# cv2.namedWindow("HSVBlur", cv2.WINDOW_NORMAL)
cv2.namedWindow("HSVBlur")

switch_name = "low:0\nup:1"
cv2.createTrackbar(switch_name, "HSVBlur", 0, 1, OnMaskBlur)
cv2.createTrackbar("H", "HSVBlur", 0, 255, OnMaskBlur)
cv2.createTrackbar("S", "HSVBlur", 0, 255, OnMaskBlur)
cv2.createTrackbar("V", "HSVBlur", 0, 255, OnMaskBlur)
# 这样就可以做一个软件标注工具，不再用PS逐渐标注。而且实现精准标注。
# 此时实现了裤子的标注，加颜色就可以了。但是还需要过滤筛选点一些杂质点。后续学习研究。
# 此时也可以用轮廓来标注。
# 参考图片：hsv来实现目标的标注分割，阈值过程图。以及分析过程.png

# 第二种方法是通过threshold阈值筛选来完成。可以尝试！


cv2.waitKey(0)
cv2.destroyAllWindows()
