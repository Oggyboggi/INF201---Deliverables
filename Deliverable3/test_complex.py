"""
Testsuite for Complex class.

Created by Iver Rannug Fossan and Oscar Wiersdalen Thunold
"""

from complex import Complex

def test():
    assert repr(Complex(1,2)) == "Complex(1, 2)"
    
    # Test __repr__
    assert  str(Complex(1,2)) == "1+2i"
    assert str(Complex)(1,-3) == "1-3i"
    assert str(complex(5)) == "5+0i"

    # Test addition
    assert Complex(1,2) + Complex(3,4) == Complex(4,6)
    
    # Test subtraction
    assert Complex(1,2) - Complex(3,4) == Complex(-2,-2)
                                                  
    # Test multiplication
    z = Complex(1,2)
    y = Complex(3,4)
    assert z * y == Complex(1*3 - 2*4, 1*4 + 2*3)
    
    # Test scalar multiplication
    assert Complex(2,3) * 3 == Complex(6,9)
    assert 3 * Complex(2,4) == Complex(6,9)
    
    # Test equality
    assert Complex(1,2) == Complex(1,2)
    assert Complex(1,2) != Complex(2,1)