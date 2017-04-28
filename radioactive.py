#! /usr/bin/env python
#coding: utf-8 

from __future__ import division, print_function
from numpy import exp, arange
import matplotlib.pyplot as plt

"""
This program numerically solves for the dependence of N(t)
through a range of time values. As h gets bigger, the values
of the N(t) function have more decimal places to improve
accuracy and make the curve smoother.
"""

tau = 2.0 # s
h = [1.0,0.1,0.01]
N0 = 1

def N(t):
	return N0 * exp(-t/tau)

def N2(a,h):
	return a*(1 - h/tau)

for i in range(len(h)):
	t = arange(0,15,h[i])
	N_i = [N0]

	for j in range(len(t) - 1):
		N_i += [N2(N_i[j],h[i])]

	plt.plot(t,N_i)
	plt.title("Radioactive Decay")
	plt.xlabel("t")
	plt.ylabel("N(t)")
plt.show()

