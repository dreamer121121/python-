from PIL import Image
from scipy.ndimage import filters
from pylab import *

# im = array(Image.open("learn.jpg").convert("L"))
# im2 = filters.gaussian_filter(im,7)
#
# figure(1)
# imshow(Image.fromarray(im))
#
# figure(2)
# im2 = Image.fromarray(im2)
# imshow(im2)
#
# show()

im = array(Image.open("learn.jpg"))
im2 = zeros(im.shape)

for i in range(3):
    #彩色图像进行高斯滤波，相当于对每一个通道进行高斯滤波。
    im2[:,:,i] = filters.gaussian_filter(im[:,:,i],5)
im2 = array(im2,'uint8')

figure(1)
im = Image.fromarray(im)
imshow(im)

figure(2)
im2 = Image.fromarray(im2)
imshow(im2)

show()
