"""
当数组的大小是 2 的指数时 DFT 效率最高。
当数组的大小是 2，3，5 的倍数时效率也会很高。所以如果你想提高代码的运行效率时，你可以修改输入图像的大小（补 0）。
对于OpenCV 你必须自己手动补 0。但是 Numpy，你只需要指定 FFT 运算的大小，它会自动补 0。

最佳大小:OpenCV 提供了一个函数:cv2.getOptimalDFTSize()。

 OpenCV 的速度是 Numpy 的 3 倍。
"""
import cv2
import numpy as np
import time

img = cv2.imread('./image/girl001.jpg', 0)
rows, cols = img.shape
print(rows, cols)

nrows = cv2.getOptimalDFTSize(rows)
ncols = cv2.getOptimalDFTSize(cols)
print(nrows, ncols)

nimg = np.zeros((nrows, ncols))
nimg[:rows, :cols] = img
if cv2.useOptimized():
    fft1 = np.fft.fft2(img)

    fft2 = np.fft.fft2(img, [nrows, ncols])

    dft1 = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft2 = cv2.dft(np.float32(nimg), flags=cv2.DFT_COMPLEX_OUTPUT)

