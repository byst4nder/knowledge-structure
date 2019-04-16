# coding:utf-8
'''
1、plt保存文件：plt.savefig("filename.png")
2、高通滤波其实是一种边缘检测操作。
3、图像中的大部分数据集中在频谱图的低频区域。
4、矩形窗口滤波会出现振铃效应，最好用高斯窗口。
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread("./image/girl001.jpg", 0)   # 要求灰度格式
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
# print(fshift.shape)   # (1200, 1920)
magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.savefig("./image/23.1.1_0numpy傅里叶变换.jpg")
plt.show()

# 频域变换:高通滤波和重建图像：（DFT的逆变换）
rows, cols = img.shape

crow, ccol = rows // 2, cols // 2
# fshift[crow-30:crow+30, ccol-30:ccol+30] = 0     # 用60* 60 的框掩模操作，去除低频分量。
fshift[crow-5:crow+5, ccol-5:ccol+5] = 0
f_ishift = np.fft.ifftshift(fshift)     # 逆平移操作，直流分量又回到了左上角。
img_back = np.fft.ifft2(f_ishift)       # FFT逆变换。
img_back = np.abs(img_back)             # 取绝对值.


plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(img_back, cmap='gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(img_back)
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
plt.savefig("./image/23.1.1_1numpy逆傅里叶变换10.jpg")
plt.show()


