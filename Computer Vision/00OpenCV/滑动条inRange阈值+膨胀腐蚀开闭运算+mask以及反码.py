import cv2
import numpy as np


img = cv2.imread("./image/blue_shorts.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gauss = cv2.GaussianBlur(gray, (3, 3), 1)

# mask = np.zeros(img.shape, np.uint8)

low_val = 0
up_val = 255
# mask = np.zeros(img.shape[:2], np.uint8)


def onMask(x):
    global low_val
    global up_val

    low_val = cv2.getTrackbarPos("low_val", "inRangeMask")
    up_val = cv2.getTrackbarPos("up_val", "inRangeMask")
    mask = cv2.inRange(gauss, low_val, up_val)
    # ret, mask = cv2.threshold(img2gray, low_val, up_val, cv2.THRESH_BINARY)
    kernel1 = np.ones((7, 7), np.uint8)
    kernel2 = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(mask, kernel1, iterations=1)
    dilation = cv2.dilate(erosion, kernel2, iterations=1)
    mask_inv = cv2.bitwise_not(dilation)
    opening = cv2.morphologyEx(mask_inv, cv2.MORPH_OPEN, kernel2)  # 膨胀腐蚀，加开闭运算。去除杂质，平滑。
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel1)

    cv2.imshow("inRangeMask", closing)
    # global mask
    cv2.imwrite("./image/girl_mask.jpg", closing)


cv2.namedWindow("inRangeMask")
cv2.createTrackbar("low_val", "inRangeMask", 0, 255, onMask)
cv2.createTrackbar("up_val", "inRangeMask", 255, 255, onMask)


# cv2.imshow("img", img)
# cv2.imshow("gray", gray)
# cv2.imshow("hsv", hsv)
# cv2.imshow("mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

