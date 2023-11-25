import numpy as np

a1 = np.array([1, 2, 3, 4])
a2 = np.array([[1,2, 3, 4],
               [5, 6, 7, 8]])

# 1x4 dimension array for the first zeroes one
b1 = np.zeros((1, 4))
b2 = np.zeros((2, 8))

arr1 = np.arange(10, dtype=float)
arr2 = np.arange(5, 12, 2, dtype=float) # start at 5, end at 12, skips 2, float dtype

print(arr2)
