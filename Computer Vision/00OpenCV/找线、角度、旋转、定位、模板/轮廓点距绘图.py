# 参考：https://blog.csdn.net/kakiebu/article/details/81983714
import cv2
import numpy as np


# 读取图像，解决imread不能读取中文路径的问题
def cv_imread(file_path):
    cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
    return cv_img


img = cv_imread("枫叶.jpg")
# img = cv2.imread(r"枫叶.jpg")  # 会报错。
high, width = img.shape[:2]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thres = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(thres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnt = contours[0]

img_c = img.copy()
cv2.drawContours(img_c, [cnt], 0, (0, 0, 255), thickness=2)

# mask = np.zeros(gray.shape, np.uint8)
# np.uint8代表无符号八位整型：范围[0, 255],所以这一句导致中间为黑色。
mask = np.empty((high, width))
# dist = cv2.pointPolygonTest(cnt, (50, 50), True)
for i in range(high):    # i行
    for j in range(width):   # j列
        distance = cv2.pointPolygonTest(cnt, (j, i), True)
        # mask[j][i] = abs(distance)
        mask[i][j] = distance
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(mask)
print(min_val, max_val, min_loc, max_loc)
# m_loc = cv2.circle(img, min_loc, 7, (0, 255, 0), 2)
# M_loc = cv2.circle(img_c, max_loc, 7, (255, 0, 0), 2)
# cv2.imshow("locations_m", m_loc)
# cv2.imshow("locations_M", M_loc)
# 距离热力图：
hot_map = np.zeros((high, width, 3), np.uint8)   # 重构图。此处选用zeros()。
for i in range(high):
    for j in range(width):
        # distance = cv2.pointPolygonTest(cnt, (j, i), True)
        distance = mask[i][j]   # 重新计算浪费时间。调取第一次的用。
        if distance > 1:
            hot_map[i][j][0] = int(abs(distance/max_val) * 255)
        elif distance < -1:
            hot_map[i][j][2] = int(abs(distance/min_val) * 255)
            # print(hot_map[i][j][2])
        else:
            hot_map[i][j][0] = int(abs(255 - distance))
            hot_map[i][j][1] = int(abs(255 - distance))
            hot_map[i][j][2] = int(abs(255 - distance))
        print("\r[%d][%d]修改完成。。。" % (i, j), end="")


# 保存中文路径。
# cv2.imencode('.jpg', thres)[1].tofile("枫叶白图.jpg")
# cv2.imshow("mask", mask)
# cv2.imshow("img_c", img_c)
cv2.imshow("hot-map", hot_map)
# cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 轮廓点距绘制热力图。
# 进度条print("\r")
