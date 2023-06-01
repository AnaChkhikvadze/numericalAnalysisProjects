import numpy as np
import cv2
import matplotlib.pyplot as plt

def display_image(img):
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def plot_histogram(image):
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show()

def create_rectangle_image(width, height, color):
    img = np.zeros((height, width), np.uint8)
    cv2.rectangle(img, (0, height // 2), (width, height), color, -1)
    return img

def main():
    image_width = 200
    image_height = 200

    black = 0
    white = 255
    gray = 127

    # Create image with two rectangles
    img = create_rectangle_image(image_width, image_height, white)
    cv2.rectangle(img, (0, image_height // 2), (image_width // 2, image_height), gray, -1)

    # Display the image
    display_image(img)

    # Plot the histogram of the image
    plot_histogram(img)

if __name__ == "__main__":
    main()
