import math
from sin_cos import Sin, Cos
from polynomial import Polynomial
import pytest

def test_sin():
    sin = Sin()
    assert str(sin) == "sin(x)"
    assert math.isclose(sin(math.pi / 2), math.sin(math.pi / 2))
    assert math.isclose(sin(0), math.sin(0))
    assert math.isclose(sin(math.pi), math.sin(math.pi))
    assert math.isclose(sin(3 * math.pi / 2), math.sin(3 * math.pi / 2))

def test_sin_derivative():
    sin = Sin()
    sin_derivative = sin.derivative()
    assert str(sin_derivative) == "cos(x)"
    assert math.isclose(sin_derivative(0), math.cos(0))
    assert math.isclose(sin_derivative(math.pi / 2), math.cos(math.pi / 2))
    assert math.isclose(sin_derivative(math.pi), math.cos(math.pi))
    
def test_cos():
    cos = Cos()
    assert str(cos) == "cos(x)"
    assert math.isclose(cos(0), math.cos(0))
    assert math.isclose(cos(math.pi / 2), math.cos(math.pi / 2))
    assert math.isclose(cos(math.pi), math.cos(math.pi))
    assert math.isclose(cos(3 * math.pi / 2), math.cos(3 * math.pi / 2))

def test_cos_derivative():
    cos = Cos()
    cos_derivative = cos.derivative()
    assert str(cos_derivative) == "(((-1) * 1) * sin(x))"
    assert math.isclose(cos_derivative(0), -math.sin(0))
    assert math.isclose(cos_derivative(math.pi / 2), -math.sin(math.pi / 2))
    assert math.isclose(cos_derivative(math.pi), -math.sin(math.pi))
    
def test_polynomial():
    poly = Polynomial(1, 0, -1)  # f(x) = 1 * 1 + 0 * x ^ 1 + (-1) * x ^ 2
    assert str(poly) == "(((1 * 1) + (0 * (x) ^ 1)) + ((-1) * (x) ^ 2))"
    assert math.isclose(poly(0), 1.0)
    assert math.isclose(poly(1), 0.0)
    assert math.isclose(poly(2), -3.0)

def test_polynomial_derivative():
    poly = Polynomial(1, 0, -1)
    poly_derivative = poly.derivative() 
    assert math.isclose(poly_derivative(1), -2.0)
    assert math.isclose(poly_derivative(3), -6.0)
    assert math.isclose(poly_derivative(5), -10.0)

def test_addition_of_two_trigonometric_functions():
    sin = Sin()
    cos = Cos()
    sum = sin + cos 
    assert str(sum) == "(sin(x) + cos(x))"
    assert math.isclose(sum(0), 1.0)
    assert math.isclose(sum(math.pi / 2), math.cos(math.pi / 2) + math.sin(math.pi / 2))
    sum_derivative = sum.derivative()
    assert str(sum_derivative) == "(cos(x) + (((-1) * 1) * sin(x)))" 
    assert math.isclose(sum_derivative(math.pi / 4), math.cos(math.pi / 4) - math.sin(math.pi / 4))

def test_addition_of_two_polynomials():
    poly1 = Polynomial(4, 5)  
    assert str(poly1) == "((4 * 1) + (5 * (x) ^ 1))"
    poly2 = Polynomial(1, 2) 
    assert str(poly2) == "((1 * 1) + (2 * (x) ^ 1))"
    addition = poly1 + poly2
    assert math.isclose(addition(1), 12.0)
    addition_derivative = addition.derivative()
    assert math.isclose(addition_derivative(8), 7.0)
    assert str(addition) == "(((4 * 1) + (5 * (x) ^ 1)) + ((1 * 1) + (2 * (x) ^ 1)))"

def test_addition_of_polynomial_and_trigonomteric_function():
    poly1 = Polynomial(5, 2)  
    assert str(poly1) == "((5 * 1) + (2 * (x) ^ 1))"
    cos = Cos()
    assert str(cos) == "cos(x)"
    addition = poly1 + cos
    assert str(addition) == "(((5 * 1) + (2 * (x) ^ 1)) + cos(x))"
    assert math.isclose(addition(0), 6.0)
    addition_derivative = addition.derivative()
    assert math.isclose(addition_derivative(0), 2.0)
    
def test_subtraction_of_trigonometric_function_and_polynomial():
    sin = Sin()
    poly = Polynomial(1, 3) 
    applied_sin = sin.apply(poly)
    cos = Cos()
    subtraction = applied_sin - cos
    assert str(subtraction) == "(sin(((1 * 1) + (3 * (x) ^ 1))) - cos(x))"
    assert math.isclose(subtraction(math.pi / 4), math.sin(1 + 3 * math.pi / 4) - math.cos(math.pi / 4))
    subtraction_derivative = subtraction.derivative()
    assert math.isclose(subtraction_derivative(0), 3 * math.cos(1) + math.sin(0))

def test_subtraction_of_two_trigonometric_functions():
    cos = Cos()
    sin = Sin()
    sub = cos - sin 
    assert str(sub) == "(cos(x) - sin(x))"
    assert math.isclose(sub(0), 1.0)
    assert math.isclose(sub(math.pi), math.cos(math.pi) - math.sin(math.pi))
    sub_derivative = sub.derivative()
    assert str(sub_derivative) == "((((-1) * 1) * sin(x)) - cos(x))" 
    assert math.isclose(sub_derivative(math.pi), -math.sin(math.pi) - math.cos(math.pi))

def test_subtraction_of_two_polynomials():
    poly1 = Polynomial(1, 2)  
    assert str(poly1) == "((1 * 1) + (2 * (x) ^ 1))"
    poly2 = Polynomial(3, 4) 
    assert str(poly2) == "((3 * 1) + (4 * (x) ^ 1))"
    sub = poly1 - poly2
    assert math.isclose(sub(1), -4.0)
    sub_derivative = sub.derivative()
    assert math.isclose(sub_derivative(8), -2.0)
    assert str(sub) == "(((1 * 1) + (2 * (x) ^ 1)) - ((3 * 1) + (4 * (x) ^ 1)))"

def test_multiplicationi_of_trigonometric_function():
    cos = Cos()
    sin = Sin()
    mul = cos * sin 
    assert str(mul) == "(cos(x) * sin(x))"
    assert math.isclose(mul(0), 0.0)
    assert math.isclose(mul(math.pi), math.cos(math.pi) * math.sin(math.pi))
    mul_derivative = mul.derivative()
    assert math.isclose(mul_derivative(math.pi), (-math.sin(math.pi) * math.sin(math.pi)) + (math.cos(math.pi) * math.cos(math.pi)))

def test_multiplication_of_two_polynomial_and_trigonometric_function():
    poly1 = Polynomial(2, 2) 
    poly2 = Polynomial(1, 2, 3) 
    cos = Cos()
    assert str(poly1) == "((2 * 1) + (2 * (x) ^ 1))"
    assert str(poly2) == "(((1 * 1) + (2 * (x) ^ 1)) + (3 * (x) ^ 2))"
    multiplication = poly1 * poly2 * cos
    assert str(multiplication) == "((((2 * 1) + (2 * (x) ^ 1)) * (((1 * 1) + (2 * (x) ^ 1)) + (3 * (x) ^ 2))) * cos(x))"
    assert math.isclose(multiplication(0), 2.0)

def test_division_of_trigonometric_functions():
    sin = Sin()
    cos = Cos()
    division = sin / cos
    assert str(division) == "(sin(x) / cos(x))"
    assert math.isclose(division(math.pi / 4), math.tan(math.pi / 4))
    division_derivative = division.derivative()
    assert str(division_derivative) == "(((cos(x) * cos(x)) - (sin(x) * (((-1) * 1) * sin(x)))) / (cos(x) * cos(x)))"
    assert math.isclose(division_derivative(math.pi / 4), 2.0)

def test_division_of_two_polynomials():
    poly1 = Polynomial(2, 1) 
    poly2 = Polynomial(3, 3, 3) 
    div = poly1 / poly2
    assert str(poly1) == "((2 * 1) + (1 * (x) ^ 1))"
    assert str(poly2) == "(((3 * 1) + (3 * (x) ^ 1)) + (3 * (x) ^ 2))"
    assert str(div) == "(((2 * 1) + (1 * (x) ^ 1)) / (((3 * 1) + (3 * (x) ^ 1)) + (3 * (x) ^ 2)))"
    assert math.isclose(div(0), 2 / 3)

def test_composition_of_trigonometric_functions():
    sin = Sin()
    cos = Cos()
    applied = sin.apply(cos)
    assert str(applied) == "sin(cos(x))"
    assert math.isclose(applied(math.pi / 2), 0.0, abs_tol=1e-9)
    applied_derivative = applied.derivative()
    assert str(applied_derivative) == "(cos(cos(x)) * (((-1) * 1) * sin(x)))"
    apply_sin = applied_derivative.apply(sin)
    assert str(apply_sin) == "(cos(cos(sin(x))) * (((-1) * 1) * sin(sin(x))))"

def test_composition_of_trigonometric_function_and_polynomial():
    sin = Sin()
    poly = Polynomial(2, 1, 1) 
    assert str(poly) == "(((2 * 1) + (1 * (x) ^ 1)) + (1 * (x) ^ 2))"
    applied = sin.apply(poly)
    assert str(applied) == "sin((((2 * 1) + (1 * (x) ^ 1)) + (1 * (x) ^ 2)))"
    assert math.isclose(applied(math.pi / 2), math.sin(2 + math.pi / 2 + (math.pi / 2 * math.pi / 2)))
    assert math.isclose(applied(math.pi), math.sin(2 + math.pi + (math.pi * math.pi)))
   
def test_with_all_functionality():
    sin = Sin()
    cos = Cos()
    tg = sin / cos
    assert math.isclose(tg(math.pi / 4), 1.0)
    tg_ = tg.derivative() # 
    assert str(tg_) == "(((cos(x) * cos(x)) - (sin(x) * (((-1) * 1) * sin(x)))) / (cos(x) * cos(x)))"
    assert math.isclose(tg_(math.pi / 4), 2.0)

    x_2 = Polynomial(0, 0, 1)  # 0 * 1 + 0 * x + 1 * x ^ 2
    assert str(x_2) == "(((0 * 1) + (0 * (x) ^ 1)) + (1 * (x) ^ 2))"
    assert math.isclose(x_2(12), 144.0)
   
    sin_2 = x_2.apply(sin)
    assert str(sin_2) == "(((0 * 1) + (0 * (sin(x)) ^ 1)) + (1 * (sin(x)) ^ 2))"
    assert math.isclose(sin_2(3 * math.pi / 2), 1.0)
    cos_x_2 = cos.apply(x_2)  
    assert str(cos_x_2) == "cos((((0 * 1) + (0 * (x) ^ 1)) + (1 * (x) ^ 2)))"
    assert math.isclose(cos_x_2(-math.sqrt(math.pi)), -1.0)

if __name__ == "__main__":
    pytest.main()

