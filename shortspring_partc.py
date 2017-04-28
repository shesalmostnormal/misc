#! /usr/bin/env python
# coding: utf-8

from __future__ import print_function,division
from math import cos,pi
from numpy import array,arange
from pylab import plot,xlabel,show, scatter

""" 
This program implements the fourth-order
Runge-Kutta method for the short spring
equations. Plots are generated showing both
x as a function of time and the phase space.
"""

# Constants
A = 1
w_d = 1
B = 7
b_c = 0.01

def f(r,t):
	x1 = r[0]
	x2 = r[1]
	f1 = x2
	f2 = -A*x1**3 - b_c*x2 - B*cos(w_d*t)
	return array([f1,f2],float)

a = 0
b = 25000*2*pi # Period = 2*pi/w_d
N = 360*(b-a)/2*pi
h = (b-a)/N

tpoints = arange(a,b,h)
x1points = []
x2points = []

xpoin = []
dxpoin = []

r = array([3.0,0],float)
for t in tpoints:
	if 0 <= t%(2*pi) < h:
		xpoin.append(r[0])
		dxpoin.append(r[1])
	x1points.append(r[0])
	x2points.append(r[1])
	k1 = h * f(r,t)
	k2 = h * f(r+0.5*k1,t+0.5*h)
	k3 = h * f(r+0.5*k2,t+0.5*h)
	k4 = h * f(r+k3,t+h)
	r += (k1+2*k2+2*k3+k4)/6

scatter(xpoin,dxpoin, s=1)
show()
