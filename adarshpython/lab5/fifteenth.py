import numpy as np
from scipy.optimize import minimize

# Define the function
def f(v):
    x,y=v[0],v[1]
    return (x-2)**2 + (y-2)**2

result = minimize(f,[0,0])

# Display the result
print("Optimization Result")
print("Minimum value of f(x,y)=(x-2)^2+(y-2)^2: ", np.round(result.fun,1))
print("x, y =",np.round(result.x,1))
print("Success =", result.success)