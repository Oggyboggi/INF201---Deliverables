"""
Task1

Complex class

Created by Iver Rannug Fossan and Oscar Wiersdalen Thunold
"""


class Complex:
    def __init__(self, real, imag=0):
        self.real = real
        self.imag = imag
        
    # Representation methods
    def __repr__(self):
        return f"Complex({self.real}, {self.imag})"
    
    # String representation
    def __str__(self):
        if self.imag < 0:
            return f"{self.real}{self.imag}i"
        else:
            return f"{self.real}+{self.imag}i"
        
    # Equality check
    def __eq__(self, other):
        if not isinstance(other, Complex):
            return NotImplemented
        return self.real == other.real and self.imag == other.imag
    
    # Arithmetic operations
    def __add__(self, other):
        if not isinstance(other, Complex):
            return NotImplemented
        return Complex(self.real + other.real, self.imag + other.imag)
    
    # Subtraction
    def __sub__(self, other):
        if not isinstance(other, Complex):
            return NotImplemented
        return Complex(self.real - other.real, self.imag - other.imag)
    
    # Multiplication
    def __mul__(self, other):
        if isinstance(other, Complex):
            a, b = self.real, self.imag
            c, d = other.real, other.imag
            return Complex(a*c - b*d, a*d + b*c)
        elif isinstance(other, (int, float)):
            return Complex(self.real * other, self.imag * other)
        return NotImplemented
    
    # Reverse multiplication for scalar * Complex
    def __rmul__(self, other):
        return self.__mul__(other)

