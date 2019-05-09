from . import imtools
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

immatrix = array([array(Image.open(im)).flatten() for im in imlist],'f')


#投影到前40个主成分上
immean = immean.flatten()


