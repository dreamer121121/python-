from PIL import Image
from pylab import *
import os.path
def get_imglist(path):
    #注意列表解析式的用法
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

def convert_to_jpg(img_list):
    for img_file in img_list:
        outfile = os.path.splitext(img_file)[0]+'.jpg'
        if img_file != outfile:
            Image.open(img_file).save(outfile)
        else:
            print("convet"+img_file+"failed")
#创建缩略图
def create_thum(img):
    img.thumbnail((128,128)) #对自身进行操作
    img.save("thum.jpg")

path = r'C:\Users\dreamer\Desktop\opencv-learn\images'
img = Image.open(path+'\learn.jpg')
# create_thum(img)
#图像的复制和粘贴和剪切指定区域
box = (0,0,400,400)
region = img.crop(box)
s = region.transpose(Image.ROTATE_180).save("rotate_180.jpg")
img.paste(s,(0,0,400,400)).save("paste.jpg")


