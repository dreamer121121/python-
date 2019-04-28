import warp
from PIL import Image
from pylab import *

im1 = array(Image.open("learn.jpg").convert("L"))
im2 = array(Image.open("book_frontal.jpg").convert("L"))
tp = array([[264,538,540,264],[40,36,605,605],[1,1,1,1]])

im3 = warp.image_in_image(im1,im2,tp)

figure()
gray()
imshow(im3)
axis("equal")
axis("off")
show()