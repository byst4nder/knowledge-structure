# https://blog.csdn.net/u013063099/article/details/81937848
import cv2
import numpy as np


srcImg = cv2.imread("text.jpg")
gray = cv2.cvtColor(srcImg, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 50, 200, 3)
# cv2.imshow("canny", canny)

# 通过霍夫变换检测直线：
lines = cv2.HoughLines(canny, 1, np.pi/180, 200)
print(len(lines))
# 由于图像不同，阈值不好设定，因为阈值设定过高导致无法检测直线，阈值过低直线太多，速度很慢
# 所以根据阈值由大到小设置了三个阈值，如果经过大量试验后，可以固定一个适合的阈值。
# L = 1
# thres = 150
# while L > 0:
#     lines = cv2.HoughLines(canny, 1, np.pi / 180, threshold=thres)
#     if lines is None:
#         print(thres)
#         exit(-1)
#     L = len(lines)
#     print(L)
#     thres += 5   # 290为None。
# thres = 285
# while L < 100:
#     lines = cv2.HoughLines(canny, 1, np.pi / 180, threshold=thres)
#     L = len(lines)
#     print(L)
#     thres -= 5
#     print(thres)
L = len(lines)
# print(lines)
sum = 0
print(list(lines[0])[0])
for i in range(L):
    for rho, theta in lines[i]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        pt1_x = int(round(x0 + 1000 * (-b)))
        pt1_y = int(round(y0 + 1000 * a))
        pt2_x = int(round(x0 - 1000 * (-b)))
        pt2_y = int(round(y0 - 1000 * a))
        sum += theta
        cv2.line(srcImg, (pt1_x, pt1_y), (pt2_x, pt2_y), (255, 0, 0), 1, cv2.LINE_AA)
average = sum / L
angle = average / np.pi * 180 - 90
# 以图像中心为旋转中心
h, w = srcImg.shape[:2]
# 计算二维旋转的仿射变换矩阵
RotateMatrix = cv2.getRotationMatrix2D((w/2.0, h/2.0), angle, 1)
# 仿射变换，背景色填充为白色
dst = cv2.warpAffine(srcImg, RotateMatrix, (w, h), borderValue=(255, 255, 255))

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
