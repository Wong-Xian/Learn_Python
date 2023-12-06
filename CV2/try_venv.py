'''图象傅里叶变换'''
'''2022-7-10 09:00:13'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gray.jpg')    #导图
f = np.fft.fft2(img)            #傅里叶变换
fshift = np.fft.fftshift(f)     #直流分量平移至图象中央

# 这里构建振幅图的公式没学过
magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

plt.show()
