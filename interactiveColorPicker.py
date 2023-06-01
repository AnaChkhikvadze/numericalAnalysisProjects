import numpy as np
import cv2


def nothing(x):
    pass


def main():
    img = np.zeros((500, 500, 3), np.uint8)
    cv2.namedWindow("Interactive Color Picker")

    cv2.createTrackbar("B", "Interactive Color Picker", 0, 255, nothing)
    cv2.createTrackbar("G", "Interactive Color Picker", 0, 255, nothing)
    cv2.createTrackbar("R", "Interactive Color Picker", 0, 255, nothing)

    switch = '0: OFF\n1: ON'
    cv2.createTrackbar(switch, 'Interactive Color Picker', 0, 1, nothing)

    while True:
        cv2.imshow("Interactive Color Picker", img)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break

        b = cv2.getTrackbarPos("B", "Interactive Color Picker")
        g = cv2.getTrackbarPos("G", "Interactive Color Picker")
        r = cv2.getTrackbarPos("R", "Interactive Color Picker")
        s = cv2.getTrackbarPos(switch, "Interactive Color Picker")

        if s == 0:
            img[:] = 0
        else:
            img[:] = [b, g, r]

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
