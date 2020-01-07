import numpy as np

# Numpy提供了一些针对ndarray的基本集合运算
# 唯一化，np.unique
names = np.array(['zs', 'grf', 'lmc', 'ylt', 'xj', 'jyq', 'yxx', 'tr'])
print(np.unique(names))
ints = np.array([1, 1, 1, 2, 2, 3, 3, 3, 4])
print(np.unique(ints))

# np.in1d用于测试一个数组中的值在另一个数组中的成员资格，返回一个布尔型数组
values = np.array([6, 0, 0, 3, 2, 5, 6])
print(np.in1d(values, [2, 3, 6]))