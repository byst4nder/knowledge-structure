import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread("./origin.bmp")
qd = cv2.imread("./quedian.bmp")
# qd = cv2.imread("./abc.bmp")
# qd = cv2.resize(qd, (qd.shape[0]//2, qd.shape[1]//2))
zero = np.zeros(img.shape, dtype=bool)
zero = np.uint8(zero)
# or
# zero = np.zeros(img.shape,np.uint8)
# cv2.imshow("zero", zero)


def kuangxuan(image):
    global zero
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("sn ", image_gray)
    # ret, thresh = cv2.threshold(image_gray, 128, 255, 0)
    # image_gray = cv2.resize(image_gray, (image_gray.shape[0]//2, image_gray.shape[1]//2))
    mask = cv2.bitwise_not(image_gray)
    # cv2.imshow("", mask)
    # cv2.waitKey(0)
    ret, thresh = cv2.threshold(mask, 128, 255, 0)
    # cv2.imshow("sb", thresh)
    # cv2.waitKey(0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, 2)
    # print(contours[:])
    # print(contours)
    # print(contours[0])
    # print(contours[0].shape)
    # contours_shape = np.array(contours).shape
    # print(contours_shape)
    # print(hierarchy)
    # print(hierarchy.shape)
    # im = cv2.drawContours(zero, contours, -1, (0, 255, 0), 3)
    # cv2.imshow("kuang", im)

    # 外接矩形框
    # cnt = contours[0]
    # print(type(cnt))
    # x, y, w, h = cv2.boundingRect(cnt)
    # kuangxuan_img = cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # cv2.imshow("kuangxuan", kuangxuan_img)
    # return image_gray[x:x+w, y:y+h]
    # return kuangxuan_img

    # rect = cv2.minAreaRect(cnt)
    # box = cv2.boxPoints(rect)
    # box = np.int0(box)
    # im = cv2.drawContours(image, [box], 0, (0, 0, 255), 2)
    # return im

    # 极点
    # leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0] for cnt in contours)
    leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0] for cnt in contours)
    # leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
    left = list([b[0]for b in leftmost])
    leftmin = min(left)
    # a = tuple(left[0])
    # left = leftmost[:]
    print(leftmost)
    print(left)
    print(leftmin)
    # print(a)
    rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0] for cnt in contours)
    right = list([b[0]for b in rightmost])
    rightmax = max(right)
    print(rightmax)
    topmost = tuple(cnt[cnt[:, :, 1].argmin()][0] for cnt in contours)
    top = list([b[1]for b in topmost])
    topmax = min(top)
    print(topmax)

    bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0] for cnt in contours)
    bottom = list([b[1]for b in bottommost])
    bottommax = max(bottom)
    print(bottommax)
    # cv2.imshow("", image_gray[ ])
    # ROI = image[56:202, 890:1368]
    # cv2.imshow("aa", ROI)
    # return leftmin, rightmax, topmax, bottommax
    return image[topmax:bottommax, leftmin:rightmax]


img_b = kuangxuan(img)
qd_b = kuangxuan(qd)


cv2.imshow("img_b", img_b)
cv2.imshow("qd_b", qd_b)

# plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

