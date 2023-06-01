import cv2
import numpy as np
from matplotlib import pyplot as plt


def g_function(z, k):
    return 1 / (1 + (z / k) ** 2)


def update_image_intensity(image, x, y, k, dx, dy, dt):
    # Gradient in the x direction
    ix = (image[x + 1, y] - image[x - 1, y]) / (2 * dx)
    # Gradient in the y direction
    iy = (image[x, y + 1] - image[x, y - 1]) / (2 * dy)
    # Magnitude of the gradient
    gradient_intensity = np.sqrt(ix ** 2 + iy ** 2)
    # Value of g for each point
    g_term = g_function(gradient_intensity, k)
    # X-derivative of the image at the next time step
    ix_next = (g_term[:, :-1] + g_term[:, 1:]) * ix / 2 * dx
    # Y-derivative of the image at the next time step
    iy_next = (g_term[:-1, :] + g_term[1:, :]) * iy / 2 * dy
    # Next image at the next time step
    image_next = image + dt * (ix_next[:, 1:-1] + iy_next[1:-1, :])
    return image_next


def ssp_runge_kutta(image, x, y, t, k, dx, dy, dt):
    # First stage
    image_1 = update_image_intensity(image, x, y, k, dx, dy, dt)
    # Second stage
    image_2 = (3 / 4) * image + (1 / 4) * image_1 + (1 / 4) * dt * update_image_intensity(image_1, x, y, k, dx, dy, dt)
    # Third stage
    image_next = (1 / 3) * image + (2 / 3) * image_2 + (2 / 3) * dt * update_image_intensity(image, x, y, k, dx, dy, dt)
    return image_next


def image_denoising(image_0, x_min, x_max, y_min, y_max, t_0, t_max, k, dt):
    dx, dy = 1, 2
    # Discretize the x-axis
    x = np.arange(x_min, x_max + dx, dx)
    # Discretize the y-axis
    y = np.arange(y_min, y_max + dy, dy)
    # Discretize the time axis
    t = np.arange(t_0, t_max + dt, dt)
    # Initialize the image
    image = image_0
    # Loop over all time steps
    for i in range(len(t) - 1):
        image = ssp_runge_kutta(image, x, y, t[i], k, dx, dy, dt)
    return image


if __name__ == "__main__":
    # Load the image and convert it to grayscale
    image = cv2.imread('coffee.png')
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Add Gaussian noise to the image
    noisy_image = grayscale + np.random.normal(0, 25, grayscale.shape)

    # Define the parameters for image denoising
    x_min, x_max = 0, image.shape[1] + 1
    y_min, y_max = 0, image.shape[0] + 1
    k = 100  # Number of spatial points
    t_min, t_max = 0, 10  # Time range
    dt = 0.05  # Time step size (increasing it improves results but takes more time)

    denoised_image = image_denoising(noisy_image, x_min, x_max, y_min, y_max, t_min, t_max, k, dt)

    # Plot the original image, the noisy image, and the denoised image
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    axs[0].imshow(grayscale, cmap='gray')
    axs[0].set_title('Original')
    axs[1].imshow(noisy_image, cmap='gray')
    axs[1].set_title('Noisy')
    axs[2].imshow(denoised_image, cmap='gray')
    axs[2].set_title('Denoised')
    plt.show()
