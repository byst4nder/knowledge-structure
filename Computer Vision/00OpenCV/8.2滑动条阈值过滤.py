# 参考文献：
# https://blog.csdn.net/qq_34711208/article/details/81707949
import cv2
# import numpy as np


img = cv2.imread("./image/cow01.jpeg")
img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gauss = cv2.GaussianBlur(img2gray, (3, 3), 1)


def on_threshold(x):
    ch_val = cv2.getTrackbarPos("Threshold", "cowBar")
    # run_flag, threshold_img = cv2.threshold(img, ch_val, 255, cv2.THRESH_BINARY)
    # run_flag, threshold_img = cv2.threshold(img2gray, ch_val, 255, cv2.THRESH_BINARY)
    # run_flag, threshold_img = cv2.threshold(gauss, ch_val, 255, cv2.THRESH_BINARY)

    run_flag_a, binary = cv2.threshold(gauss, ch_val, 255, cv2.THRESH_BINARY)
    run_flag_b, binary_inv = cv2.threshold(gauss, ch_val, 255, cv2.THRESH_BINARY_INV)
    run_flag_c, trunc = cv2.threshold(gauss, ch_val, 255, cv2.THRESH_TRUNC)
    run_flag_d, to_zero = cv2.threshold(gauss, ch_val, 255, cv2.THRESH_TOZERO)
    run_flag_e, to_zero_inv = cv2.threshold(gauss, ch_val, 255, cv2.THRESH_TOZERO_INV)

    # if run_flag:
    #     cv2.imshow("cowBar", threshold_img)
    if run_flag_a:
        cv2.imshow("Binary", binary)
    if run_flag_b:
        cv2.imshow("Binary_INV", binary_inv)
    if run_flag_c:
        cv2.imshow("Trunc", trunc)
    if run_flag_d:
        cv2.imshow("To_Zero", to_zero)
    if run_flag_e:
        cv2.imshow("To_Zero_Inv", to_zero_inv)


cv2.namedWindow("cowBar")
cv2.createTrackbar("Threshold", "cowBar", 0, 255, on_threshold)
cv2.imshow("origin_img", img)
cv2.imshow("cowBar", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imshow("canshu1",参数2)
# imshow的参数1，定位窗口，如果窗口存在，就显示那个窗口，如果窗口不存在，则创建窗口。
# 参数2，在窗口中，显示内容。

# threshold返回两个值：一个是阈值retVal,另一个是过滤图像。
