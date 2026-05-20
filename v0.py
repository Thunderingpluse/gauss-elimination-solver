import numpy as np

def gauss_elimination(A, b):
    n = len(b)
    matrix = np.hstack((A, b.reshape(-1, 1))).astype(float)

    for i in range(n):
        max_row = np.argmax(abs(matrix[i:n, i])) + i
        matrix[[i, max_row]] = matrix[[max_row, i]]

        for j in range(i + 1, n):
            factor = matrix[j][i] / matrix[i][i]
            matrix[j, i:] -= factor * matrix[i, i:]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (matrix[i, n] - np.dot(matrix[i, i+1:n], x[i+1:n])) / matrix[i, i]
    
    return x

A = np.array([[1, 1, 1], [2, 3, 7], [1, 3, -2]])
b = np.array([6, 29, 1])

solution = gauss_elimination(A, b)
print(f"Solution: {solution}")