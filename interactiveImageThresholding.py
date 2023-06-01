import cv2


def print_value(value):
    print(value)


def main():
    image_path = "color.png"
    try:
        img = cv2.imread(image_path, 0)
    except FileNotFoundError:
        print(f"Error: Image file '{image_path}' not found.")
        return

    cv2.namedWindow("Threshold")
    trackbar_name = "Threshold Value"
    cv2.createTrackbar(trackbar_name, "Threshold", 0, 255, print_value)

    while True:
        cv2.imshow("Gradient", img)
        threshold_value = cv2.getTrackbarPos(trackbar_name, "Threshold")
        _, th1 = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)
        _, th2 = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY_INV)
        _, th3 = cv2.threshold(img, threshold_value, 255, cv2.THRESH_TRUNC)
        _, th4 = cv2.threshold(img, threshold_value, 255, cv2.THRESH_TOZERO)
        _, th5 = cv2.threshold(img, threshold_value, 255, cv2.THRESH_TOZERO_INV)
        cv2.imshow("Thresholding 1", th1)
        cv2.imshow("Thresholding 2", th2)
        cv2.imshow("Thresholding 3", th3)
        cv2.imshow("Thresholding 4", th4)
        cv2.imshow("Thresholding 5", th5)

        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
