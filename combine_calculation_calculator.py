import numpy as np

# Coefficients of the equations
# Example: 2x + 3y = 8 and 3x + 4y = 11
A = np.array([[2, 3], [3, 4]])
B = np.array([8, 11])

# Solving the system of equations
solution = np.linalg.solve(A, B)

print("Solution:")
print(f"x = {solution[0]}")
print(f"y = {solution[1]}")
