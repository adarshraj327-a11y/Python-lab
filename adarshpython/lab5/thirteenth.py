import numpy as np
from scipy.misc import derivative
from scipy.integrate import quad

def f(x):
    return x**3 + 2*x**2 - 5*x + 1

print("\nNumerical Differentiation\n")
print("f(x) = x^3 + 2x^2 - 5x + 1")
x = float(input("Enter the value of x for differentiation: "))
d = derivative(f, x, dx=1e-6)
print("Derivative at x =", x, "is", d)

print("\nNumerical Integration\n")
print("f(x) = x^3 + 2x^2 - 5x + 1")
a = float(input("\nEnter lower limit of integration: "))
b = float(input("Enter upper limit of integration: "))
result, error = quad(f, a, b)
print("Integral from", a, "to", b, "=", result)
print("Estimated error =", error)