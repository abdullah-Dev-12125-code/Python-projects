import numpy as np

A = np.array([[1,2,3],[2,5,6],[7,-1,2]])
B = np.array([[3,2,-8],[2,7,-7],[7,-1,2]])

print("Sum:\n", A+B)
print("Difference:\n", A-B)
print("Product:\n", A@B)
