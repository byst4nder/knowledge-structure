#! python2
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

from skimage.transform import hough_line

from skimage.draw import line

img = np.zeros((100, 150), dtype=bool)  # 零值黑底图：bool类型
img[30, :] = 1          # 行号30画白线，设置为True
img[:, 65] = 1          # 列号65画白线，设置为True
img[35:45, 35:50] = 1   # 矩形切割，
rr, cc = line(60, 130, 80, 10)      # 画线
img[rr, cc] = 1                     # 线白
img += np.random.random(img.shape) > 0.99  # 这一句不得了了：
# np.random.random((100, 150))  随机值矩阵，内部参数为元组。这样的矩阵构成一幅图像。灰度图。
# >0.99 作为一个阈值，进行筛选。如果大于0.99则返回True.
# 加号，可以理解为取并集。

out, angles, d = hough_line(img)

fix, axes = plt.subplots(1, 2, figsize=(7, 4))

axes[0].imshow(img, cmap=plt.cm.gray)
axes[0].set_title('Input image')

axes[1].imshow(
    out, cmap=plt.cm.bone,
    extent=(np.rad2deg(angles[-1]), np.rad2deg(angles[0]), d[-1], d[0]))
axes[1].set_title('Hough transform')
axes[1].set_xlabel('Angle (degree)')
axes[1].set_ylabel('Distance (pixel)')

plt.tight_layout()
plt.show()
