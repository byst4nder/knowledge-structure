# 第一章 基于边缘轮廓的矫正

![invoice.jpg](https://wx3.sinaimg.cn/mw690/005Q1p9vgy1gc9hfz34spj30pe0f775z.jpg)

处理流程-步骤总结：

1. 图像灰度化
2. 阈值二值化
3. 检测轮廓   [cv2.findContours()]()
4. 寻找轮廓的包围矩阵，并且获取角度[cv2.minAreaRect(cnt)]()
5. 根据角度进行旋转矫正 [仿射变换]()
6. 旋转后的轮廓提取
7. ROI截取   [mask蒙版]() | [cv2.boundingRect(cnt)]()

> 
> 关键技术就是通过**轮廓的最小外接框minAreaRect()**来获取旋转角度。
> 

以上步骤只针对此图，必要时增加膨胀、腐蚀、开闭运算等形态学变化，去掉背景(前景提取)等。