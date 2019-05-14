import imtools
import pickle
from scipy.cluster.vq import *
from pylab import *
from PIL import Image

path = r'C:\Users\dreamer\Desktop\reposite\python计算机视觉\data\selectedfontimages\a_selected_thumbs'
imlist = imtools.get_imlist(path)
imbr = len(imlist)


with open('a_pca_modes.pkl','rb') as f:
    immean = pickle.load(f)
    V = pickle.load(f)

#创建图像矩阵每一行为一幅图像，共66个图像即66行
immatrix = array([array(Image.open(im)).flatten() for im in imlist],'f')


# #投影到前40个主成分上
immean = immean.flatten()
projected = array([dot(V[:40],immatrix[i]-immean) for i in range(imbr)])

#进行K-means聚类
projected = whiten(projected)
centroids,distortion = kmeans(projected,4)
code,distance = vq(projected,centroids)


#绘制聚类族
for k in range(4):
    ind = where(code==k)[0]#返回的是索引
    figure()
    gray()
    for i in range(minimum(len(ind),40)):
        subplot(4,10,i+1)
        imshow(immatrix[ind[i]].reshape((25,25)))
        axis('off')
    show()





