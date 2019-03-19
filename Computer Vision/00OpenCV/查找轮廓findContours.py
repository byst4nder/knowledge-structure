import numpy as np
import cv2


img = cv2.imread("./image/sk002.jpg")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 200, 255, 0)


contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 绘制独立轮廓，方法一；
img1 = cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
# 绘制独立轮廓，方法二：
img2 = cv2.drawContours(img, contours, 3, (0, 255, 0), 3)
cv2.imshow("img", img)   # img被玷污了。。。
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
