import numpy as np
import matplotlib.pyplot as plt

def newton_method(f, df, x0, max_iterations, tolerance):
    iterations = 0
    x = x0
    data = [x0]
    root_data = []

    while abs(f(x)) > tolerance and iterations < max_iterations:
        xi = x - f(x) / df(x)
        data.append(xi)
        root_data.append(xi)
        print(f"Iteration {iterations}: x = {xi}, f(x) = {f(xi)}, dx = {df(xi)}")
        x = xi
        iterations += 1

    if abs(f(x)) > tolerance:
        print("Error! Divergence!")

    root_data.append(x)
    return x, data, root_data


def plot_animation(data, f, root_data):
    x = np.linspace(-4, 4, 100)
    fx = np.vectorize(f)(x)
    plt.figure("Newton's Method")
    plt.title("Newton's Method")
    plt.plot(x, fx, color="blue", label="f(x)")
    plt.axhline(y=0, color='black')
    plt.axvline(x=0, color='black')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()

    for i in range(len(root_data)):
        x_values = [data[i], root_data[i]]
        y_values = [f(data[i]), 0]
        x_line = [data[i], data[i]]
        y_line = [f(data[i]), 0]
        plt.plot(x_values, y_values)
        plt.plot(x_line, y_line, '--')
        plt.plot(data[i], f(data[i]), c="red", marker="o")
        plt.pause(2)

    plt.grid()
    plt.show()


def main():
    f = lambda x: x ** 4 + 3 * np.cos(x) + 2 * x - 5
    df = lambda x: 4 * x ** 3 - 3 * np.sin(x) + 2

    root, data, root_data = newton_method(f, df, 0.8, 100, 0.00001)
    plot_animation(data, f, root_data)


if __name__ == '__main__':
    main()
