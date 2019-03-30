from imtool import *
from pylab import mpl
import os
import matplotlib.pyplot as plt


mpl.rcParams['font.sans-serif'] = ['SimHei']#设置字体

im = array(Image.open("learn.jpg").convert("L"))

#进行直方图均衡h化
im2,cdf = histeq(im)
print("")

figure(1)
im = Image.fromarray(im)
im.save("原始图像.jpg")
title("原始图像")

figure(2)
hist1 = hist(array(im).flatten(),256)
plt.savefig("./原始图像直方图.jpg")
plt.close()
title("原始图像直方图")


figure(3)
im2 = np.trunc(im2)
im2 = Image.fromarray(im2).convert("L") #此处必须将PIL对象进行灰度转换

#原因：im2本身是一个800x800的矩阵，因此只能表示灰度图像，但真正的灰度图像
#实际上也是以三通道方式存储，只是三通道的值是相同的，此处进行convert("L")
#相当于告诉PIL我们要将im2存储成灰度图像，只需在硬盘中开辟8bit空间即可
#https://stackoverflow.com/questions/16720682/pil-cannot-write-mode-f-to-jpeg


im2.save("直方图均衡后的图像.jpg")
title("直方图均衡后的图像")


figure(4)
hist2 = hist(array(im2).flatten(),256)
title("均衡后的直方图")
plt.savefig("均衡后的直方图.jpg")
plt.close()





