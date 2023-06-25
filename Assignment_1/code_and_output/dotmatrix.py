import cv2 #importing OpenCV
import numpy as np
print("This file converts a number into a dotmatrix representation. dotmatrix.jpg file will be saved in the current file.\n")
img = np.zeros((300, 500), dtype=np.uint8)
N = int(input("Enter Number: "))
n2 = int(N%10)
N/=10
n1 = int(N%10)
on = [[[1,1,1],
       [1,0,1], 
       [1,0,1], 
       [1,0,1], 
       [1,1,1]],
      
    [[0,1,0], 
     [1,1,0], 
     [0,1,0], 
     [0,1,0], 
     [1,1,1]],
      
    [[1,1,1],
     [0,0,1],
     [1,1,1],
     [1,0,0],
     [1,1,1]],
      
    [[1,1,1],
     [0,0,1],
     [1,1,1],
     [0,0,1],
     [1,1,1]],
      
    [[1,0,1],
     [1,0,1],
     [1,1,1],
     [0,0,1],
     [0,0,1]],
      
    [[1,1,1],
     [1,0,0],
     [1,1,1],
     [0,0,1],
     [1,1,1]],
      
    [[1,1,1],
     [1,0,0],
     [1,1,1],
     [1,0,1],
     [1,1,1]],
      
    [[1,1,1],
     [0,0,1],
     [0,0,1],
     [0,0,1],
     [0,0,1]],
      
    [[1,1,1],
     [1,0,1],
     [1,1,1],
     [1,0,1],
     [1,1,1]],
      
    [[1,1,1],
     [1,0,1],
     [1,1,1],
     [0,0,1],
     [1,1,1]]]

x_index = [65, 125, 185, 315, 375, 435]
y_index = [30, 90, 150, 210, 270]

for i in range(5):
    for j in range(3):
        cv2.circle(img=img, center = (x_index[j], y_index[i]), radius = 25, color = (on[n1][i][j]*255, on[n1][i][j]*255, on[n1][i][j]*255) , thickness = -1)

for i in range(5):
    for j in range(3,6):
        cv2.circle(img=img, center = (x_index[j], y_index[i]), radius = 25, color = (on[n2][i][j-3]*255, on[n2][i][j-3]*255, on[n2][i][j-3]*255) , thickness = -1)
# cv2.imshow('asa',img)
# cv2.waitKey(0)
cv2.imwrite('dotmatrix.jpg',img)