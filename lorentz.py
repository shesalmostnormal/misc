#! /usr/bin/env python
# coding: utf-8

from __future__ import print_function,division
from math import sin
from numpy import array,arange
from pylab import plot,xlabel,ylabel,show

"""
This program implements the fourth-order
Runge-Kutta method for the Lorenz
equations. Plots are generated showing both 
y as a function of time, and z against x (also
known as the strange attractor).
"""

# Constants
sigma = 10.
r_c = 28.
b_c = 8./3.

# Lorenz
def f(r,t):
	x = r[0]
	y = r[1]
	z = r[2]
	fx = sigma*(y - x)
	fy = r_c*x - y - x*z
	fz = x*y - b_c*z
	return array([fx,fy,fz],float)

# Initial conditions
a = 0.0
b = 50.0
N = 10000
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []
ypoints = []
zpoints = []

# Runge-Kutta method
r = array([0.0,1.0,0.0],float)
for t in tpoints:
	xpoints.append(r[0])
	ypoints.append(r[1])
	zpoints.append(r[2])
	k1 = h * f(r,t)
	k2 = h * f(r+0.5*k1,t+0.5*h)
	k3 = h * f(r+0.5*k2,t+0.5*h)
	k4 = h * f(r+k3,t+h)
	r += (k1+2*k2+2*k3+k4)/6

# Plotting
plot(tpoints,ypoints)
xlabel("t")
ylabel("y")
show()
plot(zpoints,xpoints)
xlabel("z")
ylabel("x")
show()