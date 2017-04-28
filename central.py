#! /usr/bin/env python
# coding: utf-8

from __future__ import division, print_function
from numpy import tanh, cosh, vectorize, linspace
import matplotlib.pyplot as plt

"""
This program creates a generic function which uses the central
difference to calculate the derivative of a given function f(x) at
a given x. 
"""


# Central derivative formula
def derivative(func, x):
	h = 1*10**-8
	return (func(x + 0.5*h) - func(x - 0.5*h))/h

# Function in question
def f(x):
	return 1 + 0.5*(tanh(2*x))

# Derivative of function in question
def f_p(x):
	return cosh(2*x)**-2

# Vectors
d_vector = vectorize(derivative)
f_vector = vectorize(f)
f_p_vector = vectorize(f_p)

N = 100
a = 2
b = -2

x = linspace(a,b,N)

f_plot = f_vector(x)
d_plot = d_vector(f_vector,x)
f_p_plot = f_p_vector(x)

plt.plot(x,f_plot)
plt.plot(x,d_plot)
plt.plot(x,f_p_plot)

plt.show()