
import numpy as np

# Coefficients of the equations
A = np.array([
    [2, 1],
    [1, 3]
])

# Results on the right side of the equations
b = np.array([12, 15])

# Solve the equations
solution = np.linalg.solve(A, b)

print("Solution:", solution)
print("Check the equations:", A @ solution)
