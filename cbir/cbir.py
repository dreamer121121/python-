import os
import imtools
import sift

path = r'./ukbench1000'
imlist = imtools.get_imlist(path)
# nbr_num = len(imlist)
#
# featlist = [imlist[i][:-3]+'sift' for i in range(nbr_num)]


#第一步：提取图像的SIFT特征
# #进行sift特征提取
# for i in range(nbr_num):
#     sift.process_image(imlist[i],featlist[i])
#---------------------------------------------------------------------



#第二步：建立图像的VOC
# import pickle
# import  vocabulary
#
# nbr_images = len(imlist)
# featlist = [imlist[i][:-3]+'sift' for i in range(nbr_images)]
#
# voc = vocabulary.Vocabulary('ukbenchtest')
# voc.train(featlist,1000,10)
#
#
# #保存词汇
# with open('vocabulary.pkl','wb') as f:
#     pickle.dump(voc,f) #注意此处的voc是一个对象，我们暂时将其以字符串形式保存在文件中
# #以后每当我们需要使用voc的属性时，我们将其从文件中读出来从新实例化变可使用其属性和方法。
#
# print('vocabulary is :',voc.name,voc.nbr_words)
#---------------------------------------------------------------------





#第三步：建立图像数据库，数据库表，并将图像添加入库
# import pickle
# import sift
# import imagesearch
#
# nbr_images = len(imlist)
#
# #载入词汇
# with open('vocabulary.pkl','rb') as f:
#     voc = pickle.load(f)
#
# #创建索引过滤器
# indx = imagesearch.Indexer('test.db',voc)
# indx.create_tables()
#
# for i in range(nbr_images):
#     locs,descr = sift.read_features_from_file(featlist[i])
#     indx.add_to_index(imlist[i],descr)
#
# #提交到数据库
# indx.db_commit()
#
# #下面的代码用于检查数据库中的内容
# import sqlite3 as sqlite
# conn = sqlite.connect('test.db')
# print(conn.execute('select count(filename) from imlist').fetchone())
# print(conn.execute('select * from imlist').fetchone())
# #--------------------------------------------------------------------------------------------------------------------


#第四步：在数据库中搜索图像
import imagesearch
import pickle
with open('vocabulary.pkl','rb') as f:
    voc = pickle.load(f)
src = imagesearch.Searcher('test.db',voc)
print("try a query")
print(src.query(imlist[0])[:10])





