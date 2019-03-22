from PIL import Image
from numpy import  *
from pylab import *
import cv2

figure()
im = array(Image.open("learn.jpg").convert('L'))
imshow(im)#这样显示一张灰度图像会出现问题！！！！！

figure()
imshow(Image.fromarray(uint8(im)))


figure()
#反变换
im2 = 255-im
imshow(Image.fromarray(im2))

figure()
#像素值变换到100-200之间
im3 = (100/255)*im+100
imshow(Image.fromarray(im3))

figure()
#对象素值求平方后得到的图像
im4 = 255*(im/255)**2
imshow(Image.fromarray(im4))

show()
