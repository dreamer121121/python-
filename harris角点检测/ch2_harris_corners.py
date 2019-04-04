from pylab import *
from numpy import *
from PIL import Image
import harris

"""
Example of detecting Harris corner points (Figure 2-1 in the book).
"""

# open image
im = array(Image.open('./empire.jpg').convert('L'))

# detect corners and plot

#上面返回的是图像中每一个像素点的harris值所组成的矩阵
harrisim = harris.compute_harris_response(im)

filtered_coords = harris.get_harris_points(harrisim, 10, threshold=0.01)
harris.plot_harris_points(im, filtered_coords)


# plot only 200 strongest
harris.plot_harris_points(im, filtered_coords[:100])