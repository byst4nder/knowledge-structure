import cv2
import numpy as np

img = cv2.imread('flash.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]

epsilon = 0.0005*cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)
cv2.polylines(img, [approx], True, (0, 0, 255), 2)

res = cv2.matchShapes(cnt, cnt, 3, 0.0)
print(res)
cv2.imshow("polylines", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
