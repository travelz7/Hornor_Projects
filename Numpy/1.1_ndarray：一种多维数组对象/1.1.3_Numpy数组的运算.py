import numpy as np

# NumPy数组的运算
arr = np.array([[1., 2., 3.],[4., 5., 6.]])
print(arr)
print(arr * arr)
print(arr - arr)
# 数组与标量的算术运算会将标量值传播到各个元素
print(1 / arr)
print(arr ** 0.5)
# 大小相同的数组之间的比较会生成布尔值数组
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
print(arr2)
print(arr2 > arr)