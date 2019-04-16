import cv2

img = cv2.imread("./image/ska07_01.jpg")

Color_Space = []
for i in dir(cv2):
    if i.startswith("COLOR_"):
        color = str("cv2.") + i
        Color_Space.append(color)
# print(len(Color_Space))
print(Color_Space[5])

for color in Color_Space[:5]:
    method = eval(color)
    print(method)
    dst = cv2.cvtColor(img, method)
    cv2.imshow(color, dst)

    cv2.waitKey(0)
cv2.destroyAllWindows()
