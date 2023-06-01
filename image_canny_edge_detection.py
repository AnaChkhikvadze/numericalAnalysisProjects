import cv2

def nothing(x):
    pass

def main():
    # Load the image
    img = cv2.imread("img.png", 0)
    img = cv2.resize(img, (500, 500))
    
    # Create trackbars
    cv2.namedWindow("Image")
    cv2.createTrackbar("Threshold 1", "Image", 1, 255, nothing)
    cv2.createTrackbar("Threshold 2", "Image", 1, 255, nothing)
    
    while True:
        # Get trackbar positions
        threshold1 = cv2.getTrackbarPos("Threshold 1", "Image")
        threshold2 = cv2.getTrackbarPos("Threshold 2", "Image")
        
        # Display original image
        cv2.imshow("Original Image", img)
        
        # Apply Canny edge detection
        canny = cv2.Canny(img, threshold1, threshold2)
        
        # Display the result
        cv2.imshow("Canny Edge Detection", canny)
        
        # Check for key press
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC key
            break
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
