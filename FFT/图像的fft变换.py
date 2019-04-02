import cv2
import numpy as np
from PIL import Image
from pylab import *
img1= array(Image.open("../learn.jpg").convert("L"))
f=np.fft.fft2(img1)
fshift=np.fft.fftshift(f)
#之所以要进行对数转换是因为傅里叶变换后的结果对于在显示器显示来讲范围比较大，这样的话对于一些小的变化或者是高的变换值不能进行观察
magnitude_spectrum=20*np.log(np.abs(fshift))

figure(1)
imshow(Image.fromarray(img1))

figure(2)
imshow(Image.fromarray(magnitude_spectrum).convert("L"))
show()

