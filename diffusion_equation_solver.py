import numpy as np
import matplotlib.pyplot as plt

# Parameters
domain_length_x = 1.0
domain_length_y = 1.0
grid_points_x = 101
grid_points_y = 101
grid_spacing_x = domain_length_x / (grid_points_x - 1)
grid_spacing_y = domain_length_y / (grid_points_y - 1)
diffusion_coefficient = 1.0
time_step = 0.1
total_simulation_time = 5.0

# Initialize the solution
solution = np.zeros((grid_points_x, grid_points_y))

# Set initial condition
solution[int(grid_points_x / 2), int(grid_points_y / 2)] = 1.0

# Time-stepping loop
for time in np.arange(0, total_simulation_time, time_step):
    previous_solution = solution.copy()

    # Solve in the x-direction
    for i in range(1, grid_points_x - 1):
        for j in range(1, grid_points_y):
            solution[i, j] = previous_solution[i, j] + diffusion_coefficient * time_step / grid_spacing_x ** 2 * (
                        previous_solution[i + 1, j] - 2 * previous_solution[i, j] + previous_solution[i - 1, j])

    # Solve in the y-direction
    for i in range(1, grid_points_x):
        for j in range(1, grid_points_y - 1):
            solution[i, j] = solution[i, j] + diffusion_coefficient * time_step / grid_spacing_y ** 2 * (
                        solution[i, j + 1] - 2 * solution[i, j] + solution[i, j - 1])

    # Solve in the x-direction again
    for i in range(1, grid_points_x - 1):
        for j in range(1, grid_points_y):
            solution[i, j] = solution[i, j] + diffusion_coefficient * time_step / grid_spacing_x ** 2 * (
                        solution[i + 1, j] - 2 * solution[i, j] + solution[i - 1, j])

    # Plot and save the solution
    plt.imshow(solution, extent=[0, domain_length_x, 0, domain_length_y], origin='lower',
               cmap='hot', vmin=solution.min(), vmax=solution.max())
    plt.colorbar()
    plt.title('Diffusion Equation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig("diffusion_t={:.2f}.png".format(time))
    plt.clf()
