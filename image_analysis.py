import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
import cv2 as cv

def process_1d_data():
    minima = 1
    maxima = 16

    def generate_data(x):
        return np.cos(x * 4 - 2 * x - 2) + (x ** 3 + 4 * x - 2) / (x * 2 + x + 2) + np.random.uniform(-1, 1, len(x))

    x_values = np.linspace(minima, maxima, 100)
    filtered_values = gaussian_filter1d(generate_data(x_values), 4)

    plt.plot(x_values, generate_data(x_values))
    
    first_derivative = np.convolve(generate_data(x_values), [1, 0, -1], mode='valid')
    plt.plot(x_values[:98], first_derivative)
    
    second_derivative = np.convolve(generate_data(x_values), [1, -2, 1], mode='valid')
    plt.plot(x_values[:98], second_derivative)

    plt.show()


def process_2d_data():
    is_blurred = False
    image = cv.imread("./img.png")

    cv.imshow("Original", image)

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    if is_blurred:
        gray = cv.GaussianBlur(gray, (3, 3), 20)

    x = cv.Sobel(gray, cv.CV_16S, 1, 0, ksize=3, scale=1, delta=0, borderType=cv.BORDER_DEFAULT)
    y = cv.Sobel(gray, cv.CV_16S, 0, 1, ksize=3, scale=1, delta=0, borderType=cv.BORDER_DEFAULT)

    x = cv.convertScaleAbs(x)
    y = cv.convertScaleAbs(y)

    blended_image = cv.addWeighted(x, 1.4, y, 1.5, 0)

    cv.imshow("1st", blended_image)
    cv.waitKey(0)

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    if is_blurred:
        gray = cv.GaussianBlur(gray, (3, 3), 20)

    x = cv.Sobel(gray, cv.CV_16S, 1, 0, ksize=3, scale=1, delta=0, borderType=cv.BORDER_DEFAULT)
    y = cv.Sobel(gray, cv.CV_16S, 0, 1, ksize=3, scale=1, delta=0, borderType=cv.BORDER_DEFAULT)

    x = cv.convertScaleAbs(x)
    y = cv.convertScaleAbs(y)

    blended_image = cv.addWeighted(x, 0.5, y, 0.5, 0)

    cv.imshow("2nd", blended_image)
    cv.waitKey(0)


if __name__ == "__main__":
    process_1d_data()
    process_2d_data()
