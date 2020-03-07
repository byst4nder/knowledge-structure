# 1、直角坐标系下的每条直线，在极坐标系下都通过通过一个点(ρ,θ)，因此对于每个点(x,y)进行极坐标换算。
# 2、设置一个累加器：每当同一条直线上的点，映射到极坐标系下的点时，这个点就累加一。
# 3、设置阈值。阈值达到标准视为一条直线。所以lines返回的是两个值：距离，角度。
# 但是衡量直线的个数通过len(lines)
import cv2
import numpy as np


img = cv2.imread("line2.bmp")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

print(lines.shape)
print(type(lines))
print(lines)
print(len(lines))
print(lines[0])
print(lines.tolist())
for rho, theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*a)
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*a)

    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow("result", img)
cv2.waitKey(10000)
cv2.destroyAllWindows()

# if __name__ == '__main__':
#     main()
