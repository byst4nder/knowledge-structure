import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('./image/water_coins.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('./image/coin_b.jpg', 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.50
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)

# cv2.imwrite('res.png', img_rgb)
cv2.imshow("res", img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 此处可以配合滑动条，设置上下阈值进行过滤筛选。
