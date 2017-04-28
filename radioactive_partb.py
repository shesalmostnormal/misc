#! /usr/bin/env python
#coding: utf-8 

from __future__ import division, print_function
from numpy import exp, arange
import matplotlib.pyplot as plt

"""
This program plots the time dependence of N(t) for different
values of tau. When tau is too big, the change in N(t) over
time is a lot bigger than when tau is too small (which N(t)
is seen to behave as a constant.)
"""

tau = [5.0,3.0,1.0,0.1,0.01]
h = 0.01
N0 = 1

def N(t,tau):
	return N0 * exp(-t/tau)

def N2(a,tau):
	return a*(1 - h/tau)

for i in range(len(tau)):
	t = arange(0,15,h)
	N_i = [N0]

	for j in range(len(t) - 1):
		N_i += [N2(N_i[j],tau[i])]

	plt.plot(t,N_i) 
	plt.title("Radioactive Decay")
	plt.xlabel("t")
	plt.ylabel("N(t)")
plt.show()

