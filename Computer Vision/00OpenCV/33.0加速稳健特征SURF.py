import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("./image/fly.jpg", 0)

# Create SURF object. You can specify params here or later.
# Here I set Hessian Threshold to 400
surf = cv2.SURF(400)


# Find keypoints and descriptors directly
kp, des = surf.detectAndCompute(img, None)


print(len(kp))

# Check present Hessian threshold
print(surf.hessianThreshold)

# 在一幅图像中显示699 个关键点太多了。我们把它缩减到50 个再绘制到图片上。
# 在匹配时，我们可能需要所有的这些特征，不过现在还不需要。所以我们现在提高Hessian 的阈值。
# We set it to some 50000. Remember, it is just for representing in picture.
# In actual cases, it is better to have a value 300-500
surf.hessianThreshold = 50000


# Again compute keypoints and check its number.
kp, des = surf.detectAndCompute(img, None)
print(len(kp))

img2 = cv2.drawKeypoints(img, kp, None, (255, 0, 0), 4)
plt.imshow(img2), plt.show()

# Check upright flag, if it False, set it to True
print(surf.upright)

surf.upright = True
# Recompute the feature points and draw it
kp = surf.detect(img,None)
img2 = cv2.drawKeypoints(img, kp, None, (255, 0, 0), 4)
plt.imshow(img2), plt.show()

# Find size of descriptor
print(surf.descriptorSize())

# That means flag, "extended" is False.
print(surf.extended)

# So we make it to True to get 128-dim descriptors.
surf.extended = True
kp, des = surf.detectAndCompute(img,None)
print(surf.descriptorSize())

print(des.shape)


# 同样是收费项目
