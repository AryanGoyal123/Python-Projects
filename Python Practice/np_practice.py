import numpy as np

a1 = np.array([1, 2, 3, 4])
a2 = np.array([[1, 2, 3, 4],
               [5, 6, 7, 8]])

# 1x4 dimension array for the first zeroes one
b1 = np.zeros((1, 4))
b2 = np.zeros((2, 8))

arr1 = np.arange(10, dtype=float)
arr2 = np.arange(5, 12, 2, dtype=float)  # start at 5, end at 12, skips 2, float dtype

matrix = np.arange(12).reshape(2, 6)  # reshape to 2x6 matrix

# creating learning rate values for ML
learning_rates = np.arange(0.01, 0.1, 0.01)

# little different, but to create a proper spacing
arr3 = np.linspace(0, 1, 5)
# output: [0.   0.25 0.5  0.75 1.  ]

# np.dot for matrix multiplication
# transpose just switches the columns and rows
# important for matrix multiplication because (2,5) can only multiply with (5, 2)
arr11 = np.arange(10).reshape(2, 5)
arr12 = np.arange(10).reshape(2, 5).transpose()
# np.dot(arr11, arr12)

# inverse and eigen values and vectors of a matrix
arr13 = np.arange(2, 19, 2).reshape(3, 3)
# print(np.linalg.inv(arr13))
# print(np.linalg.eig(arr13))
