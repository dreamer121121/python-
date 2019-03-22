from PIL import Image
from pylab import *

im = array(Image.open("learn.jpg"))
imshow(im)
print("please click 3 points")
x = ginput(3)#x是一个列表记录点击的坐标。
print("your clicked",x)
show()
