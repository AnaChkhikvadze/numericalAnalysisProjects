import numpy as np
import cv2
import matplotlib.pyplot as plt

def show_image_grid(images, titles):
    num_images = len(images)

    plt.figure(figsize=(12, 8))
    for i in range(num_images):
        plt.subplot(2, np.ceil(num_images/2), i+1)
        plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.tight_layout()
    plt.show()

def main():
    img = cv2.imread("img.png")
    img = cv2.resize(img, (1280, 720))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    kernel = 1 / 25 * np.ones((5, 5))

    blur = cv2.blur(img, (5, 5))
    gaussian = cv2.GaussianBlur(img, (5, 5), 0)
    median = cv2.medianBlur(img, 5)
    bilateral = cv2.bilateralFilter(img, 9, 75, 75)

    titles = ["Original Image", "Box Blur", "Gaussian Blur", "Median Blur", "Bilateral Filter"]
    images = [img, blur, gaussian, median, bilateral]

    show_image_grid(images, titles)

if __name__ == "__main__":
    main()
