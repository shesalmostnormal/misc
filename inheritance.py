#! /usr/bin/env python
#coding:utf-8

from __future__ import division, print_function
from numpy import sqrt,arctan

"""
Performing vector operations (dot and cross products, addition,
subtraction, magnitude, calculation of theta and phi angles)
utilizing classes in object-oriented programming.
"""

# Class definitions

class Vector2D:

    def __init__(self, aX = 0.0, aY = 0.0):
        self.setX(aX)
        self.setY(aY)

    def setX(self,aX):
        self.__iX = aX

    def setY(self,aY):
        self.__iY = aY

    def x(self):
        return self.__iX

    def y(self):
        return self.__iY

    def __add__(self,other):
        return Vector2D(self.x() + other.x(), self.y() + other.y())

    def __mul__(self, other):
        return (self.x()*other.x() + self.y()*other.y())

    def print(self):
        print("(",self.x(),",",self.y(),")")

class Vector3D(Vector2D):

    def __init__(self,aX,aY,aZ):
        self.setX(aX)
        self.setY(aY)
        self.setZ(aZ)

    def setZ(self, aZ):
        self.__iZ = aZ

    def z(self):
        return self.__iZ

    def mag(self):
        return sqrt((self.x()**2 + self.y()**2 + self.z()**2))

    def cos_theta(self):
        return (self.z())/(self.mag())

    def phi(self):
        return arctan(self.z())/(self.x())

    def __add__(self,other):
        return Vector3D(self.x() + other.x(), self.y() + other.y(), self.z() + other.z())

    def __sub__(self,other):
        return Vector3D(self.x() - other.x(), self.y() - other.y(), self.z() - other.z())

    def __mul__(self, other):
        return Vector3D(self.x() - other.x(), self.y() - other.y(), self.z() - other.z())

    def __truediv__(self, other):
        return Vector3D(self.y()*other.z() - self.z()*other.y(), self.x()*other.z() - self.z()*other.x(),self.x()*other.y() - self.y()*other.x())

    def print(self):
        print("(",self.x(),",",self.y(),",",self.z(),")")

### MAIN ###

A = Vector3D(2,3,4)

print("Vector A is")
A.print()
print("Magnitude is", A.mag())
print("Cosine angle theta is",A.cos_theta())
print("Phi value is",A.phi())

B = Vector3D(3,4,5)

print("Vector B is")
B.print()
print("Dot product of A and B is")
(A*B).print()
print("Addition of A and B is")
(A+B).print()
print("Subtraction of A and B is")
(A-B).print()
print("Cross product of A and B is")
(A/B).print()