import numpy as np

# 计算偏回归系数
X = np.array([[1, 1, 4, 3], [1, 2, 7, 6], [1, 2, 6, 6], [1, 3, 8, 7], [1, 2, 5, 8],
             [1, 3, 7, 5], [1, 6, 10, 12], [1, 5, 7, 7], [1, 6, 3, 4], [1, 5, 7, 8]])
Y = np.array([3.2, 3.8, 3.7, 4.3, 4.4, 5.2, 6.7, 4.8, 4.2, 5.1])
X_trans_X_inverse = np.linalg.inv(np.dot(np.transpose(X), X))
beta = np.dot(np.dot(X_trans_X_inverse, np.transpose(X)), Y)
print('偏回归系数为：\n', beta)