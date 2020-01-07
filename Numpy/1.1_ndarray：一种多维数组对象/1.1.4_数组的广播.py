import numpy as np

# 广播示例
a = np.array([[0.0, 0.0, 0.0], [10.0, 10.0, 10.0], [20.0, 20.0, 20.0],[30.0, 30.0, 30.0]])
b = np.array([1.0, 2.0, 3.0])
print('第一个数组：')
print(a)
print('\n第二个数组：')
print(b)
print('\n第一个数组加第二个数组：')
print(a + b)
