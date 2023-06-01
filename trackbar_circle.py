import cv2
import numpy as np

def nothing(x):
    print(x)

def main():
    img = np.zeros((500, 500, 3), dtype=np.uint8)
    cv2.namedWindow("Trackbar Window")
    cv2.createTrackbar("t1", "Trackbar Window", 0, 100, nothing)

    while True:
        t1 = cv2.getTrackbarPos("t1", "Trackbar Window")
        draw_circle(img, t1)
        cv2.imshow("Image", img)

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()

def draw_circle(img, t1):
    img.fill(0)
    radius = min(t1, 100)
    cv2.circle(img, (100, radius), 50, (255, 0, 0), 2)

if __name__ == "__main__":
    main()
