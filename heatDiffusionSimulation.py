import numpy as np

def simulate_heat_diffusion_finite_difference(L, N, dx, dt, alpha, num_steps):
    """
    Simulates heat diffusion in a rod using the finite difference method.

    Args:
        L (float): Length of the rod.
        N (int): Number of grid points.
        dx (float): Spatial step.
        dt (float): Time step.
        alpha (float): Thermal diffusivity.
        num_steps (int): Number of time steps to simulate.

    Returns:
        numpy.ndarray: Array containing the temperature field at each grid point.
    """
    T = np.zeros(N)  # Initialize temperature field

    for _ in range(num_steps):
        Tn = T.copy()  # Create a copy of the temperature field

        for i in range(1, N - 1):
            T[i] = Tn[i] + alpha * dt / dx ** 2 * (Tn[i + 1] - 2 * Tn[i] + Tn[i - 1])

    return T


def simulate_heat_diffusion_backward_difference(L, N, dx, dt, alpha, num_steps):
    """
    Simulates heat diffusion in a rod using the backward difference method.

    Args:
        L (float): Length of the rod.
        N (int): Number of grid points.
        dx (float): Spatial step.
        dt (float): Time step.
        alpha (float): Thermal diffusivity.
        num_steps (int): Number of time steps to simulate.

    Returns:
        numpy.ndarray: Array containing the temperature field at each grid point.
    """
    T = np.zeros(N)  # Initialize temperature field
    T_prev = np.zeros(N)  # Initialize previous temperature field

    for _ in range(num_steps):
        for i in range(1, N - 1):
            T_prev[i] = T[i]
            T[i] = T_prev[i] + alpha * dt / dx ** 2 * (T_prev[i + 1] - 2 * T_prev[i] + T_prev[i - 1])

    return T


# Parameters
L = 1  # Length of the rod
N = 10  # Number of grid points
dx = L / (N - 1)  # Spatial step
dt = 0.01  # Time step
alpha = 0.01  # Thermal diffusivity
num_steps = 1000  # Number of time steps

# Simulate heat diffusion using the finite difference method
temperature_fd = simulate_heat_diffusion_finite_difference(L, N, dx, dt, alpha, num_steps)

# Simulate heat diffusion using the backward difference method
temperature_bd = simulate_heat_diffusion_backward_difference(L, N, dx, dt, alpha, num_steps)
