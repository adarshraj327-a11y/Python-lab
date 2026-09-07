import numpy as np

# -------------------------------
# Input Matrices
# -------------------------------
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)


# =================================
# WITHOUT NUMPY
# =================================

# Addition
add = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    add.append(row)

# Subtraction
sub = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] - B[i][j])
    sub.append(row)

# Multiplication
mul = [[0 for j in range(len(B[0]))] for i in range(len(A))]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            mul[i][j] += A[i][k] * B[k][j]

# Transpose
trans = []
for j in range(len(A[0])):
    row = []
    for i in range(len(A)):
        row.append(A[i][j])
    trans.append(row)

print("\n--- Without NumPy ---")
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Transpose of A:", trans)


# =================================
# USING NUMPY
# =================================

A_np = np.array(A)
B_np = np.array(B)

print("\n--- Using NumPy ---")

print("Addition:")
print(A_np + B_np)

print("Subtraction:")
print(A_np - B_np)
print("Multiplication:")
print(np.dot(A_np, B_np))

print("Transpose of A:")
print(A_np.T)
