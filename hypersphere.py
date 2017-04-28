#! bin/usr/python
#coding: utf-8

from __future__ import division, print_function
import numpy as np
import numpy.random
from math import pi
import matplotlib.pyplot as plt

"""
Calculating the volume of a hypershpere uses the Monte Carlo method by generating random sample points to approximate the volume of sphere of d-dimensions from zero to twelve.
"""


# CONSTANTS

DMAX = 12           
POINTS = 1000000    
limitD1 = -1             
limitD2 = 1              

# FUNCTIONS

# Generates the random sample points and checks if it is in the sphere
def f(x):   

    mag = 0
    for i in range(len(x)):
        mag += x[i]**2
    if mag <= 1:
        return 1
    return 0

# Mean Value method for volume
def monteCarlo(D):    

    Integral = ((limitD2-limitD1)**D)/POINTS
    sum = 0
    for _ in range(POINTS):
        x = np.random.uniform(limitD1,limitD2,D)
        sum += f(x)
    return Integral*sum

# Make x and y values for d-dimensional sphere
def makeXY():

    X = np.linspace(0,DMAX,DMAX+1)
    Y = []
    for i in range(len(X)):
        Y.append(monteCarlo(X[i]))
        print(i, "  ", Y[i])
    return X, Y


X, Y = makeXY()

plt.plot(X,Y)
plt.title("Volume of n­dimensional­Sphere vs. n")
plt.ylabel("Volume")
plt.xlabel("Dimension")
plt.show()
