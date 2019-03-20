from PIL import Image
from pylab import *

#读取图像到数组
im = array(Image.open("learn.jpg").convert('L'))
#图像在内存中是以灰度矩阵的方式存在的
print("---type---",type(im))
print("---shape---",im.shape)
#新建一个图像
figure()

#不使用颜色信息
gray()

#在远点的左上角显示轮廓
contour(im,origin='image')
axis('equal')
axis('off')

figure()
hist(im.flatten(),128)# 第一个参数必须是一维数组，第二个参数是直方图小方块的个数。
show()