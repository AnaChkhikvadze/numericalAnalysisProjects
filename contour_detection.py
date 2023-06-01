import numpy as np
import cv2

def resize_image(image, scale_factor):
    return cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)

def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def threshold_image(image, threshold_value):
    _, thresholded_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    return thresholded_image

def find_contours(image):
    contours, _ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_L1)
    return contours

def draw_contours(image, contours, color=(10, 255, 10), thickness=1):
    cv2.drawContours(image, contours, -1, color, thickness)

def display_image(window_name, image):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    image_path = "img.png"
    scale_factor = 0.5
    threshold_value = 100

    original_image = cv2.imread(image_path)
    resized_image = resize_image(original_image, scale_factor)
    grayscale_image = convert_to_grayscale(resized_image)
    thresholded_image = threshold_image(grayscale_image, threshold_value)
    contour_list = find_contours(thresholded_image)

    print(f"Number of contours = {len(contour_list)}")

    draw_contours(resized_image, contour_list)
    display_image("Original Image", resized_image)
    display_image("Thresholded Image", thresholded_image)

if __name__ == "__main__":
    main()
