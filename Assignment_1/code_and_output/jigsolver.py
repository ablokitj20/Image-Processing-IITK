import cv2 as cv
import numpy as np
import os.path

print("This file converts the given jigsaw image in assignment into the solved image. If there is a file namely jigsaw.jpg in current folder, then it will create an image jigsolved.jpg in current folder. If there is no image as jigsaw.jpg in the current folder then enter the directory / path of the the jigsaw image and then a jigsolved.jpg file will be created on the current folder. \n")

file_exists = os.path.exists('./jigsaw.jpg')
if(file_exists):
    img = cv.imread('./jigsaw.jpg')
else:
    img = str(input("Enter Directory :"))
    img = cv.imread(img)

imglr = np.fliplr(img[150:330, 515:700])
imgud = np.flipud(img[370:,370:])
imgud2 = np.flipud(img[0:410,0:190])

img[150:330, 515:700] = imglr
img[370:,370:] = imgud
img[0:410,0:190] = imgud2

imgud3 = np.flipud(img[210:410,0:190])
img[198:398,0:190] = imgud3

for y in range(198,411):
    for x in range(0,190):
        temp = img[y,x][1]
        img[y,x][1] = img[y,x][0]
        img[y,x][0] = temp

cv.imwrite('./jigsolved.jpg',img)
