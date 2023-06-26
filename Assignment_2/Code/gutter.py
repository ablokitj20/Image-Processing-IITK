import cv2 as cv
import numpy as np
from PIL import Image
path = input('')
norm_img = cv.imread(path,0)

# norm_img = img # Needed for 3.x compatibility
# cv.normalize(img, norm_img, alpha=0, beta=255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8UC1)
dilated_img = cv.dilate(norm_img, np.ones((7,7), np.uint8))
bg_img = cv.medianBlur(dilated_img, 21)
diff_img = 255 - cv.absdiff(norm_img, bg_img)
norm_img2 = cv.normalize(diff_img,None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8UC1)
final = Image.fromarray(norm_img2)
def normalize(img):
    lmin = float(img.min())
    lmax = float(img.max())
    return np.floor((img - lmin)/(lmax - lmin)*255.00)
# cv.imwrite('./cleaned-gutter.jpg./',norm_img)
final.save('cleaned-gutter.jpg')
