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

figure()
imshow(codeim)
show()



