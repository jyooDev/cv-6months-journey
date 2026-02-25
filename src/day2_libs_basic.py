import numpy as np
import matplotlib.pyplot as plt


def findSolution(a1, b1, c1, d1, a2, b2, c2, d2):
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    x, y = np.meshgrid(x, y)
    z1 = (d1 - a1 * x - b1 * y) / c1
    z2 = (d2 - a2 * x - b2 * y) / c2

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(projection='3d')

    ax.plot_surface(x, y, z1, alpha=0.5)
    ax.plot_surface(x, y, z2, alpha=0.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()


if __name__ == "__main__":
    while True:
        try:
            a1 = float(input("Enter coefficient a1: "))
            b1 = float(input("Enter coefficient b1: "))
            c1 = float(input("Enter coefficient c1: "))
            d1 = float(input("Enter coefficient d1: "))  
            a2 = float(input("Enter coefficient a2: "))
            b2 = float(input("Enter coefficient b2: "))
            c2 = float(input("Enter coefficient c2: "))
            d2 = float(input("Enter coefficient d2: "))

            findSolution(a1, b1, c1, d1, a2, b2, c2, d2)
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue