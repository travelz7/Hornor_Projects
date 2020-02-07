import numpy as np

arr4 = np.array([[1, 1000, 3000], [2, 20, 200], [3, 30, 300]])
print(arr4)
print('垂直方向计算数组的和：\n', np.sum(arr4, axis=0))
print('水平方向计算数组的和：\n', np.sum(arr4, axis=1))
