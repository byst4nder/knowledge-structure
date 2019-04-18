# coding=utf-8
import cv2
import numpy as np

# img_copy = img.copy()   # 防止原图被污染。


# Create a black image
# img = np.zeros((512, 512, 3), np.uint8)

# 画线：
# line1 = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 60)
# cv2.imshow("line", line1)

# 画矩形
# rectangle1 = cv2.rectangle(img, (384, 0,), (510, 128), (0, 255, 0), 3)
# cv2.imshow("rectangle", rectangle1)

# 画圆
# cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)   # -1参数完全填充
# cv2.circle(img, (440, 70), 70, (0, 255, 255), 3)

# 画椭圆
# cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
# cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 360, (128, 128, 128), 4, 1, 0)
#         图像，  中心点， 长短轴，顺时针起始，终止，旋转角度，BGR，线条粗细。 用来设计logo，很方便。

# 画多边形
# pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
# pts = pts.reshape((-1, 1, 2))
# cv2.polylines(img, [pts], True, (0, 255, 255))

# 图片上加字：
# font = cv2.FONT_HERSHEY_SIMPLEX
# # cv2.putText(img, u'我爱你', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)
# cv2.putText(img, "I Love U", (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

# 形状匹配：
img1 = np.zeros((512, 512, 3), np.uint8)
img2 = np.zeros((512, 512, 3), np.uint8)

shape1 = cv2.circle(img1, (128, 128), 72, (32, 64, 255), 2)
shape2 = cv2.circle(img2, (128, 128), 56, (32, 255, 64), 4)

img_gray1 = cv2.cvtColor(shape1, cv2.COLOR_RGB2GRAY)
img_gray2 = cv2.cvtColor(shape2, cv2.COLOR_RGB2GRAY)

contours1, hierarchy1 = cv2.findContours(img_gray1, 2, 1)
contours2, hierarchy2 = cv2.findContours(img_gray2, 2, 1)

# cont1 = cv2.drawContours(shape1, contours1, -1, (0, 255, 0), 3)
cnt1 = contours1[0]
cnt2 = contours2[0]

ret = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
print(ret)

cv2.waitKey(0)
cv2.destroyAllWindows()
