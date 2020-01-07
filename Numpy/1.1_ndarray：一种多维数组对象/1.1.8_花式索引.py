import numpy as np

# 花式索引是一个Numpy术语，它指的是利用整数数组进行索引
arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i;
print(arr)
# 为了以特定顺序选取行子集，只需传入一个用于指定顺序的整数列表或ndarray
print(arr[[4, 3, 2, 1]])
# 使用负数索引将会从末尾开始选取行
print(arr[[-1, -2, -3]])
# 索引更低维度的数组或元素
arr = np.arange(32).reshape(8, 4)
print(arr[[0, 1, 2, 3], [0, 1, 2, 3]])
print(arr[[0, 1, 2, 3]][:, [0, 1, 2, 3]])