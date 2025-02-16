# Reymond Ramirez
# COT 4500
# Assignment 2

import numpy as np
import math

# Cubic Spline Function
def cubic_spline(x, y):
    n = len(x) - 1
    h = [x[i + 1] - x[i] for i in range(n)]
    alpha = [0] * (n + 1)
    for i in range(1, n):
        alpha[i] = (3 / h[i]) * (y[i + 1] - y[i]) - (3 / h[i - 1]) * (y[i] - y[i - 1])

    l = [1] + [0] * n
    mu = [0] * (n + 1)
    z = [0] * (n + 1)
    for i in range(1, n):
        l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

    l[n] = 1
    z[n] = 0
    c = [0] * (n + 1)
    b = [0] * n
    d = [0] * n
    a = [y[i] for i in range(n)]
    for j in range(n - 1, -1, -1):
        c[j] = z[j] - mu[j] * c[j + 1]
        b[j] = (y[j + 1] - y[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    return a, b, c, d

# Hermite Function
def hermite(x, y, y_prime):
    n = len(x)
    Q = np.zeros((2 * n, 2 * n))
    z = np.zeros(2 * n)
    for i in range(n):
        z[2 * i] = z[2 * i + 1] = x[i]
        Q[2 * i][0] = Q[2 * i + 1][0] = y[i]
        Q[2 * i + 1][1] = y_prime[i]
        if i != 0:
            Q[2 * i][1] = (Q[2 * i][0] - Q[2 * i - 1][0]) / (z[2 * i] - z[2 * i - 1])
    for i in range(2, 2 * n):
        for j in range(2, i + 1):
            Q[i][j] = (Q[i][j - 1] - Q[i - 1][j - 1]) / (z[i] - z[i - j])
    return Q

# Newton Forward Function
def newton_forward(x, y):
    n = len(x)
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = diff_table[i + 1][j - 1] - diff_table[i][j - 1]
    return diff_table


def print_polynomial_approximations(x, diff_table):
    for degree in range(1, 4):  
        print(f"{diff_table[0][degree]:.15f}")
    print("\n")

def newton_forward_interpolation(x, y, x_to_interpolate):
    diff_table = newton_forward(x, y)
    h = x[1] - x[0]
    u = (x_to_interpolate - x[0]) / h
    interpolation_value = y[0]
    u_term = 1
    for i in range(1, len(x)):
        u_term *= (u - (i - 1))
        interpolation_value += (u_term * diff_table[0][i]) / math.factorial(i)
    return interpolation_value


def neville(x, y, w):
    m = len(x)
    a = y.copy()
    for k in range(1, m):
        for i in range(m - k):
            a[i] = ((w - x[i + k]) * a[i] + (x[i] - w) * a[i + 1]) / (x[i] - x[i + k])
    return a[0]

def main():
    # Neville's Method
    neville_x = np.array([3.6, 3.8, 3.9])
    neville_y = np.array([1.675, 1.436, 1.318])
    result = neville(neville_x, neville_y, 3.7)
    print(result,"\n")

    # Newton's Forward Method
    newton_x = np.array([]) # Insert x values
    newton_y = np.array([]) # Insery y values
    diff_table = newton_forward(newton_x, newton_y)
    print_polynomial_approximations(newton_x, diff_table)
    x_to_interpolate = # Insert x value to interpolate
    approximation = newton_forward_interpolation(newton_x, newton_y, x_to_interpolate)
    print(approximation,"\n")

    # Divided Difference
    divided_x=np.array([]) # Insert x values
    divided_y=np.array([]) # Insert y values
    divided_prime=np.array([]) # Insert y' values
    hermite_matrix = hermite(divided_x, divided_y, divided_prime)
    print(hermite_matrix[:6, :5])

    # Cubic Spline Interpolation
    cubic_x=np.array([]) # Insert x values
    cubic_y=np.array([]) # Insert y values

    a, b, c, d = cubic_spline(cubic_x, cubic_y)

    # Forming Matrix A
    n = len(cubic_x) - 1
    A = np.zeros((n + 1, n + 1))
    for i in range(1, n):
        A[i, i - 1] = cubic_x[i] - cubic_x[i - 1]
        A[i, i] = 2 * (cubic_x[i + 1] - cubic_x[i - 1])
        A[i, i + 1] = cubic_x[i + 1] - cubic_x[i]
    A[0, 0] = 1
    A[n, n] = 1

    # Forming Vector B
    b_vec = np.zeros(n + 1)
    for i in range(1, n):
        b_vec[i] = 3 * ((cubic_y[i + 1] - cubic_y[i]) / (cubic_x[i + 1] - cubic_x[i]) - (cubic_y[i] - cubic_y[i - 1]) / (cubic_x[i] - cubic_x[i - 1]))

    # Forming Vector X
    x_vec = np.linalg.solve(A, b_vec)
    print("\n")
    print(A)
    print(b_vec)
    print(x_vec)

main()
