import numpy as np
import cv2

def main():
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    video_capture = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    video_output = cv2.VideoWriter("output.avi", fourcc, 20.0, (480, 640))

    background_subtractor = cv2.createBackgroundSubtractorKNN()

    while True:
        ret, frame = video_capture.read()

        if frame is None:
            break

        foreground_mask = background_subtractor.apply(frame)
        foreground_mask = cv2.morphologyEx(foreground_mask, cv2.MORPH_OPEN, kernel)

        video_output.write(foreground_mask)

        cv2.imshow("Foreground Mask", foreground_mask)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video_capture.release()
    video_output.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
