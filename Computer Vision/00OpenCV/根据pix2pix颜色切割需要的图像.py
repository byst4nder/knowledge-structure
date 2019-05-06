import cv2
import numpy as np
from matplotlib import pyplot as plt


img_o = cv2.imread("./image/1.png")
img_m = cv2.imread("./image/2.png")
cols, rows, _ = img_o.shape
B_channel, G_channel, R_channel = cv2.split(img_m)

_, RedThresh = cv2.threshold(R_channel, 160, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(RedThresh)
# 方法二：
# lower_blue = np.array([120, 120, 120])
# upper_blue = np.array([150, 150, 150])
#
# mask = cv2.inRange(img_m, lower_blue, upper_blue)
cv2.imshow("mask", mask_inv)
kernel = np.ones((25, 25), np.uint8)
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
closing = cv2.morphologyEx(mask_inv, cv2.MORPH_CLOSE, kernel)
opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
cv2.imshow("opening", opening)
# masked_img = cv2.bitwise_and(img_o, img_o, mask=opening)  # 实物图分割。
(cnts, _) = cv2.findContours(opening.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
if len(cnts) == 0:
    # print("skipped: %s" % (image_path))
    print("......")
else:
    c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
    x, y, w, h = cv2.boundingRect(c)
    cropImg = img_o[y:y + h, x:x + w]
cv2.imshow("res", cropImg)
cv2.waitKey(0)
cv2.destroyAllWindows()


