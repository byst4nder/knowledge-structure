import cv2
import numpy as np
from matplotlib import pyplot as plt



# imread（const string& filename, int flags=1）
# flag=-1时，8位深度，原通道
#
# flag=0，8位深度，1通道
#
# flag=1,   8位深度  ，3通道
#
# flag=2，原深度，1通道
#
# flag=3,  原深度，3通道
#
# flag=4，8位深度 ，3通道


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
# img1 = cv2.imread("./image/sk001.jpg", 0)
# img2 = cv2.imread("./image/sk002.jpg", 0)
#
# addImg = cv2.add(img1, img2)  # 饱和运算。
# addWeightImg = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
#
#
# cv2.imshow("img1", img1)
# cv2.imshow("img2", img2)
# cv2.imshow("addImg", addImg)
# cv2.imshow("addWeighted", addWeightImg)


# 按位运算
# img1 = cv2.imread("./image/cat01.jpg")
# img2 = cv2.imread("./image/opencv-logo-white.jpg")
#
# # create a ROI
# rows, cols, channels = img2.shape
# roi = img1[0:rows, 0:cols]
#
# img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
# # threshold() 阈值筛选，第四个坐标为，阈值筛选策略函数。
# mask_inv = cv2.bitwise_not(mask)
# # cv2.bitwise_and()
# # cv2.bitwise_or()
# # cv2.bitwise_xor()
#
#
# # 取ROI中与mask中部位零的值对应的像素的值，其他值为0
# img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
# # 注意这里必须有mask=mask，或者mask=mask_inv,其中的mask=不能忽略。
#
# img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)
#
# dst = cv2.add(img1_bg, img2_fg)
# img1[0:rows, 0:cols] = dst
#
# cv2.imshow("res", img1)
# cv2.imshow("img1_bg ", img1_bg)
# cv2.imshow("img2_fg", img2_fg)


# 14 几何变换：

# # 14.1 resize
# img = cv2.imread("./image/girl001.jpg")
# res1 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
# # 等价
# height, width = img.shape[:2]
# res2 = cv2.resize(img, (2*width, 2*height), interpolation=cv2.INTER_CUBIC)

# 14.2平移
# 先构建移动矩阵：[[1, 0, tx],[0, 1, ty]]

# img = cv2.imread("./image/blue_shorts.jpg")
# rows, cols = img.shape[:2]
#
# M = np.float32([[1, 0, -100], [0, 1, -50]])
# dst = cv2.warpAffine(img, M, (cols-100, rows-50))      # 第三个参数为（宽， 高）opencv要转换。
# 同时可以通过第三参数将平移后的尺寸修改掉。


# 14.3旋转
# img = cv2.imread("./image/girl002.png")
# rows, cols = img.shape[:2]
#
# M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 0.6)
# # 第一个参数：旋转中心， 第二个为旋转角度， 第三个为旋转后缩放因子。
# # 可以通过设置旋转中尉，缩放因子，以及窗口大小来防止旋转后超出边界的问题。
#
# dst = cv2.warpAffine(img, M, (2*cols, 2*rows))
# cv2.imshow("img", dst)

# 14.4 仿射变换
# 原图中所有平行线在结果图像中同样平行。
# S1：需要从原图像中找到三个点以及他们在输出图像中的位置。
# S2：然后cv2.getAffineTransform 会创建一个 2x3 的矩阵，
# S3：最后这个矩阵会被传给函数 cv2.warpAffine。

# img = cv2.imread("./image/girl003.jpg")
# rows, cols, ch = img.shape
#
# pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
# pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
#
# M = cv2.getAffineTransform(pts1, pts2)
# dst = cv2.warpAffine(img, M, (cols, rows))

# plt.subplot(121), plt.imshow(img), plt.title("Input")
# plt.subplot(122), plt.imshow(img), plt.title("Output")
# plt.show()

# 14.5视角变换

# img = cv2.imread("./image/girl003.jpg")
# rows, cols, ch = img.shape
#
# pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
# pts2 = np.float32([[0, 0], [300, 0], [3, 300], [300, 300]])
#
#
# M = cv2.getPerspectiveTransform(pts1, pts2)
# dst = cv2.warpPerspective(img, M, (300, 300))
# plt.subplot(121), plt.imshow(img), plt.title("Input")
# plt.subplot(122), plt.imshow(dst), plt.title("Output")





plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

