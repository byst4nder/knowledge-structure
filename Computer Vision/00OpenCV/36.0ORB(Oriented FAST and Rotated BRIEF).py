# ORB算法比 SURF 和 SIFT 算法快的多，ORB 描述符也比 SURF 好很多。ORB是低功耗设备的最佳选择。


import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('./image/CornerSample.jpg', 0)

# Initiate STAR detector
# orb = cv2.ORB()
orb = cv2.ORB_create()

# find the keypoints with ORB
kp = orb.detect(img, None)

# compute the descriptors with ORB
kp, des = orb.compute(img, kp)

# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0), flags=0)
plt.imshow(img2), plt.show()
