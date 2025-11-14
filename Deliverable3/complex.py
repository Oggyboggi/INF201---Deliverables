"""""
Task 1

Complex Class
"""""
import math


class Complex:
    # Constructor
    def __init__(self, re, im=0):
        self.re = re
        self.im = im
        
    # Representation
    def __repr__(self):
        return f"Complex({self.re}, {self.im})"
    
    # String conversion
    def __str__(self):
        sign = "+" if self.im >= 0 else "-"
        return f"{self.re}{sign}{abs(self.im)}i"
    
    # Addition
    def __add__(self, rhs):
        return Complex(self.re + rhs.re, self.im + rhs.im)
    
    # Subtraction
    def __sub__(self, rhs):
        return Complex(self.re - rhs.re, self.im - rhs.im)
    
    # Multiplication
    def __mul__(self, rhs):
        if isinstance(rhs, Complex):
            re = self.re * rhs.re - self.im * rhs.im
            im = self.re * rhs.im + self.im * rhs.re
            return Complex(re, im)
        elif isinstance(rhs, (int, float)):
            return Complex(self.re * rhs, self.im * rhs)
        else:
            return NotImplemented
        
    # Scalarmultiplication
    def __rmul__(self, lhs):
        return self * lhs
    
    # Equality
    def __eq__(self, rhs):
        if isinstance(rhs, Complex):
            return self.re == rhs.re and self.im == rhs.im
        return False
