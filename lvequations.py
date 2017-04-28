#! /usr/bin/env python
# coding: utf-8

from math import sin
from numpy import array,arange
from pylab import plot,xlabel,show

"""
This program implements the fourth-order
Runge-Kutta method for the Lotka-Volterra
equations. Plots are generated showing both
x and y as a function of time.
"""

# Constants
alpha = 1.0
beta = gamma = 0.5
delta = 0.2

# Lotka-Volterra equations
def f(r,t):
	x = r[0]
	y = r[1]
	fx = alpha*x - beta*x*y
	fy = gamma*x*y - delta*y
	return array([fx,fy],float)

# Initial conditions
a = 0.0
b = 30.0
N = 1000
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []
ypoints = []

# Runge-Kutta method
r = array([2.0,2.0],float)
for t in tpoints:
	xpoints.append(r[0])
	ypoints.append(r[1])
	k1 = h * f(r,t)
	k2 = h * f(r+0.5*k1,t+0.5*h)
	k3 = h * f(r+0.5*k2,t+0.5*h)
	k4 = h * f(r+k3,t+h)
	r += (k1+2*k2+2*k3+k4)/6

# Plot of x vs. t and y vs. t
plot(tpoints,xpoints)
plot(tpoints,ypoints)
xlabel("t")
show() 