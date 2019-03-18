import cv2
import numpy as np
import sys

Apple = cv2.imread("./image/apple01.jpg")
Orange = cv2.imread("./image/orange.jpg")

A = Apple
# B = Orange[:, 156:868]
# 因为都是白板的，可以通过画图来将图像底板拉伸拓展。大小做到2^N。始终保持，缩放尺寸统一，防止四舍五入的小数。

height, width = A.shape[:2]
B = cv2.resize(Orange, (width, height))
# A = A[50:, :]
# B = B[50:, :]

# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in range(5, 0, -1):
    GE = cv2.pyrUp(gpA[i])
    L = cv2.subtract(gpA[i-1], GE)
    lpA.append(L)

# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in range(5, 0, -1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1], GE)
    lpB.append(L)

# Now add left and right halves of images in each level
LS = []
for la, lb in zip(lpA, lpB):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:, 0: int(cols/2)], lb[:, int(cols/2):]))  # 此处要用int转成整数，否则报错。
    LS.append(ls)

# now reconstruct
ls_ = LS[0]
for i in range(1, 6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])

# image with direct connecting each half
# real = np.hstack((A[:, :cols/2], B[:, cols/2:]))
real = np.hstack((A[:, :int(cols/2)], B[:, int(cols/2):]))
# np.hstack() 矩阵图像的拼接函数，非常需要的东西，老鼠书上的知识点要好好看看。

cv2.imwrite('Pyramid_blending2.jpg', ls_)
cv2.imwrite('Direct_blending.jpg', real)
cv2.imshow("Pyramid_blending2", ls_)
cv2.imshow("Direct_blending", real)
cv2.waitKey(0)
cv2.destroyAllWindows()
