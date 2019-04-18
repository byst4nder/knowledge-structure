import cv2
import numpy as np

img1 = cv2.imread("./image/sk001.jpg", 0)
img2 = cv2.imread("./image/sk002.jpg", 0)
# cv2.imshow("img0", img2)

ret1, thresh1 = cv2.threshold(img1, 127, 255, 0)
ret1, thresh2 = cv2.threshold(img2, 127, 255, 0)

contours1, hierarchy = cv2.findContours(thresh1, 2, 1)
cnt1 = contours1[0]
contours2, hierarchy = cv2.findContours(thresh2, 2, 1)
cnt2 = contours2[0]

img1 = cv2.drawContours(img2, contours2, -1, (0, 0, 255), 3)
ret = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
print(ret)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
