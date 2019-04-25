import os
import cv2
filenames = [f for f in os.listdir("./") if f.endswith(".jpg")]
dog_imgs = []
for i in range(3):
    for j in range(5):
        temp = cv2.imread(filenames[i*6+j+1],0)-cv2.imread(filenames[i*6+j],0)
        title = "Dog-o-"+str(i)+" s-"+str(j)
        dog_imgs.append(temp)
        cv2.imwrite(title+".jpg",temp)
        cv2.imshow(title,temp)
cv2.waitKey(0)
cv2.destroyAllWindows()
