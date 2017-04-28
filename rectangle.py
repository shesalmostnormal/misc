#! /usr/bin/env python
#coding: utf-8

from __future__ import division, print_function

"""
This program contains a class Rectangle that defines
length and width (two private member variables), their
respective functions, and a two-argument constuctor that
defaults to unit values.
"""

# Class definition

class Rectangle:

    def __init__(self, length = 1.0, width = 1.0):
        self.setLength(length)
        self.setWidth(width)

    def setLength(self,length):
        self.__il = length 
    
    def setWidth(self, width):
        self.__iw = width

    def l(self):
        return self.__il

    def w(self):
        return self.__iw

    def area(self):
        return self.l()*self.w()

    def circumference(self):
        return 2*self.l() + 2*self.w()

    def print(self): 
        print("(",self.l(),",",self.w(),")")

    def __add__(self,other):
        return Rectangle(self.l() + other.l(), self.w() + other.w())

### MAIN ###

R1 = Rectangle(20,10) # Length by width

print("Rectange with length and width")
R1.print()
print("Has an area of",R1.area())

R2 = Rectangle() # Default size for second rectangle

print("Addition of two rectangles is a rectangle with length and width")
(R1 + R2).print()