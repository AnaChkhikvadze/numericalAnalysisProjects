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
total_time = 5.0

# Initialize the solution
solution = np.zeros((grid_points_x, grid_points_y))

# Time-stepping loop
for t in np.arange(0, total_time, time_step):
    previous_solution = solution.copy()

    # Solve in x-direction
    for i in range(1, grid_points_x - 1):
        for j in range(1, grid_points_y):
            solution[i, j] = previous_solution[i, j] + diffusion_coefficient * time_step / grid_spacing_x ** 2 * (
                    previous_solution[i + 1, j] - 2 * previous_solution[i, j] + previous_solution[i - 1, j])

    # Solve in y-direction
    for i in range(1, grid_points_x):
        for j in range(1, grid_points_y - 1):
            solution[i, j] = solution[i, j] + diffusion_coefficient * time_step / grid_spacing_y ** 2 * (
                    solution[i, j + 1] - 2 * solution[i, j] + solution[i, j - 1])

# Plot the solution
plt.imshow(solution, extent=[0, domain_length_x, 0, domain_length_y], origin='lower',
           cmap='hot', vmin=solution.min(), vmax=solution.max())
plt.colorbar()
plt.title('Diffusion Equation Solution')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
