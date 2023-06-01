import numpy as np
import cv2


def nothing(x):
    pass


def main():
    img = cv2.imread("img.png", 0)
    img = cv2.resize(img, (500, 500))

    cv2.namedWindow("Threshold")
    cv2.createTrackbar("Threshold Value", "Threshold", 1, 255, nothing)
    cv2.createTrackbar("Block Size", "Threshold", 3, 255, nothing)
    cv2.createTrackbar("Constant", "Threshold", 0, 255, nothing)

    while True:
        cv2.imshow("Image", img)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # Press 'Esc' key to exit
            break

        threshold_value = cv2.getTrackbarPos("Threshold Value", "Threshold")
        block_size = cv2.getTrackbarPos("Block Size", "Threshold")
        constant = cv2.getTrackbarPos("Constant", "Threshold")

        if block_size % 2 == 0:
            block_size += 1

        _, binary_threshold = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)
        adaptive_mean_threshold = cv2.adaptiveThreshold(
            img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, constant
        )
        adaptive_gaussian_threshold = cv2.adaptiveThreshold(
            img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, constant
        )

        cv2.imshow("Binary Threshold", binary_threshold)
        cv2.imshow("Adaptive Mean Threshold", adaptive_mean_threshold)
        cv2.imshow("Adaptive Gaussian Threshold", adaptive_gaussian_threshold)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
