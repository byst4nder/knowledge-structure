# cv2.getTrackbarPos()
# 函数的第一个参数是滑动条的名字，
# 第二个参数是滑动条被放置窗口的名字，
# 第三个参数是滑动条的默认位置。
# 第四个参数是滑动条的最大值，
# 第五个函数是回调函数，每次滑动条的滑动都会调用回调函数
# 回调函数通常都会含有一个默认参数，就是滑动条的位置。
# 滑动条的另外一个重要应用就是用作转换按钮。


import cv2
import numpy as np


def nothing(x):
    pass


def dosomething(x):
    pass


# Create a black image, a window
img = np.zeros((300, 512, 3), np.uint8)

cv2.namedWindow("image", cv2.WINDOW_NORMAL)   # 第一个参数是实例化窗口名称，第二个参数，窗口大小可以调节。

# Create trackbars for color change
cv2.createTrackbar("R", "image", 0, 255, nothing)
cv2.createTrackbar("G", "image", 0, 255, nothing)
cv2.createTrackbar("B", "image", 0, 255, nothing)

# Create switch for ON/OFF functionality
switch = "0-OFF \n1-ON"
cv2.createTrackbar(switch, "image", 0, 1, nothing)

while True:
    cv2.imshow("image", img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
        # cv2.destroyAllWindows()
    elif k == ord("s"):  # wait for "s" key to save and exit.
        cv2.imwrite("messigray.png", img)
    # get current positions of four trackbars
    r = cv2.getTrackbarPos("R", "image")
    g = cv2.getTrackbarPos("G", "image")
    b = cv2.getTrackbarPos("B", "image")
    s = cv2.getTrackbarPos(switch, "image")

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]


cv2.destroyAllWindows()


# 注意事项：createTrackbar的第二个参数，必须和namedWindow的第一个参数完全一致。
# getTrackbarPos的第一个参数必须和createTrackbar的第一个参数完全一致。
# getTrackbarPos的第二个参数必须和createTrackbar的第二个参数完全一致。
# imshow的第一个参数必须跟namedWindow的参数相同，才可以同框显示。否则是两个窗口。


# cv2.waitKey()是一个键盘绑定函数，在毫秒级时间内，如果键盘有输入就返回按键的ASCII码值，程序继续运行。如果没有输入，返回-1。
# 如果设置为零，则无限期等待。
# 也可以被用来检测特定键是否被按下，k==27,检测ESC to exit
