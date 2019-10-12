import cv2
import inspect
import numpy as np


img = cv2.imread("1.jpg")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_copy = img.copy()

# contours, hierarchy = cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours, hierarchy = cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 200]
print('len(contours)', len(contours))

cnt = contours[0]
M = cv2.moments(cnt)
print(M)



# 区域框
x, y, w, h = cv2.boundingRect(cnt)
img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 5)
# 最小外接矩形框
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
img = cv2.drawContours(img, [box], 0, (0, 0, 255), 5)

# 方向是物体定向的角度，最小外接框的角度。
(x_, y_), (MA, ma), angle = cv2.fitEllipse(cnt)
print((x_, y_), (MA, ma), angle)

cv2.imshow("result", img)

# # 近似轮廓
# contours2, hierarchy2 = cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# for cnt2 in contours2:
#     epsilon = 0.5*cv2.arcLength(cnt2, True)
#     approx = cv2.approxPolyDP(cnt2, epsilon, True)
#
#     # res = cv2.drawContours(img_copy, approx, -1, (0, 0, 255), 3)
#     res = cv2.polylines(img_copy, [approx], True, (0, 0, 255), 2)

approx = cv2.approxPolyDP(cnt, 24, True)
res = cv2.polylines(img_copy, [approx], True, (0, 0, 255), 2)

cv2.imshow("res", res)

cv2.waitKey()
cv2.destroyAllWindows()


# 图像过大时，可以使用。
def resize_show(image_name):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    window_name = [var_name for var_name, var_val in callers_local_vars if var_val is image_name][0]
    cv2.namedWindow(window_name, 0)
    cv2.resizeWindow(window_name, (int(image_name.shape[0]/2), int(image_name.shape[1]/2)))
    cv2.imshow(window_name, image_name)
