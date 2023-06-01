import numpy as np
import cv2

def trackbar_callback(x):
    print(x)

def detect_shapes(image):
    resized_img = cv2.resize(image, (500, 500))
    blurred_img = cv2.GaussianBlur(resized_img, (3, 3), 6)
    gray_img = cv2.cvtColor(blurred_img, cv2.COLOR_BGR2GRAY)

    _, threshold_img = cv2.threshold(gray_img, 230, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        cv2.drawContours(resized_img, approx, -1, (0, 0, 255), 6)
        x, y = approx.ravel()[[0, 1]]

        if len(approx) == 3:
            cv2.putText(resized_img, "Triangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
        elif len(approx) == 4:
            x, y, h, w = cv2.boundingRect(approx)
            aspect_ratio = float(w) / h

            if 0.95 <= aspect_ratio <= 1.05:
                cv2.putText(resized_img, "Square", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
            else:
                cv2.putText(resized_img, "Rectangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
        elif len(approx) == 5:
            cv2.putText(resized_img, "Pentagon", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
        elif len(approx) == 6:
            cv2.putText(resized_img, "Hexagon", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
        else:
            cv2.putText(resized_img, "Circle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    cv2.imshow('Shapes', resized_img)
    cv2.imshow("Threshold", threshold_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    image = cv2.imread("images/shapes.jpg")
    detect_shapes(image)

if __name__ == "__main__":
    main()
