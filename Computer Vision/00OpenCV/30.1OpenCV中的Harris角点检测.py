import cv2
import numpy as np

filename = './image/chessboard2.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)    # input 必须是float32格式。
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# result is dilated for marking the corners, not important
dst = cv2.dilate(dst, None)  # 膨胀　提升后续图像角点标注的清晰准确度

# Threshold for an optimal value, it may vary depending on the image.
img[dst > 0.09 * dst.max()] = [0, 0, 255]

cv2.imshow('dst', img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
