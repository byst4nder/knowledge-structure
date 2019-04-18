"""
cv2.HoughLinesP():
    函数的返回值就是直线的起点和终点。

"""
import cv2
import numpy as np

img = cv2.imread('./image/form.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
minLineLength = 100
maxLineGap = 10  # 可以加两个滑动条来控制。
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength, maxLineGap)

for i in range(len(lines)):

    # for x1, y1, x2, y2 in lines[0]:
    for x1, y1, x2, y2 in lines[i]:
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

cv2.imshow('houghlinesP', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

