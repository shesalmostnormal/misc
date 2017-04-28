#! /usr/bin/env python
# coding: utf-8

from __future__ import print_function,division
from math import sin,pi
from numpy import array,arange
from pylab import plot,xlabel,show

"""
This program implements the fourth-order
Runge-Kutta method for the nonlinear pendulum
equations. Plots are generated showing both
theta as a function of time and dtheta/dt as a 
function of theta.
"""

# Constants
g = 9.81
l = 0.1

# NOnlinear Pendulum
def f(r,t):
	theta = r[0]
	omega = r[1]
	ftheta = omega
	fomega = -(g/l)*sin(theta)
	return array([ftheta,fomega],float)

# Initial Conditions
a = 0.0
b = 5.0
N = 1000
h = (b-a)/N

tpoints = arange(a,b,h)
thetapoints = []
omegapoints = []

# RUnge-Kutta method
r = array([10.0*pi/180.0,0.0],float)
for t in tpoints:
	thetapoints.append(r[0])
	omegapoints.append(r[1])
	k1 = h * f(r,t)
	k2 = h * f(r+0.5*k1,t+0.5*h)
	k3 = h * f(r+0.5*k2,t+0.5*h)
	k4 = h * f(r+k3,t+h)
	r += (k1+2*k2+2*k3+k4)/6

#PLotting
plot(tpoints,thetapoints)
plot(tpoints,omegapoints)
show() 
