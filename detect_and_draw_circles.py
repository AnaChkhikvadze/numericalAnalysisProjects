import numpy as np
import cv2

def detect_and_draw_circles(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Resize the image
    resized_image = cv2.resize(image, (1400, 700))

    # Create a copy of the image for output
    output_image = resized_image.copy()

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    # Apply median blur to reduce noise
    blurred_image = cv2.medianBlur(gray_image, 5)

    # Detect circles using Hough transform
    circles = cv2.HoughCircles(image=blurred_image,
                               method=cv2.HOUGH_GRADIENT,
                               dp=1,
                               minDist=20,
                               param1=50,
                               param2=60,
                               minRadius=0,
                               maxRadius=0)

    # Ensure circles were found
    if circles is not None:
        detected_circles = np.uint16(np.around(circles))

        # Draw the detected circles on the output image
        for (x, y, r) in detected_circles[0, :]:
            cv2.circle(output_image, (x, y), r, (0, 255, 0), 2)
            cv2.circle(output_image, (x, y), 2, (0, 255, 255), 2)

        # Display the output image
        cv2.imshow("Circles Detected", output_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Specify the image file path
image_file = "shapes.png"

# Detect and draw circles in the image
detect_and_draw_circles(image_file)
