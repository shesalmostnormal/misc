#! /usr/bin/env python
# coding: utf-8

from __future__ import print_function,division
from math import cos,pi
from numpy import array,arange
from pylab import plot,xlabel,show

"""
This program implements the fourth-order
Runge-Kutta method for the short spring
equations. Plots are generated showing both
x as a function of time and the phase space,
along with varying parameters B and b_c.
"""

# Constants
A = 1
w_d = 1
B = [7,7,10,7]
b_c = [6,0.6,0.05,0.01]

def f(r,t,i):
	x1 = r[0]
	x2 = r[1]
	f1 = x2
	f2 = -A*x1**3 - b_c[i]*x2 - B[i]*cos(w_d*t)
	return array([f1,f2],float)

a = 0.0
b = 25.0
N = 1000
h = (b-a)/N

tpoints = arange(a,b,h)

r = array([3.0,0.0],float)
for i in range(len(B)):
	x1points = []	
	x2points = []	
	for t in tpoints:
		x1points.append(r[0])
		x2points.append(r[1])
		k1 = h * f(r,t,i)
		k2 = h * f(r+0.5*k1,t+0.5*h,i)
		k3 = h * f(r+0.5*k2,t+0.5*h,i)
		k4 = h * f(r+k3,t+h,i)
		r += (k1+2*k2+2*k3+k4)/6
	plot(tpoints,x1points)
	plot(x2points,x1points)
	show() 
