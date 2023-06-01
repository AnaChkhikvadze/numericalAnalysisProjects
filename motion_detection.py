import numpy as np
import cv2

def detect_motion():
    # Initialize video capture
    video_capture = cv2.VideoCapture(0)

    # Read initial frames
    _, previous_frame = video_capture.read()
    _, current_frame = video_capture.read()

    while video_capture.isOpened():
        # Compute frame difference
        frame_diff = cv2.absdiff(previous_frame, current_frame)
        gray_diff = cv2.cvtColor(frame_diff, cv2.COLOR_BGR2GRAY)
        blurred_diff = cv2.GaussianBlur(gray_diff, (5, 5), 0)
        _, threshold = cv2.threshold(blurred_diff, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(threshold, None, iterations=3)

        # Find contours of moving objects
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Draw bounding rectangles around moving objects
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if cv2.contourArea(contour) < 700:
                continue
            cv2.rectangle(previous_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow("Motion Detection", previous_frame)

        # Update frames
        previous_frame = current_frame
        _, current_frame = video_capture.read()

        # Check for 't' key press to exit
        if cv2.waitKey(1) & 0xFF == ord("t"):
            break

    # Release the video capture and close windows
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_motion()
