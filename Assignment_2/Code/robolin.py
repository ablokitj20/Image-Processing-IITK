import cv2
import numpy as np
from PIL import Image

def canny_edge_detection(image, sigma=1, low_threshold=50, high_threshold=150):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), sigma)

    # Compute gradients using Sobel operator
    gradient_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
    gradient_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)

    # Compute gradient magnitude and direction
    gradient_magnitude = np.sqrt(gradient_x ** 2 + gradient_y ** 2)
    gradient_direction = np.arctan2(gradient_y, gradient_x)

    # Non-maximum suppression
    suppressed = np.zeros_like(gradient_magnitude)
    angle_quantization = np.round(gradient_direction / (np.pi / 4)) % 4
    for i in range(1, gradient_magnitude.shape[0] - 1):
        for j in range(1, gradient_magnitude.shape[1] - 1):
            mask = np.zeros(8, dtype=bool)
            mask[angle_quantization[i, j]] = True
            if (gradient_magnitude[i, j] > gradient_magnitude[i + 1, j] and
                gradient_magnitude[i, j] > gradient_magnitude[i - 1, j] and
                gradient_magnitude[i, j] > gradient_magnitude[i, j + 1] and
                gradient_magnitude[i, j] > gradient_magnitude[i, j - 1] and
                gradient_magnitude[i, j] > gradient_magnitude[i + 1, j + 1] and
                gradient_magnitude[i, j] > gradient_magnitude[i - 1, j - 1] and
                gradient_magnitude[i, j] > gradient_magnitude[i + 1, j - 1] and
                gradient_magnitude[i, j] > gradient_magnitude[i - 1, j + 1]):
                suppressed[i, j] = gradient_magnitude[i, j]

    # Double thresholding and edge tracking
    thresholded = np.zeros_like(suppressed)
    thresholded[suppressed >= high_threshold] = 255
    strong_i, strong_j = np.where(suppressed >= high_threshold)
    weak_i, weak_j = np.where((suppressed >= low_threshold) & (suppressed < high_threshold))

    # Edge tracking using hysteresis
    for i, j in zip(strong_i, strong_j):
        thresholded[i, j] = 255
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1),
                       (1, 1), (-1, -1), (-1, 1), (1, -1)):
            ai, aj = i + di, j + dj
            if thresholded[ai, aj] == 0 and suppressed[ai, aj] >= low_threshold:
                thresholded[ai, aj] = 255

    return thresholded.astype(np.uint8)


# Example usage
path = input("Enter the path to the image: ")
image = cv2.imread(path)

edge = canny_edge_detection(image, sigma=1, low_threshold=50, high_threshold=150)

name = "robolin-" + path
final = Image.fromarray(edge)
final.save(name)
