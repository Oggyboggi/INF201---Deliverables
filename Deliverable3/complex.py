
import math

class Complex:
    def __init__(self, re, im=0):
        self.re = re
        self.im = im
        
    def __repr__(self):
        return f'Complex({self.re}, {self.im})'
    
    def __add__(self, rhs):
        return Complex(self.re + rhs.real, self.im + rhs.imag)
    
    def __sub__(self, rhs):
        return Complex(self.re - rhs.real, self.im - rhs.imag)
    
    def __mul__(self, rhs):
        if isinstance(rhs, complex):
            re = self.re * rhs.real - self.im * rhs.imag
            im = self.re * rhs.imag + self.im * rhs.real
            return Complex(re, im)
        return Complex(self.re * rhs, self.im * rhs)
    
    def __rmul__(self, lhs):
        return self * lhs
    
    def __eq__(self, rhs):
        if isinstance(rhs, Complex):
            return self.re == rhs.re and self.im == rhs.im
    
    def __str__(self):
        return f'({self.re} + {self.im}i)' if self.im >= 0 else f'({self.re} - {-self.im}i)'






"""
class Vector():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, rhs):
        return Vector(self.x + rhs.x, self.y + rhs.y)

    def __sub__(self, rhs):
        return Vector(self.x - rhs.x, self.y - rhs.y)

    def __mul__(self, rhs):
        return Vector(self.x * rhs, self.y * rhs)

    def __rmul__(self, lhs):
        return self * lhs

    def __truediv__(self, rhs):
        return self * (1. / rhs)

    def norm(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
        
"""
