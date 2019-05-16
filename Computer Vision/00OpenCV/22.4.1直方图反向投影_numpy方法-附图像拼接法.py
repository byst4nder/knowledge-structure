# https://my.oschina.net/wujux/blog/801380?utm_source=debugrun&utm_medium=referral

"""
1、OpenCV中cv2.imwrite()中文路径读取保存办法：
2、矩阵图像拼接方法：np.vstack()和np.hstack()
3、numpy中的算法来实现反向投影。
4、通道拆分(cv2.split)及合并(cv2.merge)

"""
import io
import sys

import cv2
import numpy as np
from matplotlib import pyplot as plt


# target = img is the image we search in
img = cv2.imread("./image/blue_shorts.jpg")
hsvt = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print("hsvt.shape:", hsvt.shape)

# roi is the object or region of object we need to find.
roi = cv2.imread("./image/roi.jpg")
roi = roi[560:805, 225:475]
# cv2.imshow("roi", roi)
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# Numpy的方法：
M = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
I = cv2.calcHist([hsvt], [0, 1], None, [180, 256], [0, 180, 0, 256])
# plt.plot(M)
# plt.plot(I)
h, s, v = cv2.split(hsvt)
# print(img.shape)
# print(h.shape)
R = M / (I+1)   # 根据R这个"调色板"创建一副新的图像，其中的每一个像素代表这个点就是目标的概率。
print("R.shape:", R.shape)
B = R[h.ravel(), s.ravel()]
print("numpy中的ravel(),可以将多维数组转换为一维数组")
B = np.minimum(B, 1)
print("np.minimum(B, 1):将B中，数字挨个比较，如果小于1，则原值输出，如果大于1则，相应位置输出1。")
print(B.shape)
B = B.reshape(hsvt.shape[:2])

disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))   # 构造卷积核
B = cv2.filter2D(B, -1, disc)    # filter2D运用内核实现对图像的卷积运算。
B = np.uint8(B)
cv2.normalize(B, B, 0, 255, cv2.NORM_MINMAX)
# 现在输出图像中灰度值最大的地方就是我们要查找的目标的位置了。
# 如果我们要找的是一个区域，我们就可以使用一个阈值对图像进行二值化。
cv2.imshow("B", B)

ret, thresh = cv2.threshold(B, 50, 255, 0)
res = cv2.bitwise_and(img, img, mask=thresh)
# cv2.imshow('nice', res)
# cv2.imshow('img', img)
res1 = np.vstack((img, cv2.merge((B, B, B)), res))   # 垂直拼接
res2 = np.hstack((img, cv2.merge((B, B, B)), res))   # 水平拼接
# np.vstack按垂直方向（行顺序）堆叠数组构成一个新的数组
# np.hstack按水平方向（列顺序）堆叠数组构成一个新的数组
# 通道拆分(cv2.split)及合并(cv2.merge)
# 此处为图像拼接。

# cv2.imwrite('thresh.png',thresh)
# cv2.imwrite('output.png',res)
cv2.imshow("result", res1)
cv2.imshow("result2", res2)
path1 = "./image/numpy_直方图反向投影_垂直拼接.jpg"
path2 = "./image/numpy_直方图反向投影_水平拼接.jpg"
# cv2.imwrite("./image/numpy_直方图反向投影_垂直拼接.jpg", res1)
cv2.imencode(".jpg", res1)[1].tofile(path1)
# cv2.imwrite("./image/numpy_直方图反向投影_水平拼接.jpg", res2)
# img = cv2.imdecode(np.fromfile(img_path,dtype=np.uint8),cv2.IMREAD_UNCHANGED)
cv2.imencode(".jpg", res2)[1].tofile(path2)


# OpenCV中提供了cv2.calcBackProject()

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
