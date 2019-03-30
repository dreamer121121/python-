from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *

im = array(Image.open("learn.jpg").convert("L"))

#sobel导数滤波器
# imx = zeros(im.shape)
# filters.sobel(im,1,imx)
#
# imy = zeros(im.shape)
# filters.sobel(im,0,imy)
#
# magnitude = sqrt(imx**2+imy**2)
#
# imshow(Image.fromarray(imx).convert("L"))
# show()

#高斯导数滤波器（注意与高斯平滑滤波器相比较）
