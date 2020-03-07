# Probabilistic_Hough_Transform 是对霍夫变换的一种优化。
# 它不会对每一个点都进行计算，而是从一幅图像中随机选取一个点集进行计算，对于直线检测来说这已经足够了。
# 但是使用这种变换我们必须要降低阈值。
# 函数的返回值就是直线的起点和终点。
import cv2
import numpy as np


img = cv2.imread('lines.bmp')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 20, 150, apertureSize=3)
minLineLength = 200  # 线的最短长度。比这个短的线都会被忽略。
maxLineGap = 10  # 两条线段之间的最大间隔，如果小于此值，这两条直线就被看成是一条直线。
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength, maxLineGap)
for x1, y1, x2, y2 in lines[0]:
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)


cv2.imshow("result", img)
cv2.waitKey(3000)
cv2.destroyAllWindows()


# 不好用，暂时放放。
