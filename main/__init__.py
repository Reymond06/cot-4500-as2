# Reymond Ramirez
# COT4500
# Assignment 1
import math
import numpy as np


def approx_algorithm(initial,tolerance):
    iterations=0
    diff = initial
    x = initial
    print(iterations,":",initial)
    while (diff>=tolerance):
        iterations+=1
        y=x
        x = # Insert function you want here
        diff = abs(y-x)
        print(iterations,":",x)
    
    print("Convergence after",iterations,"iterations\n")


def f(x):
    return #Insert function you want here

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
    return # Insert function you want here

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
    return # Insert function you want here

def derive(x):
    return # Insert derivative function of h(x)

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
    approx_algorithm(null_value,tolerance_value)
    bisection_method(a,b,tol,maximum)
    fixedpoint_iteration(initial_approximation,error_tol,max_iter)
    newtonraph_method(initial_approx,tol,maximum_iteration)

main()
