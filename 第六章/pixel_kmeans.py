from scipy.cluster.vq import *
from scipy.misc import imresize
from  PIL import Image
from pylab import *

steps = 50
im = array(Image.open('empire.jpg'))

dx = int(im.shape[0] / steps)
dy = int(im.shape[1] / steps)

features = []
for x in range(steps):
    for y in range(steps):
        print("--x,y--",x,y)
        R = mean(im[x*dx:(x+1)*dx,y*dy:(y+1)*dy,0])
        G = mean(im[x*dx:(x+1)*dx,y*dy:(y+1)*dy,1])
        B = mean(im[x*dx:(x+1)*dx,y*dy:(y+1)*dy,2])
        features.append([R,G,B])

features = array(features,'f')
#聚类
centroids,variance = kmeans(features,3)
code,distance = vq(features,centroids)

#用聚类标记显示图像
codeim = code.reshape(steps,steps)
codeim = imresize(codeim,im.shape[:2],interp='nearest')#对图像进行放大，且采用最近邻插值
codeim = Image.fromarray(uint(codeim)).convert('L') #转换为PIL对象

figure()
imshow(codeim)
codeim.save('clustering.jpg') #此时codeim已经被转换为PIL对象故可以直接使用.save方法
#但还必须转换为convert("L")否则会报错，因为：
#灰度图像在保存时实际上还是以三通道方式进行保存的，只是每一个像素的的三通道
#灰度值是相同的，因此在保存时我们必须指明其类型，若指明为灰度图像故计算机只会开辟1/3的空间存储灰度值

show()



