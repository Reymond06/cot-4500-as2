# README

# Interpolation Methods
This repository contains Python implementations of: Neville's Method, Newton's Forward Method, Hermite Polynomial Approximation, and Cubic Spline Interpolation. These methods are used to estimate unknown values that fall within the range of a discrete set of known data points.

## Requirements
This project requires Python 3 and the NumPy library as well as Python's math library

# Running Code
To use and run the code, please save assignment_2.py to your computer and edit the code to include your values and run the following command on your terminal: python3 assignment_2.py

To run test_assignment_2.py, save the file and run the following command in your terminal: python3 test_assignment_2.py

# Interpolation Methods

Neville's Method: Neville's method is used to find the interpolating polynomial that passes through a given set of data points. It is particularly useful for small sets of data

Newton's Forward Method: Newton's forward method is used to construct a polynomial that approximates a function using forward differences. This method is efficient for equally spaced data points

Hermite Polynomial Approximation: Hermite interpolation is used when both function values and derivative values are known. It constructs a polynomial that matches both the function values and the derivative values at the given data points

Cubic Spline Interpolation: Cubic spline interpolation is used to construct a smooth curve that passes through a given set of data points. It ensures that the curve is smooth at the data points by matching the first and second derivatives
