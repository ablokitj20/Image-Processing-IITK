import cv2
import numpy as np
from PIL import Image
path = input('')
img = cv2.imread(path, 0)
res = cv2.equalizeHist(img)

def createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)):
    def clahe_apply(image):
        # Calculate the size of each tile
        tile_height = int(np.ceil(image.shape[0] / tileGridSize[0]))
        tile_width = int(np.ceil(image.shape[1] / tileGridSize[1]))

        # Initialize the output image
        output = np.zeros_like(image, dtype=np.uint8)

        # Apply CLAHE on each tile
        for i in range(tileGridSize[0]):
            for j in range(tileGridSize[1]):
                # Define the boundaries of the current tile
                y_start = i * tile_height
                y_end = min((i + 1) * tile_height, image.shape[0])
                x_start = j * tile_width
                x_end = min((j + 1) * tile_width, image.shape[1])

                # Extract the current tile
                tile = image[y_start:y_end, x_start:x_end]

                # Calculate the histogram of the tile
                hist, _ = np.histogram(tile.flatten(), bins=256, range=[0, 256])

                # Clip the histogram based on the specified clipLimit
                clipped_hist = np.clip(hist, 0, int(clipLimit * tile.size / 256))

                # Calculate the cumulative distribution function (CDF) of the clipped histogram
                cdf = clipped_hist.cumsum()

                # Normalize the CDF
                cdf = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())

                # Interpolate the pixel values using the normalized CDF
                tile_equalized = np.interp(tile.flatten(), np.arange(0, 256), cdf).reshape(tile.shape)

                # Assign the equalized tile to the corresponding location in the output image
                output[y_start:y_end, x_start:x_end] = tile_equalized

        return output

    return clahe_apply


clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
name = "enhanced-"+path
# cv2.imwrite('ww.jpg',cl1)
final = Image.fromarray(cl1)
final.save(name)