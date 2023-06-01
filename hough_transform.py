import numpy as np
import cv2

IMAGE_SIZE = (500, 500)
GAUSSIAN_KERNEL_SIZE = (5, 5)
GAUSSIAN_SIGMA = 1
CANNY_THRESHOLD1 = 200
CANNY_THRESHOLD2 = 200
HOUGH_RESOLUTION = 1
HOUGH_THETA = np.pi / 360
HOUGH_THRESHOLD = 100
HOUGH_MIN_LINE_LENGTH = 10
HOUGH_MAX_LINE_GAP = 9
LINE_COLOR = (0, 255, 255)
LINE_THICKNESS = 2

def detect_and_draw_lines(image_path):
    # Load and resize the image
    image = cv2.imread(image_path)
    if image is None:
        print("Failed to load image")
        return
    image = cv2.resize(image, IMAGE_SIZE)

    # Convert to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect edges using Canny edge detection
    edge_image = cv2.Canny(grayscale_image, CANNY_THRESHOLD1, CANNY_THRESHOLD2)

    # Display edge image
    cv2.imshow("Edges", edge_image)

    # Detect lines using Hough transform
    detected_lines = cv2.HoughLinesP(edge_image, HOUGH_RESOLUTION, HOUGH_THETA, HOUGH_THRESHOLD,
                                     minLineLength=HOUGH_MIN_LINE_LENGTH, maxLineGap=HOUGH_MAX_LINE_GAP)

    # Draw the detected lines on the image
    for line in detected_lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), LINE_COLOR, LINE_THICKNESS)

    # Display the image with lines
    cv2.imshow("Image", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call the function and pass the image file path
detect_and_draw_lines("img.png")
