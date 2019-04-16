"""
1、cv2.dft()和cv2.idft()输出结果是双通道的：实数部分和虚数部分。
2、输入图像是np.float32格式。
3、LPF（低通滤波）将高频部分去除。其实就是对图像进行模糊操作
4、使用cv2.magnitude计算平方和：将实部和虚部投影到空间域。
cv2.magnitude(x, y) 将sqrt(x^2 + y^2) 计算矩阵维度的平方根
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread("./image/girl001.jpg", 0)

dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
# 使用cv2.magnitude将实部和虚部转换为实部，乘以20是为了使得结果更大
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image1'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum1'), plt.xticks([]), plt.yticks([])
plt.savefig("./image/23.2.1_0OpenCV傅里叶变换.png")
plt.show()


rows, cols = img.shape
crow, ccol = rows//2, cols//2

# create a mask first, center square is 1, remaining all zeros
mask = np.zeros((rows, cols, 2), np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1

# apply mask and inverse DFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image2'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_back, cmap='gray')
plt.title('Magnitude Spectrum2'), plt.xticks([]), plt.yticks([])
plt.show()
