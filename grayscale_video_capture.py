import cv2

def capture_video():
    # Open video capture
    video_capture = cv2.VideoCapture(0)

    # Print initial video capture properties
    print("Initial video capture properties:")
    print("Width:", video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    print("Height:", video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Set video capture properties (optional)
    # video_capture.set(3, 1208)
    # video_capture.set(4, 720)

    # Print updated video capture properties
    print("Updated video capture properties:")
    print("Width:", video_capture.get(3))
    print("Height:", video_capture.get(4))

    # Create video writer
    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    video_writer = cv2.VideoWriter("outputgray.avi", fourcc, 20.0, (640, 480))

    while True:
        # Read frame from video capture
        ret, frame = video_capture.read()

        if ret:
            # Convert frame to grayscale
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Write grayscale frame to video file
            video_writer.write(gray_frame)

            # Display the grayscale frame
            cv2.imshow("frame", gray_frame)

            # Check for 'q' key press to exit
            if cv2.waitKey(1) == ord("q"):
                break
        else:
            break

    # Release video capture and writer
    video_capture.release()
    video_writer.release()

    # Close all windows
    cv2.destroyAllWindows()

# Call the main function
if __name__ == "__main__":
    capture_video()
