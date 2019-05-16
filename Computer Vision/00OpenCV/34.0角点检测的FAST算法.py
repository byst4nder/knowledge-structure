import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('./image/CornerSample.jpg', 0)

# Initiate FAST object with default values
# fast = cv2.FastFeatureDetector()
fast = cv2.FastFeatureDetector_create(threshold=25)

# find and draw the keypoints
kp = fast.detect(img, None)
img2 = cv2.drawKeypoints(img, kp, None, color=(255, 0, 0))

# Print all default params
# print("Threshold: ", fast.getInt('threshold'))
print("Threshold: ", fast.getThreshold())
# print("nonmaxSuppression: ", fast.getBool('nonmaxSuppression'))
print("nonmaxSuppression: ", fast.getNonmaxSuppression())
# print("neighborhood: ", fast.getInt('type'))
print("neighborhood: ", fast.getType())
print("Total Keypoints with nonmaxSuppression: ", len(kp))

cv2.imwrite('./image/fast_true.png', img2)

# Disable nonmaxSuppression
# fast.setBool('nonmaxSuppression', 0)
fast.setNonmaxSuppression(0)
kp = fast.detect(img, None)

print("Total Keypoints without nonmaxSuppression: ", len(kp))

img3 = cv2.drawKeypoints(img, kp, None, color=(255, 0, 0))

cv2.imwrite('./image/fast_false.png', img3)
