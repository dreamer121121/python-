from PIL import Image
from pylab import * #pylab是pyplot和numpy的结合体

#读取图像到数组
im = array(Image.open("learn.jpg"))

#绘制图像
imshow(im)

#一些点
x = [100,100,400,400]
y = [200,500,200,500]

#使用红色星状标记绘制点
plot(x,y,'s--')


#绘制连接前两个点的线
# plot(x,y)

show()#用于真正显示图像。
