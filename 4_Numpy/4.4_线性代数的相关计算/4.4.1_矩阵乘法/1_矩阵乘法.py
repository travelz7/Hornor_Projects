import numpy as np

# 一维数组的点积
vector_dot = np.dot(np.array([1, 2, 3]), np.array([4, 5, 6]))
print('一维数组的点积：\n', vector_dot)
# 二维数组的乘法
arr10 = np.arange(12).reshape(4, 3)
arr11 = np.arange(101, 113).reshape(3, 4)
print('两个二维数组：')
print(arr10)
print(arr11)
arr2d = np.dot(arr10, arr11)
print('二维数组的乘法：\n', arr2d)
