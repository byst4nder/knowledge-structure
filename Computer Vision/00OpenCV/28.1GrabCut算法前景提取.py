import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread("./image/blue_shorts.jpg")
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# 包含前景的矩形，格式为 (x,y,w,h)
# 为了确定rect，反复调整ROI
# x = 190
# y = 90
# w = 300
# h = 750
# ROI = img[y:y+h, x:x+w]
# cv2.imshow("rect", ROI)

rect = (190, 90, 300, 750)

# 函数返回值是迭代更新的mask, bgdModel, fgdModel。
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")
img = img*mask2[:, :, np.newaxis]

# plt.imshow(img), plt.colorbar(), plt.show()
cv2.imshow("fg", img)
plt.imshow(mask), plt.title("mask"), plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

# 经过测试发现，还是缺少一些部分，下面进行修改。完善。

