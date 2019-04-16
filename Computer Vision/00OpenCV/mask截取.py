import cv2
import numpy as np


img = cv2.imread("./image/blue_shorts.jpg")
roi_mask = cv2.imread("./image/roi_mask.jpg", 0)
kernel = np.ones((5, 5), np.uint8)
opening = cv2.morphologyEx(roi_mask, cv2.MORPH_OPEN, kernel)
# blur = cv2.GaussianBlur(roi_mask, (9, 9), 0)

roi = cv2.bitwise_and(img, img, mask=opening)
img = img[:roi_mask.shape[0], :roi_mask.shape[1]] = roi

cv2.imshow("roi", roi)
cv2.imshow("img", img)
cv2.imwrite("./image/roi.jpg", roi)


# 创造掩模方法
# img = cv2.imread("./image/blue_shorts.jpg", 0)
# mask = np.zeros(img.shape[:2], np.uint8)

# mask[100:286, 285:465] = 255
# masked_img = cv2.bitwise_and(img, img, mask=mask)

# img1 = cv2.imread("./image/blue_shorts.jpg")
# roi = img1[100:286, 285:465, :]
# cv2.imshow("roi", roi)

# cv2.imshow("mask", mask)
# cv2.imshow("masked_img", masked_img)


cv2.waitKey(0)
cv2.destroyAllWindows()
