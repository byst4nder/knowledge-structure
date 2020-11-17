import cv2
import numpy as np

filename = 'chessboard.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)    # input 必须是float32格式。
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# result is dilated for marking the corners, not important
dst = cv2.dilate(dst, None)  # 膨胀　提升后续图像角点标注的清晰准确度
cv2.imshow('dst1', dst)

# Threshold for an optimal value, it may vary depending on the image.
img[dst > 0.09 * dst.max()] = [0, 0, 255]
# 将所有的dst设置一个阈值过滤并标注。BGR。

cv2.imshow('dst', img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()


#     • img - 数据类型为 float32 的输入图像。
# 　　• blockSize - 角点检测中要考虑的领域大小。
# 　　• ksize - Sobel 求导中使用的窗口大小
# 　　• k - Harris 角点检测方程中的自由参数，取值参数为 [0,04，0.06].
