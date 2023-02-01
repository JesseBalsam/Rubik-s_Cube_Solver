import numpy as np
import matplotlib.cbook as cbook
import matplotlib.image as image
import matplotlib.pyplot as plt
from PIL import Image




# def closest_colour(requested_colour):
#     min_colours = {}
#     for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
#         r_c, g_c, b_c = webcolors.hex_to_rgb(key)
#         rd = (r_c - requested_colour[0]) ** 2
#         gd = (g_c - requested_colour[1]) ** 2
#         bd = (b_c - requested_colour[2]) ** 2
#         min_colours[(rd + gd + bd)] = name
#     return min_colours[min(min_colours.keys())]
#
# def get_colour_name(requested_colour):
#     try:
#         closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
#     except ValueError:
#         closest_name = closest_colour(requested_colour)
#         actual_name = None
#     return closest_name
#
#
#
# im = Image.open('idk_man2.jpg')
# pix = im.load()
# print(im.size)  # Get the width and height of the image for iterating over
# plt.show()
# width = im.size[0]
# height = im.size[1]
#
# requested_colour = (pix[150,150])
# closest_name = get_colour_name(requested_colour)
#
# print(closest_name)
#
#
# side1 = [get_colour_name(pix[width * 1/6,height * 1/6]), get_colour_name(pix[width * 1/2,height * 1/6]), get_colour_name(pix[width * 5/6,height * 1/6]),
#          get_colour_name(pix[width * 1/6,height * 1/2]),get_colour_name(pix[width * 1/2,height * 1/2]), get_colour_name(pix[width * 5/6,height * 1/2]),
#          get_colour_name(pix[width * 1/6,height * 5/6]), get_colour_name(pix[width * 1/2,height * 5/6]), get_colour_name(pix[width * 5/6,height * 5/6])]
#
# print(side1)

# 1/6,1/6 1/2,1/6 5/6,1/6
# 1/6,1/2 1/2,1/2 5/6,1/2
# 1/6,5/6 1/2,5/6 5/6,5/6

# with cbook._get_data_path("idk_man2.jpg") as image_file:
#   image = plt.imread("idk_man2.jpg")
#
# fig, ax = plt.subplots()
# ax.imshow(image)
# ax.axis('on')
#
# im = Image.open('idk_man2.jpg')
# pix = im.load()
# print (im.size)  # Get the width and height of the image for iterating over
# print (pix[0,0])  # Get the RGBA Value of the a pixel of an image
# plt.show()

#nested array
#image of a 3 x 3 array
#divide length by 3
#each section divide 2
#same for width
#get function to get rgb of each 9 points
#create nested list of colors
#get all 4-6 sides
#use swapping method to solve

#needs to know 4 sides and unknown sides cannot be opposite
#frulbd
cube = [['w','g','g','b','g','b','o','o','r'],
 ['y','b','b','r','r','w','g','o','y'],
 ['y','o','y','y','w','y','r','r','r'],
 ['o','g','b','y','o','w','b','o','g'],
 ['r','w','g','r','b','r','b','w','o'],
 ['w','y','w','b','y','g','w','g','o']]


#finish bettercube
#write old pochmann

#cube[r][c]



def swapper(buffer, swap):


def solver(cube):
    edges = [(cube[0][1], cube[1][7]), (cube[0][5], cube[1][3]), (cube[0][7], cube[5][1]), (cube[0][4],
                cube[3][5]), (cube[4][1], cube[2][1]), (cube[4][3], cube[1][5]), (cube[4][7], cube[5][7]), (cube[4][5],
                cube[3][3])]



#helloworld
#hello
#edit code
#click green checkamrk
#edit commit message
#click commit and push
#check in git if item I committed and puches is there
#done