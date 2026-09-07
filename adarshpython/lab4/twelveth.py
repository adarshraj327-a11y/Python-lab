import numpy as np

# Define the matrix
A = np.array([[4, 1],
              [2, 3]])

print("Matrix A:")
print(A)

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Display eigenvalues
print("\nEigenvalues:")
print(eigenvalues)

# Display eigenvectors
print("\nEigenvectors:")
print(eigenvectors)