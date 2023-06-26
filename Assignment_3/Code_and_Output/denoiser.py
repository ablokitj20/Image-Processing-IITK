"""Code to do bilateral filtering"""
import cv2
import numpy as np
path = input("")

def gaussian(x,sigma):
    return (1.0 / (2 * np.pi * sigma**2)) * np.exp(- (x**2) / (2 * (sigma**2)))

def gaussian1(x,y,sigma):
    return (np.exp(-(x**2 + y**2)/(2*(sigma**2))))/(2*3.14*(sigma**2))

def gaussian_Filter(size, sigma):
    out = np.zeros((size,size))
    for i in range(size):
        for j in range(size):
            out[i,j] = gaussian1(i-size//2,j-size//2, sigma )
    return out/np.sum(out)

def distance(x1,y1,x2,y2):
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def bilateral_fun(img, ksize, sigma1, sigma2):
    out_img = np.zeros((img.shape[0],img.shape[1]))
    img_mod = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    for i in range(ksize//2,img.shape[0]-ksize//2):
        for j in range(ksize//2,img.shape[1]-ksize//2):
            gaussian_i = gaussian(img_mod[i-ksize//2:i+ksize//2+1,j-ksize//2:\
                                          j+ksize//2+1,0] - img_mod[i][j][0]*\
                                  np.ones((ksize,ksize)),sigma1)
            gaussian_s = gaussian_Filter(ksize, sigma2)
            if np.sum(gaussian_i*gaussian_s) !=0:
                out_img[i,j] = np.uint8(round(np.sum(gaussian_i*gaussian_s\
                        *img_mod[i-ksize//2:i+ksize//2+1,j-ksize//2:\
                        j+ksize//2+1,0])/np.sum(gaussian_i*gaussian_s)))
    img_mod[:,:,0] = out_img
    out_img1 = cv2.cvtColor(img_mod, cv2.COLOR_LAB2BGR)
    return out_img1

img = cv2.imread(path)
img = bilateral_fun(img, 9, 20, 7)
bilateral_img = img
cv2.imwrite("denoised.jpg",bilateral_img)