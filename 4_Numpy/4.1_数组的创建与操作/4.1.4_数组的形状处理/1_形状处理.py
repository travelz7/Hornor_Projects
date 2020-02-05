import numpy as np
arr3 = np.array([[1, 5, 7], [3, 6, 1], [2, 4, 8], [5, 8, 9], [1, 5, 9], [8, 5, 2]])
print(arr3)
print(arr3.shape)

print(arr3.reshape(2, 9))
print(arr3.shape)

print(arr3.resize(2, 9))
print(arr3.shape)
print(arr3)