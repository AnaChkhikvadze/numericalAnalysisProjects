import numpy as np
import cv2
import matplotlib.pyplot as plt


class InteractiveImageAnalyzer:
    def __init__(self, image_path):
        self.img = cv2.imread(image_path, 1)
        self.points = []
        cv2.imshow("Image", self.img)
        cv2.setMouseCallback("Image", self.click_event)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def click_event(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.show_coordinates(x, y)
        elif event == cv2.EVENT_RBUTTONDOWN:
            self.show_pixel_value(x, y)

    def show_coordinates(self, x, y):
        font = cv2.FONT_ITALIC
        text = f'x={x}; y={y}'
        cv2.putText(self.img, text, (x, y), font, 0.4, (255, 255, 0), 2)
        cv2.imshow("Image", self.img)

    def show_pixel_value(self, x, y):
        font = cv2.FONT_ITALIC
        blue, green, red = self.img[y, x]
        text = f'{blue}; {green}; {red}'
        cv2.putText(self.img, text, (x, y), font, 0.4, (0, 255, 255), 2)
        cv2.imshow("Image", self.img)


image_analyzer = InteractiveImageAnalyzer("img.png")
