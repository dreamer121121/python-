from PIL import Image
from numpy import *


def pca(X):
    """    Principal Component Analysis
        input: X, matrix with training data stored as flattened arrays in rows
        return: projection matrix (with important dimensions first), variance and mean.
    """
    
    # get dimensions
    num_data,dim = X.shape

    print("---X---",X.shape)
    # center data
    mean_X = X.mean(axis=0)
    X = X - mean_X


    M = dot(X.T,X) # covariance matrix
    print("---协方差矩阵---",M.shape)
    e,EV = linalg.eigh(M) # eigenvalues and eigenvectors
    print("---e---",e.shape)
    print("--e---",e)
    print("--EV--",EV.shape)
    # tmp = dot(X.T,EV).T # this is the compact trick
    # print("--tmp--",tmp.shape)
    V = EV # reverse since last eigenvectors are the ones we want
    S = sqrt(e)[::-1] # reverse since eigenvalues are in increasing order

    # if dim>num_data:
        # PCA - compact trick used
    # M = dot(X.T,X) # covariance matrix
    # print("---协方差矩阵---",M.shape)
    # e,EV = linalg.eigh(M) # eigenvalues and eigenvectors
    # print("---e---",e.shape)
    # print("--EV--",EV.shape)
    # tmp = dot(X.T,EV).T # this is the compact trick
    # print("--tmp--",tmp.shape)
    # V = tmp[::-1] # reverse since last eigenvectors are the ones we want
    # S = sqrt(e)[::-1] # reverse since eigenvalues are in increasing order
    # for i in range(V.shape[1]):
    #     V[:,i] /= S
    # else:
    #     print("---SVD---")
    #     # PCA - SVD used
    #     U,S,V = linalg.svd(X) #进行SVD分解
    #     print("---S.shape--",S.shape)
    #     print("---V.shape--",V.shape)
    #     print("---U.shape--",U.shape)
    #     V = V[:num_data] # only makes sense to return the first num_data
    #
    # return the projection matrix, the variance and the mean
    return V,S,mean_X


def center(X):
    """    Center the square matrix X (subtract col and row means). """
    
    n,m = X.shape
    if n != m:
        raise Exception('Matrix is not square.')
    
    colsum = X.sum(axis=0) / n
    rowsum = X.sum(axis=1) / n
    totalsum = X.sum() / (n**2)
    
    #center
    Y = array([[ X[i,j]-rowsum[i]-colsum[j]+totalsum for i in range(n) ] for j in range(n)])
    
    return Y


from PIL import Image
from numpy import *
from pylab import *
import os

def read_file():
    path = r'C:\Users\dreamer\Desktop\reposite\python计算机视觉\data\fontimages\a_thumbs'
    ims = [os.path.join(path,f) for f in os.listdir(path) if f.endswith(".jpg")]
    return ims

imlist = read_file()
im = array(Image.open(imlist[0]))
m,n = im.shape[0:2]
imnbr = len(imlist)

#创建矩阵，保存所有压平后的图像数据
immatrix = array([array(Image.open(im)).flatten() for im in imlist],'f')

#执行PCA
V,S,immean = pca(immatrix)

#显示图像
figure()
gray()
subplot(2,4,1)
imshow(immean.reshape(m,n))
for i in range(7):
    subplot(2,4,i+2)
    imshow(V[i].reshape(m,n))
show()
