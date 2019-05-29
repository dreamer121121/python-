import os
import imtools
import sift

path = r'./ukbench1000'
imlist = imtools.get_imlist(path)
# nbr_num = len(imlist)
#
# featlist = [imlist[i][:-3]+'sift' for i in range(nbr_num)]
#
#
# #进行sift特征提取
# for i in range(nbr_num):
#     sift.process_image(imlist[i],featlist[i])

import pickle
import  vocabulary

nbr_images = len(imlist)
featlist = [imlist[i][:-3]+'sift' for i in range(nbr_images)]

voc = vocabulary.Vocabulary('ukbenchtest')
voc.train(featlist,1000,10)


#保存词汇
with open('vocabulary.pkl','wb') as f:
    pickle.dump(voc,f) #注意此处的voc是一个对象，我们暂时将其以字符串形式保存在文件中
#以后每当我们需要使用voc的属性时，我们将其从文件中读出来从新实例化变可使用其属性和方法。

print('vocabulary is :',voc.name,voc.nbr_words)
