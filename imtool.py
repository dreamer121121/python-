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



