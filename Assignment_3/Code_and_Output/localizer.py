"""Code to find the place from the location.png"""
import numpy as np
import cv2 as cv
path = input('Enter Your file name: ')
img = cv.imread(path)
a = 0
b2 = 0
c = 0
d = 0
final = 0
i = int(img.shape[0])*int(img.shape[1])
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        b = int(img[y, x][0])
        g = int(img[y, x][1])
        r = int(img[y, x][2])
        a = a + abs(r-g)
        b2 = b2 + abs(r-b)
        c = c + abs(b-g)
        d = d + abs(2*g-b-r)
a_ = a/i
b2_ = b2/i
c_ = c/i
d_ = d/i

distgrass = abs(a_ - 12.14) + abs(b2_ - 21.77) + \
    abs(c_ - 31.30) + abs(d_ - 42.13)
distbuild = abs(a_ - 5.41) + abs(b2_ - 8.74) + abs(c_ - 3.39) + abs(d_ - 3.01)
distroad = abs(a_ - 15.43) + abs(b2_ - 27.31) + \
    abs(c_ - 11.87) + abs(d_ - 4.38)

if distgrass <= distbuild and distbuild <= distroad:
    grass = 3
    build = 1
    road = 0

if distgrass <= distroad and distroad <= distbuild:
    grass = 3
    build = 0
    road = 1

if distroad <= distbuild and distbuild <= distgrass:
    grass = 0
    build = 1
    road = 3

if distroad <= distgrass and distgrass <= distbuild:
    grass = 1
    build = 0
    road = 3

if distbuild <= distgrass and distgrass <= distroad:
    grass = 1
    build = 3
    road = 0

if distbuild <= distroad and distroad <= distgrass:
    grass = 0
    build = 3
    road = 1

if c_ <= 80 and c_ >= 0:
    grass = grass + 1
if d_ <= 85 and d_ >= 12:
    grass = grass + 1

if c_ <= 6 and c_ >= 0:
    build = build + 1
if d_ <= 8 and d_ >= 1:
    build = build + 1

if c_ <= 20 and c_ > 6:
    road = road + 1
if d_ <= 12 and d_ >= 0:
    grass = grass + 1

flag = [grass, road, build]
ans = max(flag)
if (ans == flag[0]):
    print('Location number = 2 \nor the Location is grass')
elif (ans == flag[1]):
    print('Location number = 3 \nor the Location is road')
else:
    print('Location number = 1 \nor the Location is building')
