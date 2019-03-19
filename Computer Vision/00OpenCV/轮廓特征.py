import cv2
import numpy as np


# img = cv2.imread("./image/sk002.jpg", 0)
# # 21.2.1矩
# ret, thresh = cv2.threshold(img, 200, 255, 0)
# contours, hierarchy = cv2.findContours(img, 1, 2)
# # res1 = cv2.drawContours(img, contours, 3, (0, 255, 0))
#
# cnt = contours[0]
# M = cv2.moments(cnt)
# # print(M)
#
# # 21.2.2 轮廓面积
# area = cv2.contourArea(cnt)
# print("area:", area)
#
# # 21.2.3 轮廓周长
# perimeter = cv2.arcLength(cnt, True)
# print("Perimeter:", perimeter)
#
# # 21.2.4 轮廓近似
# epsilon = 0.1*cv2.arcLength(cnt, True)
# approx = cv2.approxPolyDP(cnt, epsilon, True)  # 得到矩形四个点。
# print(approx)

# =============================================================================

# 21.2.5  凸包

img = cv2.imread("./image/contourFeatures.png")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]
# 21.2.6 凸性检测
# k = cv2.isContourConvex(cnt)
# print(k)

# 21.2.7 边界矩形

# 直边界矩形
x, y, w, h = cv2.boundingRect(cnt)
rect1 = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow("boundingRect", rect1)

# 旋转的边界矩形

rect2 = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect2)
box = np.int0(box)
im = cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
cv2.imshow("minRect", im)

# 21.2.8 最小外接圆：

(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
rect3 = cv2.circle(img, center, radius, (255, 0, 0), 2)
cv2.imshow("minEnclosingCircle", rect3)


# 21.2.9 椭圆拟合

ellipse = cv2.fitEllipse(cnt)
rect4 = cv2.ellipse(img, ellipse, (0, 128, 128), 3)
cv2.imshow("ellipse", rect4)

# 21.2.10  直线拟合：
rows, cols = img.shape[:2]
[vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x*vy/vx)+y)
righty = int(((cols-x)*vy/vx)+y)
rect5 = cv2.line(img, (cols-1, righty), (0, lefty), (0, 255, 0), 2)
cv2.imshow("FitLine", rect5)

# 21.3.6  掩膜和像素点：
# mask = np.zeros(img.shape, np.uint8)
mask = np.zeros(imgray.shape, np.uint8)
cv2.drawContours(mask, [cnt], 0, 255, -1)
pixelpoints = np.transpose(np.nonzero(mask))
# pixelpoints = cv2.findNonZero(mask)
print(pixelpoints.shape)
print(type(pixelpoints))


# 21.3.7  图像像素统计方法：



cv2.waitKey(0)
cv2.destroyAllWindows()
