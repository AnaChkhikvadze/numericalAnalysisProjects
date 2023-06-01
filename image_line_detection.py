import numpy as np
import cv2

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    resized_image = cv2.resize(image, (500, 500))
    blurred_image = cv2.GaussianBlur(resized_image, (5, 5), 1)
    gray_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2GRAY)
    return gray_image

def detect_edges(image):
    edges = cv2.Canny(image, 50, 200)
    return edges

def detect_lines(edges):
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
    return lines

def draw_lines(image, lines):
    for line in lines:
        rho, theta = line[0]
        cos_theta = np.cos(theta)
        sin_theta = np.sin(theta)
        x0 = cos_theta * rho
        y0 = sin_theta * rho
        x1 = int(x0 + 1000 * (-sin_theta))
        y1 = int(y0 + 1000 * cos_theta)
        x2 = int(x0 - 1000 * (-sin_theta))
        y2 = int(y0 - 1000 * cos_theta)
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 1)
    return image

def main():
    image_path = "img.png"
    gray_image = preprocess_image(image_path)
    edges = detect_edges(gray_image)
    lines = detect_lines(edges)
    image_with_lines = draw_lines(gray_image, lines)

    cv2.imshow("Edges", edges)
    cv2.imshow("Image with Lines", image_with_lines)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
