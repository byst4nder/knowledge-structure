import cv2
import numpy as np


srcImg = cv2.imread("invoice.jpg")
rows, cols, ch = srcImg.shape
gray = cv2.cvtColor(srcImg, cv2.COLOR_BGR2GRAY)
ret, thres = cv2.threshold(gray, 100, 200, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnt = contours[0]

rect = cv2.minAreaRect(cnt)
angle = rect[2]
center = rect[0]
box = cv2.boxPoints(rect)   # 获取四个顶点坐标，这个四个顶点要用来切割图像。
box = np.int0(box)    # 框的mask
box_w = int(np.sqrt((box[3][1]-box[0][1])**2 + (box[3][0]-box[0][0])**2))
box_h = int(np.sqrt((box[1][1]-box[0][1])**2 + (box[1][0]-box[0][0])**2))
# 为了长平型，如果近x轴正向边较短则顺时针余角。
if box_w < box_h:
    angle = 90 + angle
mask = np.zeros(srcImg.shape[:2], np.uint8)
cv2.drawContours(mask, [cnt], 0, 255, -1)
cv2.imshow("mask", mask)
ROI = cv2.add(srcImg, np.zeros(np.shape(srcImg), dtype=np.uint8), mask=mask)
cv2.imshow("ROI", ROI)
M = cv2.getRotationMatrix2D(center, angle, 1)
rotate = cv2.warpAffine(ROI, M, (cols, rows))
gray2 = cv2.cvtColor(rotate, cv2.COLOR_BGR2GRAY)
# contours2, hierarchy2 = cv2.findContours(gray2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# x, y, w, h = cv2.boundingRect(contours2[0])
x, y, w, h = cv2.boundingRect(gray2)

res = rotate[y:y+h, x:x+w]
cv2.imshow("res", res)
cv2.waitKey(0)
cv2.destroyAllWindows()


