import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Physical parameters
thermal_conductivity_steel = 1.172E-5  # thermal conductivity of steel with 1% carbon
plate_length = 0.1  # length of the rectangular plate in the x-direction
plate_width = 0.1  # width of the rectangular plate in the y-direction

# Numerical parameters
num_points_x = 40  # number of points in the x direction
num_points_y = 40  # number of points in the y direction
time_step = 0.1  # time step
final_time = 10  # final time

# Boundary conditions (Dirichlet)
internal_field_temperature = 1
bottom_edge_temperature = 0
top_edge_temperature = 0
left_edge_temperature = 0
right_edge_temperature = 0

# Compute cell length
dx = plate_length / num_points_x
dy = plate_width / num_points_y

# Calculate Courant numbers
courant_number_x = thermal_conductivity_steel * time_step / (dx ** 2)
courant_number_y = thermal_conductivity_steel * time_step / (dy ** 2)

# Check for stability
if courant_number_x > 0.5 or courant_number_y > 0.5:
    raise ValueError("Unstable Solution!")

# Initialize temperature array
temperature = np.zeros((num_points_x, num_points_y, int(final_time / time_step)))

# Set initial condition
temperature[:, :, 0] = internal_field_temperature

# Set boundary conditions
temperature[:, 0] = bottom_edge_temperature
temperature[:, -1] = top_edge_temperature
temperature[0] = left_edge_temperature
temperature[-1] = right_edge_temperature

# Generate 2D mesh
X, Y = np.meshgrid(np.linspace(0, plate_length, num_points_x, endpoint=True),
                   np.linspace(0, plate_width, num_points_y, endpoint=True))

# Main time-loop
for t in range(0, int(final_time / time_step) - 1):
    for i in range(1, num_points_x - 1):
        for j in range(1, num_points_y - 1):
            d2dx2 = (temperature[i + 1, j, t] - 2 * temperature[i, j, t] + temperature[i - 1, j, t]) / dx ** 2
            d2dy2 = (temperature[i, j + 1, t] - 2 * temperature[i, j, t] + temperature[i, j - 1, t]) / dy ** 2
            temperature[i, j, t + 1] = thermal_conductivity_steel * time_step * (d2dx2 + d2dy2) + temperature[i, j, t]

# Plot the final temperature distribution
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, temperature[:, :, int(final_time / time_step) - 1], cmap='gist_rainbow_r', edgecolor='none')
ax.set_xlabel('X [m]')
ax.set_ylabel('Y [m]')
ax.set_zlabel('T [°]')
plt.show()
