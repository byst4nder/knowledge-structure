import cv2
import numpy as np


img = cv2.imread('./image/home.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# sift = cv2.SIFT()
sift = cv2.xfeatures2d.SIFT_create()

kp = sift.detect(gray, None)

img = cv2.drawKeypoints(gray, kp, img)

cv2.imwrite('sift_keypoints.jpg', img)

# 这个算法包含在 OpenCV 中的收费模块中。
