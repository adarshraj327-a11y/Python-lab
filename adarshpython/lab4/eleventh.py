import numpy as np

# Input matrix
A = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])

print("Matrix A:")
print(A)

# Determinant
det = np.linalg.det(A)
print("\nDeterminant of A:")
print(round(det, 2))

# Inverse
if det != 0:
    inverse = np.linalg.inv(A)
    print("\nInverse of A:")
    print(inverse)
else:
    print("\nInverse does not exist because the determinant is zero.")

# Rank
rank = np.linalg.matrix_rank(A)
print("\nRank of A:")
print(rank)