from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *

im = array(Image.open("empire.jpg").convert("L"))
#sobel导数滤波器
# imx = zeros(im.shape)
# filters.sobel(im,1,imx)
#
# imy = zeros(im.shape)
# filters.sobel(im,0,imy)
#
# magnitude = sqrt(imx**2+imy**2)
#
# imshow(Image.fromarray(magnitude).convert("L"))
# show()

#高斯导数滤波器（注意与高斯平滑滤波器相比较）

sigma = 2
imx = zeros(im.shape)
imx = filters.gaussian_filter(im,(sigma,sigma),(0,1),output=imx)

imy = zeros(im.shape)
imy = filters.gaussian_filter(im,(sigma,sigma),(1,0),output=imy)

magnitude = sqrt(imx**2+imy**2)
imshow(Image.fromarray(uint8(magnitude)))
show()

