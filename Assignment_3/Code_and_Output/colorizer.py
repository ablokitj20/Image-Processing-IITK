"""Generating image from Y Cb and Cr"""
import numpy as np
import cv2 as cv
x, y, z = input("").split()
cb4 = cv.imread(y)
cr4 = cv.imread(z)
Y = cv.imread(x)
w = Y.shape[1]
h = Y.shape[0]
points = (w,h)
cr4_= cv.resize(cr4, points, interpolation= cv.INTER_LINEAR)
cb4_= cv.resize(cb4, points, interpolation= cv.INTER_LINEAR)
img2 = Y.copy()
for y in range(cr4_.shape[0]):
    for x in range(cr4_.shape[1]):
        a = Y[y,x][0]
        b = cb4_[y,x][0]
        c = cr4_[y,x][0]
        r = a + 1.402525*(c-128)
        g = a - 0.343730*(b-128) - 0.714401*(c-128)
        b2 = a + 1.769905*(b-128) + 0.000013*(c-128)
        img2[y,x][0] = b2
        img2[y,x][1] = g
        img2[y,x][2] = r
cv.imwrite("flyingelephant.jpg",img2)