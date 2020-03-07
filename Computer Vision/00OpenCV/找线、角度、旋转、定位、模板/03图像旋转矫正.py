# 参考文献：https://www.cnblogs.com/skyfsm/p/6902524.html
# 一、思路：
#       1、轮廓提取技术
#       2、霍夫变换知识
#       3、ROI感兴趣区域
# 二、处理步骤
#       1、图片灰度化
#       2、阈值二值化
#       3、检测轮廓
#       4、寻找轮廓的包围矩阵，并且获取角度
#       5、根据角度进行旋转矫正
#       6、对旋转后的图像进行轮廓提取
#       7、对轮廓内的图像区域提取，成为一张独立图像。
# 关键技术就是通过轮廓的最小外接框来获取旋转角度。
# 区分：当得到对象轮廓后，可用https://blog.csdn.net/u013925378/article/details/84563011
#       boundingRect()得到包覆此轮廓的 最小正矩形，https://blog.csdn.net/hjxu2016/article/details/77833984
#       minAreaRect()得到包覆轮廓的 最小斜矩形  !!!!!包含了角度和中心。
import cv2
import numpy as np


srcImg = cv2.imread("./invoice.jpg")
rows, cols, ch = srcImg.shape
gray = cv2.cvtColor(srcImg, cv2.COLOR_BGR2GRAY)
ret, thres = cv2.threshold(gray, 100, 200, cv2.THRESH_BINARY)
# cv2.imshow("thres", thres)
# 第二个参数cv2.RETR_EXTERNAL只检索外框
# contours, hierarchy = cv2.findContours(thres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours, hierarchy = cv2.findContours(thres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 200]
cnt = contours[0]      # 此处选择了最大的轮廓。应该遍历，然后选择面积筛选。确定最大面积轮廓。


rect = cv2.minAreaRect(cnt)
# 返回包覆输入信息的最小斜矩形，是一个Box2D结构rect：（最小外接矩形的中心（x，y），（宽度，高度），旋转角度）
# 详解：https://blog.csdn.net/duiwangxiaomi/article/details/92565308
print(type(rect))
print("rect", rect)
box = cv2.boxPoints(rect)   # 获取四个顶点坐标，这个四个顶点要用来切割图像。
print(box)
box = np.int0(box)    # 框的mask
# frame = cv2.drawContours(srcImg, [box], 0, (0, 0, 255), 2)   # 画出最小外接矩形。
# cv2.imshow("frame", frame)

# 补充长短轴角度问题。
roi = cv2.drawContours(gray, [box], -1, (255, 255, 255), cv2.FILLED)  # cv2.FILLED轮廓填充,
# 第二个参数必须是列表，否则罢工 ：https://blog.csdn.net/u014365862/article/details/77720368
cv2.imshow("roi", roi)
# 新建一个感兴趣的区域图，大小跟原图一样大
mask = np.zeros(srcImg.shape, np.uint8)   # 使用掩模，mask[100:300, 100:400] = 255
masked_img = cv2.add(srcImg, mask, mask=roi)  # mask实现蒙版功能   此处逻辑需要更新一下。
# 成功提取到roi,然后转入到旋转中
cv2.imshow("masked_img", masked_img)

# rect中包含了角度，同时给出了旋转中心,放射变换，实现图像的旋转。
angle = rect[2]
center = rect[0]
print("angle:", angle)
M = cv2.getRotationMatrix2D(center, angle, 1)
dst = cv2.warpAffine(masked_img, M, (cols, rows))   # 此处的列和行必须切换。
# opencv中，是数学中矩阵的方式，先行后列。
cv2.imshow("dst", dst)
# 此时旋转矫正已经完成
# 对矫正图，进行截取roi
gray2 = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
ret2, thres2 = cv2.threshold(gray2, 100, 200, cv2.THRESH_BINARY)
contours2, hierarchy2 = cv2.findContours(thres2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# 截取ROI
x, y, w, h = cv2.boundingRect(contours2[0])
res = dst[y:y+h, x:x+w]
cv2.imshow("res", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
