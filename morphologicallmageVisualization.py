import numpy as np
import cv2
import matplotlib.pyplot as plt

def ImageMorphologyVisualization(image_path, kernel_size, iterations=1):
    try:
        with open(image_path, 'rb') as file:
            img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

        _, th1 = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY)
        kernel = np.ones((kernel_size, kernel_size), np.uint8)

        dilation = cv2.dilate(th1, kernel, iterations=iterations)
        erosion = cv2.erode(th1, kernel, iterations=iterations)
        opening = cv2.morphologyEx(th1, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(th1, cv2.MORPH_CLOSE, kernel)
        gradient = cv2.morphologyEx(th1, cv2.MORPH_GRADIENT, kernel)

        titles = ["Original", "Threshold", "Dilation", "Erosion", "Opening", "Closing", "Gradient"]
        images = [img, th1, dilation, erosion, opening, closing, gradient]

        plt.figure(figsize=(10, 8))

        for i, image in enumerate(images):
            plt.subplot(3, 3, i + 1)
            if i == 1:
                plt.imshow(image, cmap='gray')
            else:
                plt.imshow(image, cmap='gray', vmin=0, vmax=255)
            plt.title(titles[i])
            plt.xticks([])
            plt.yticks([])

        plt.subplots_adjust(top=0.9, bottom=0.1, left=0.1, right=0.9, hspace=0.5, wspace=0.5)
        plt.colorbar()

        plt.show()

    except FileNotFoundError:
        print("Image file not found.")
    except Exception as e:
        print("An error occurred:", str(e))

# Example usage
ImageMorphologyVisualization("img.png", kernel_size=2, iterations=1)
