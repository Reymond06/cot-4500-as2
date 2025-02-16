# Reymond Ramirez
# COT4500
# Assignment 1 Test Cases
import math
import numpy as np

# Approximating sqrt(2)
def approx_algorithm(initial,tolerance):
    iterations=0
    diff = initial
    x = initial
    print(iterations,":",initial)
    while (diff>=tolerance):
        iterations+=1
        y=x
        x = (x/2)+(1/x)
        diff = abs(y-x)
        print(iterations,":",x)

    print("Convergence after",iterations,"iterations\n")

def f(x):
    return x**2 - 2 # y = x^2 - 2

# Finding x = sqrt(2) as a zero
def bisection_method(left,right,tolerance,max_value):
    i = 0

    while(abs(right-left)>tolerance and i<max_value):
        i+=1

        p = (left+right)/2

        if((f(left)<0 and f(p)>0) or (f(left)>0 and f(p)<0)):
            right= p
        else:
            left = p
        print(i,":",p)
    print("\n")

def g(x):
    return 0.5*pow(10.0-x*x*x,0.5) # y = 0.5(10-x^3)^0.5

# Finding solution to the equation
def fixedpoint_iteration(p0, TOL, n0):
    i = 1
    while i <= n0:
        p = g(p0)

        if (np.abs(p - p0) < TOL):
            break
        print("Iteration #",i,":",p)
        i+=1
        p0=p

    if(i==n0):
        print("Method failed after",i,"iterations.")
    else:
        print("The method is successful\n")

def h(x):
    return x**3 - 5*x**2 + 2*x + 1

def derive(x):
    return 3*x**2 - 10*x + 2

# Finding a root of the equation x^3 - 5x^2 + 2x + 1
def newtonraph_method(p_prev,TOL,n0):
    i=1
    while i <= n0:
        if derive(p_prev) != 0:
            p_next = p_prev - h(p_prev) / derive(p_prev)
            if abs(p_next - p_prev) < TOL:
                print("Success! The root is", p_next,"\n")
                return p_next
            p_prev = p_next
        else:
            print("Unsuccessful because the derivative is 0\n")
            return
        i += 1
    print("Unsuccessful after", i, "iterations\n")
    return


def main():
    approx_algorithm(1.5,0.000001)
    bisection_method(0,2,0.000001,20)
    fixedpoint_iteration(0.5,0.000001,100)
    newtonraph_method(2,0.000001,100)


main()
