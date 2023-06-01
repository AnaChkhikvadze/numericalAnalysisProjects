import numpy as np
import cv2

def main():
    # Create a black image
    background = np.zeros((250, 500, 3), np.uint8)

    # Draw a white rectangle on the black image
    rectangle = cv2.rectangle(background, (200, 0), (300, 100), (255, 255, 255), -1)

    # Load an image
    image = cv2.imread("img.png", 1)

    # Perform bitwise NOT operation
    bit_not = cv2.bitwise_not(rectangle, image)

    # Display the original images and the result
    cv2.imshow("Background", rectangle)
    cv2.imshow("Image", image)
    cv2.imshow("Bitwise NOT", bit_not)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
