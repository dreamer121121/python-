#coding:utf-8
import cv2 as cv

#高斯金字塔
# def pyramid_image(image):
#     level = 3#金字塔的层数
#     temp = image.copy()#拷贝图像
#     pyramid_images = []
#     for i in range(level):
#         dst = cv.pyrDown(temp)
#         pyramid_images.append(dst)
#         cv.imshow("高斯金字塔"+str(i), dst)
#         temp = dst.copy()
#     return pyramid_images


def Gaussian_pyramid(img):
    sigma0 = 1.6
    S = 3
    k = pow(2, 1 / 3)
    level = 3
    img_copy = img.copy()
    pyramid_imgs = []
    O_imgs = []
    for o in range(level):

        if not pyramid_imgs:
            first_img_o = img_copy
        else:
            first_img_o = cv.pyrDown(O_imgs[-3])
        O_imgs = []
        for s in range(S+3):
            sigma = sigma0*pow(2,o)*pow(k,s)#计算尺度
            print("o--"+str(o)+" "+"s--"+str(s)+"--sigma："+str(sigma))
            if s == 0:
                blured = cv.GaussianBlur(first_img_o, ksize=(0,0),sigmaX=sigma, sigmaY=sigma)
            else:
                blured = cv.GaussianBlur(O_imgs[-1],ksize=(0,0),sigmaX=sigma,sigmaY=sigma)

            O_imgs.append(blured)

        pyramid_imgs.append(O_imgs)
    return pyramid_imgs


def show_pyramids_and_save(img_list):
    for i in range(len(img_list)):
        for j in range(len(img_list[i])):
            title = "o-"+str(i)+" "+"s-"+str(j)
            cv.imshow(title,img_list[i][j])
            cv.imwrite(title+".jpg",img_list[i][j])

def preprocess(filepath):
    src = cv.imread(filepath)
    img = cv.resize(src,dsize=(512,512))
    return img

if __name__ == "__main__":

    filepath = "./learn.jpg"
    src = preprocess(filepath)
    pyramid_imgs = Gaussian_pyramid(src)
    show_pyramids_and_save(pyramid_imgs)
    cv.waitKey(0)
    cv.destroyAllWindows()

