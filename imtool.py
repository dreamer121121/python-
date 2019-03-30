from PIL import Image
from pylab import *



#直方图均衡
def histeq(im,nbr_bins=256):
    """
    此函数用于图像直方图均衡，输入参数
    im:数组形式的灰度图像
    nbr_bins:直方图中使用小区间的个数
    :param im:
    :param nbr_bins:
    :return:
    """
    imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)
    cdf = imhist.cumsum()
    cdf = 255 *cdf / cdf[-1] #归一化
    im2 = interp(im.flatten(),bins[:-1],cdf) #线性插值
    return im2.reshape(im.shape),cdf

#图像平均
def compute_average(imlist):
    """
    此图像用于计算图像列表的平均图像
    :param imlist:
    :return:
    """
    #打开第一幅图像
    averageim = array(Image.open(imlist[0]),'f')
    for imname in imlist[1:]:
        try:
            averageim += array(Image.open(imname))
        except:
            print(imname + "...skiped")
    averageim /= len(imlist)
    return array(averageim,'uint8')

#图像PCA

def pca(X):

    """
    此函数用于主成分分析
    :param X: 存储训练数据，每一行为一条训练数据
    :return: 投影矩阵，方差，均值。
    """

    #获取维数
    num_data,dim = X.shape

    #数据中心化
    mean_X = X.mean(axis=0)
    X -= mean_X

    if dim > num_data:
        #PCA-使用紧致技巧
        M = dot(X,X.T)#协方差矩阵:dot()主要实质就是进行矩阵乘法。

        """
        此处可能存在问题，由原书中介绍每一行代表一个一张图片，即（每一行代表一个observation(sample))
        计算协方差矩阵时应当是X.T*X而并非是X*X.T
        详情可参考博文：360浏览器收藏夹/数学/
        https://blog.csdn.net/u013555719/article/details/82628835
        """

        e,EV = linalg.eigh(M)#计算特征值特征向量。
        temp = dot(X.T,EV).T #紧致技巧
        V = temp[::-1] #对特征向量矩阵进行逆转,类似于a.reverser()但是reverse会改变自身。
        S = sqrt(e)[::-1] #对特征值按逆向排列
        for i in range(V.shape[1]):
            V[:,i] /= S
    else:
        #使用SVD 方法
        U,S,V = linalg.svd(X)
        V = V[:num_data]

    return V,S,mean_X











