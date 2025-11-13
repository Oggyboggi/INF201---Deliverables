"""
Created by Iver Rannug Fossan and Oscar Wiersdalen Thunold
"""

# test_complex.py

from complex import Complex

# --- Konstruksjon og representasjon ---

def test_constructor_defaults():
    z = Complex()
    assert z.re == 0
    assert z.im == 0

def test_constructor_only_real():
    z = Complex(5)
    assert z.re == 5
    assert z.im == 0

def test_str():
    assert str(Complex(1, 2)) == "1+2i"
    assert str(Complex(3, -4)) == "3-4i"
    assert str(Complex(0, 0)) == "0+0i"

def test_repr():
    z = Complex(1, 2)
    assert repr(z) == "Complex(1, 2)"


# --- Felt-tilgang ---

def test_re_im_properties():
    z = Complex(7, -8)
    assert z.re == 7
    assert z.im == -8


# --- Aritmetikk mellom komplekse tall ---

def test_addition():
    z = Complex(1, 2)
    y = Complex(3, 4)
    s = z + y
    assert s.re == 4
    assert s.im == 6

def test_subtraction():
    z = Complex(1, 2)
    y = Complex(3, 4)
    d = z - y
    assert d.re == -2
    assert d.im == -2

def test_multiplication():
    z = Complex(1, 2)
    y = Complex(3, 4)
    p = z * y
    # (1+2i)(3+4i) = -5 + 10i
    assert p.re == -5
    assert p.im == 10


# --- Aritmetikk med tall (int) ---

def test_add_scalar_left_and_right():
    z = Complex(1, 2)
    s1 = z + 3
    s2 = 3 + z
    assert s1.re == 4 and s1.im == 2
    assert s2.re == 4 and s2.im == 2

def test_mul_scalar_left_and_right():
    z = Complex(1, 2)
    m1 = z * 3
    m2 = 3 * z
    assert m1.re == 3 and m1.im == 6
    assert m2.re == 3 and m2.im == 6


# --- Sammenligning ---

def test_equality_and_inequality():
    z = Complex(1, 2)
    y = Complex(3, 4)
    z2 = Complex(1, 2)

    assert (z == y) is False
    assert (z != y) is True
    assert (z == z2) is True
    assert (z != z2) is False


# --- Eksempel fra oppgaveteksten ---

def test_example_from_spec():
    # Complex(2, -3) * Complex(2, 3) = 13 + 0i
    z = Complex(2, -3) * Complex(2, 3)
    assert z.re == 13
    assert z.im == 0
