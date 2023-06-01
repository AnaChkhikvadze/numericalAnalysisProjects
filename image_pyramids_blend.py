import numpy as np
import cv2

def resize_image(image, width, height):
    """Resize the image to the specified width and height."""
    return cv2.resize(image, (width, height))

def create_pyramid(image, levels):
    """Create a Gaussian pyramid of the image with the given number of levels."""
    pyramid = [image.copy()]
    for i in range(levels):
        image = cv2.pyrDown(image)
        pyramid.append(image)
    return pyramid

def create_laplacian_pyramid(gaussian_pyramid):
    """Create a Laplacian pyramid from the given Gaussian pyramid."""
    laplacian_pyramid = [gaussian_pyramid[-1]]
    for i in range(len(gaussian_pyramid) - 1, 0, -1):
        gaussian_expanded = cv2.pyrUp(gaussian_pyramid[i])
        laplacian = cv2.subtract(gaussian_pyramid[i - 1], gaussian_expanded)
        laplacian_pyramid.append(laplacian)
    return laplacian_pyramid

def blend_images(laplacian_pyr1, laplacian_pyr2):
    """Blend two images using their Laplacian pyramids."""
    blended_pyr = []
    for lap1, lap2 in zip(laplacian_pyr1, laplacian_pyr2):
        cols, rows, ch = lap1.shape
        lap = np.hstack((lap1[:, :int(cols / 2)], lap2[:, int(cols / 2):]))
        blended_pyr.append(lap)
    return blended_pyr

def reconstruct_image(laplacian_pyr):
    """Reconstruct the image from its Laplacian pyramid."""
    reconstruct = laplacian_pyr[0]
    for i in range(1, len(laplacian_pyr)):
        reconstruct = cv2.pyrUp(reconstruct)
        reconstruct = cv2.add(laplacian_pyr[i], reconstruct)
    return reconstruct

def main():
    # Load images
    gradient = cv2.imread("color.png")
    landscape_img = cv2.imread("img.png")

    # Resize images
    landscape_img = resize_image(landscape_img, 500, 500)
    gradient = resize_image(gradient, 500, 500)

    # Create image combination
    combo = np.hstack((landscape_img[:, :255], gradient[:, 255:]))

    # Create Gaussian pyramids
    gp_landscape = create_pyramid(landscape_img.copy(), 6)
    gp_gradient = create_pyramid(gradient.copy(), 6)

    # Create Laplacian pyramids
    lp_landscape = create_laplacian_pyramid(gp_landscape)
    lp_gradient = create_laplacian_pyramid(gp_gradient)

    # Blend the images
    blended_pyr = blend_images(lp_landscape, lp_gradient)

    # Reconstruct the final image
    reconstruct = reconstruct_image(blended_pyr)

    # Display the images
    cv2.imshow("Blended Image", reconstruct)
    cv2.imshow("Image Combination", combo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
