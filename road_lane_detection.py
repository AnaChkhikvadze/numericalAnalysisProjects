import numpy as np
import cv2
import matplotlib.pyplot as plt

def read_image(file_path):
    return cv2.imread(file_path)

def apply_gaussian_blur(image, kernel_size=(3, 3), sigma=3):
    return cv2.GaussianBlur(image, kernel_size, sigma)

def convert_to_rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def get_image_dimensions(image):
    height, width = image.shape[:2]
    return width, height

def create_region_of_interest_mask(image, vertices):
    mask = np.zeros_like(image)
    mask_color = 255
    cv2.fillPoly(mask, np.int32([vertices]), mask_color)
    return mask

def apply_region_of_interest(image, mask):
    return cv2.bitwise_and(image, mask)

def draw_detected_lines(image, lines):
    image_copy = image.copy()
    line_image = np.zeros_like(image_copy)
    
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    return cv2.addWeighted(image_copy, 0.8, line_image, 1, 0.0)

def display_image(image):
    plt.imshow(image, cmap='gray')
    plt.show()

# Read the image
image = read_image("images/road.jpg")

# Apply Gaussian blur
blurred_image = apply_gaussian_blur(image)

# Convert to RGB
rgb_image = convert_to_rgb(blurred_image)

# Get image dimensions
width, height = get_image_dimensions(rgb_image)

# Define region of interest vertices
region_of_interest_vertices = [
    [0, height],
    [width / 2, height / 2],
    [830, 360],
    [width, height]
]

# Create region of interest mask
roi_mask = create_region_of_interest_mask(rgb_image, region_of_interest_vertices)

# Apply region of interest mask
cropped_image = apply_region_of_interest(rgb_image, roi_mask)

# Detect lines using Hough transform
lines = cv2.HoughLinesP(image=cropped_image, rho=1, theta=np.pi / 180, threshold=100, minLineLength=10, maxLineGap=60)

# Draw detected lines on the image
image_with_lines = draw_detected_lines(rgb_image, lines)

# Display the final image
display_image(image_with_lines)
