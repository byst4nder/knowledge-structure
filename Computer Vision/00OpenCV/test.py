import cv2
import numpy as np


# 切割ROI
# img = cv2.imread("./image/ball.png", 0)
# # cv2.imshow("img", img)
# ball = img[310:365, 360:430]
#
# img[100:155, 200:270] = ball
# cv2.imshow("img", img)

# 图像加法和图像混合
# img1 = cv2.imread("./image/sk001.jpg")
# img2 = cv2.imread("./image/sk002.jpg")
#
# addImg = cv2.add(img1, img2)     # 饱和运算。
# addWeightImg = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
#
#
# cv2.imshow("img1", img1)
# cv2.imshow("img2", img2)
# cv2.imshow("addImg", addImg)
# cv2.imshow("addWeighted", addWeightImg)
# 因为OpenCV的加法是饱和运算：超过255，就为255，变成白色。
# numpy 运算是模操作，超过255，取余。
# cv2.add加和起来，颜色会改变，因为超过255就为白色，叠加为其他色。
# cv2.addWeighted加和起来有一种透明的效果。


# 测试灰度图效果：
img1 = cv2.imread("./image/sk001.jpg", 4)
img2 = cv2.imread("./image/sk002.jpg", 4)

addImg = cv2.add(img1, img2)  # 饱和运算。
addWeightImg = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)


cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("addImg", addImg)
cv2.imshow("addWeighted", addWeightImg)



cv2.waitKey(0)
cv2.destroyAllWindows()

