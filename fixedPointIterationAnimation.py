import numpy as np
import matplotlib.pyplot as plt

def fixed_point_iteration(approx_function, fixed_point_function, initial_guess, min_error, max_iterations):
    iteration = 0
    error = 1
    x = 0
    data = []

    while error > min_error and iteration < max_iterations:
        x = fixed_point_function(initial_guess)
        error = abs(initial_guess - x)
        print(f'Iteration: {iteration}, x = {x:.6f}, error = {error:.6f}, f(x) = {approx_function(x):.6f}')
        initial_guess = x
        data.append(initial_guess)
        iteration += 1

    if error > min_error:
        print("Error!!! Divergence!!!")

    return x, data


def animate_fixed_point_iteration(approx_function, fixed_point_function, root, data, initial_guess, data_x):
    x = np.linspace(-5, 5, 100)
    y = np.vectorize(fixed_point_function)(x)
    fx = np.vectorize(approx_function)(x)

    plt.figure("Fixed Point Iteration")
    plt.title('Fixed Point Iteration')
    plt.plot(x, y, color="red", label="g(x)")
    plt.plot(x, fx, color="blue", label="f(x)")
    plt.plot(x, x, color="yellow", label="x = y")
    plt.plot(initial_guess, fixed_point_function(initial_guess), 'ro')
    plt.xlim(min(x), max(x))
    plt.axhline(y=0, color='black')
    plt.axvline(x=0, color='black')
    temp_data_x, temp_data = [], []
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()

    for i in range(len(data)):
        if i == 0:
            plt.ylim(root - 10, root + 10)
        else:
            plt.xlim(data_x[i] - 1, data[i] + 1)
        temp_data_x.append(data_x[i])
        temp_data.append(data[i])
        plt.scatter(temp_data_x, temp_data)
        plt.pause(2)

    plt.show()


approx_function = lambda x: x ** 4 - 3 * x ** 2 - 3
fixed_point_function = lambda x: (3 * x ** 2 + 3) ** (1 / 4)
initial_guess = 1
min_error = 0.001
max_iterations = 100

root, data = fixed_point_iteration(approx_function, fixed_point_function, initial_guess, min_error, max_iterations)

data_x = [initial_guess] + data[:-1]
animate_fixed_point_iteration(approx_function, fixed_point_function, root, data, initial_guess, data_x)
