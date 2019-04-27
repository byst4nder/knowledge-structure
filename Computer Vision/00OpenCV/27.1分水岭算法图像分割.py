"""
ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)


"""

import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('image/water_coins.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# noise removal
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# sure background area
sure_bg = cv2.dilate(opening, kernel, iterations=3)
plt.subplot(2, 3, 1), plt.imshow(sure_bg, cmap='gray'), plt.title("sure_bg")
# cv2.imshow("sure_bg", sure_bg)
# Finding sure foreground area
# 距离变换的基本含义是计算一个图像中非零像素点到最近的零像素点的距离，也就是到零像素点的最短距离
# 个最常见的距离变换算法就是通过连续的腐蚀操作来实现，腐蚀操作的停止条件是所有前景像素都被完全
# 腐蚀。这样根据腐蚀的先后顺序，我们就得到各个前景像素点到前景中心??像素点的
# 距离。根据各个像素点的距离值，设置为不同的灰度值。这样就完成了二值图像的距离变换
# cv2.distanceTransform(src, distanceType, maskSize)
# 第二个参数 0,1,2 分别表示 CV_DIST_L1, CV_DIST_L2 , CV_DIST_C
dist_transform = cv2.distanceTransform(opening, 1, 5)    # 标记前景图像采用了距离变换函数。
xianshi = np.uint8(dist_transform)
cv2.imshow("abc", xianshi)
ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
# cv2.imshow("sure_fg", sure_fg)
plt.subplot(2, 3, 2), plt.imshow(sure_fg, cmap='gray'), plt.title("sure_fg")
unknown = cv2.subtract(sure_bg, sure_fg)
plt.subplot(2, 3, 3), plt.imshow(unknown, cmap='gray'), plt.title("unknown")

# cv2.imshow("unknown", unknown)

# Marker labelling
ret, markers1 = cv2.connectedComponents(sure_fg)
plt.subplot(2, 3, 4), plt.imshow(markers1, cmap='gray'), plt.title("markers1")
# Add one to all labels so that sure background is not 0, but 1
markers = markers1+1
# plt.imshow(markers, cmap="gray"), plt.title("markers")
# markers = np.unit8(markers)
# cv2.imshow("markers+1", markers)

# Now, mark the region of unknown with zero
markers[unknown == 255] = 0
plt.subplot(2, 3, 5), plt.imshow(markers, cmap="gray"), plt.title("markers[unknow==255]=0")
# 结果使用 JET 颜色地图表示。深蓝色区域为未知区域。肯定是硬币的区域使用不同的颜色标记。
# 其余区域就是用浅蓝色标记的背景了。
# 现在标签准备好了。到最后一步：实施分水岭算法了。标签图像将会被修改，边界区域的标记将变为 -1.
markers3 = cv2.watershed(img, markers)
img[markers3 == -1] = [255, 0, 0]
plt.subplot(2, 3, 6), plt.imshow(img), plt.title("img")

# plt.subplot(2, 3, 2), plt.imshow(sure_bg, cmap='gray'), plt.title("sure_bg")
# plt.subplot(2, 3, 3), plt.imshow(unknown, cmap='gray'), plt.title("unknown")
# plt.subplot(2, 3, 4), plt.imshow(markers1, cmap='gray'), plt.title("markers1")
# plt.subplot(2, 3, 5), plt.imshow(markers, cmap='gray'), plt.title("markers")
# plt.subplot(2, 3, 6), plt.imshow(markers3, cmap='gray'), plt.title("markers3")

plt.show()
# cv2.imshow("marker", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
