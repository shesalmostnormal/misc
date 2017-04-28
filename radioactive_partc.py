#! /usr/bin/env python
#coding: utf-8 

from __future__ import division, print_function
from numpy import exp, arange
import matplotlib.pyplot as plt

"""
This program numerically solves coupled equations of parent
and daughter nucleus radioactive decay.

a) tauP >> tauD: No change in N(t) over time. The small tauD
value in the exponential is what makes the entire function
behave constant.
b) tauP = tauD: A maximum is reached then proceeds to decrease
at a similar rate.
c) tauP << tauD: Very fast change over short amount of time. Due
to the large tauD, the exponential reaches a maximum then
stabalizes.
"""

### Constants ###

tauP = 2.0 # s
tauD = [0.02,2.0,200.0] # s
h = 0.01
Np0 = 1
Nd0 = 0

### Functions ###

def N(t):
	return Np0*exp(-t/tau)

# Parent nucleus
def Np(a):
	return a*(1-h/tauP)

# Daughter nucleus
def Nd(b,a,tauD):
	return b + (h/tauP)*a - (h/tauD)*b

for i in range(len(tauD)):
	t = arange(0,20,h)

	Np_i = [Np0]
	Nd_i = [Nd0]

	for j in range(len(t)-1):
		Np_i += [Np(Np_i[j])]

	for k in range(len(t)-1):
		Nd_i += [Nd(Nd_i[k],Np_i[k],tauD[i])]

	plt.plot(t,Np_i) 
	plt.title("Radioactive Decay")
	plt.xlabel("t")
	plt.ylabel("N(t)")
	plt.plot(t,Nd_i)
plt.show()