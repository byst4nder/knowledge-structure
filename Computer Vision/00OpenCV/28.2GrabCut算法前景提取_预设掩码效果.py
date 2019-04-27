import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread("./image/blue_shorts.jpg")
mask = np.zeros(img.shape[:2], np.uint8)
newmask = cv2.imread("./image/girl_mask.jpg", 0)
mask[newmask == 0] = 0
mask[newmask == 255] = 1

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

rect = (190, 90, 300, 750)

# 函数返回值是迭代更新的mask, bgdModel, fgdModel。
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")
img = img*mask2[:, :, np.newaxis]

# plt.imshow(img), plt.colorbar(), plt.show()
cv2.imshow("fg", img)
plt.imshow(mask2), plt.title("mask2"), plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

# 经过测试发现，预设完全掩码效果不可取。

