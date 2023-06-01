import numpy as np
import cv2
import matplotlib.pyplot as plt

def read_resize_image(image_path, width, height):
    img = cv2.imread(image_path, 0)
    img = cv2.resize(img, (width, height))
    return img

def apply_laplacian(image):
    lap = cv2.Laplacian(image, cv2.CV_64F, ksize=1)
    lap = np.uint8(np.abs(lap))
    return lap

def apply_sobel(image):
    sobx = cv2.Sobel(image, cv2.CV_64F, dx=1, dy=0)
    sobx = np.uint8(np.abs(sobx))

    soby = cv2.Sobel(image, cv2.CV_64F, dx=0, dy=1)
    soby = np.uint8(np.abs(soby))

    sob = cv2.bitwise_or(sobx, soby)
    return sob

def display_images(images, titles):
    for i in range(len(images)):
        plt.subplot(2, 3, i + 1)
        plt.imshow(images[i], 'gray')
        plt.xticks([])
        plt.yticks([])
        plt.title(titles[i])

    plt.show()

def main():
    image_path = "img.png"
    width, height = 1920, 1080

    try:
        img = read_resize_image(image_path, width, height)
        lap = apply_laplacian(img)
        sob = apply_sobel(img)

        titles = ["Original", "Laplacian", "Sobel X", "Sobel Y", "Sobel"]
        images = [img, lap, sobx, soby, sob]

        display_images(images, titles)

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
