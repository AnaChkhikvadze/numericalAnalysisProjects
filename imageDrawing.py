import numpy as np
import cv2

def draw_image():
    width, height = 680, 680
    img = np.zeros((width, height, 3), np.uint8)

    img = draw_line(img)
    img = draw_arrowed_line(img)
    img = draw_rectangle(img)
    img = draw_circle(img)
    img = draw_text(img)

    show_image(img)

def draw_line(img):
    start_point = (0, 0)
    end_point = (100, 100)
    color = (255, 0, 0)
    thickness = 2
    img = cv2.line(img, start_point, end_point, color, thickness)
    return img

def draw_arrowed_line(img):
    start_point = (20, 10)
    end_point = (400, 20)
    color = (255, 0, 0)
    thickness = 2
    img = cv2.arrowedLine(img, start_point, end_point, color, thickness)
    return img

def draw_rectangle(img):
    top_left = (400, 400)
    bottom_right = (500, 500)
    color = (0, 0, 255)
    thickness = 2
    img = cv2.rectangle(img, top_left, bottom_right, color, thickness)
    return img

def draw_circle(img):
    center = (400, 800)
    radius = 100
    color = (0, 255, 0)
    thickness = -1
    img = cv2.circle(img, center, radius, color, thickness)
    return img

def draw_text(img):
    text = "Anna"
    org = (500, 500)
    font_face = cv2.FONT_ITALIC
    font_scale = 4
    color = (255, 255, 255)
    thickness = 10
    line_type = cv2.LINE_AA
    img = cv2.putText(img, text, org, font_face, font_scale, color, thickness, line_type)
    return img

def show_image(img):
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    draw_image()
