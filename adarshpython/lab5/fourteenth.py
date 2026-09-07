import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Given data points
x = np.array([1, 2, 3, 4, 5, 6], dtype=float)
y = np.array([6, 17, 34, 57, 86, 121], dtype=float)

# Define second-degree polynomial
def quadratic(x, a, b, c):
    return a * x**2 + b * x + c

# Fit the data using SciPy curve_fit
popt, pcov = curve_fit(quadratic, x, y)

# Get polynomial coefficients
a, b, c = popt

# Display coefficients
print("Estimated Polynomial Coefficients:")
print("a =", round(a, 4))
print("b =", round(b, 4))
print("c =", round(c, 4))

# Display fitted polynomial
print("\nFitted Polynomial:")
print("y = {:.4f}x^2 + {:.4f}x + {:.4f}".format(a, b, c))

# Generate values for fitted curve
x_fit = np.linspace(1, 6, 200)
y_fit = quadratic(x_fit, a, b, c)

# Plot original data points
plt.scatter(x, y, color="red", label="Original Data")

# Plot fitted curve
plt.plot(x_fit, y_fit, color="blue", label="Fitted Curve")

# Add labels and title
plt.xlabel("x")
plt.ylabel("y")
plt.title("Second-Degree Polynomial Fitting")

plt.legend()
plt.grid(True)
plt.show()