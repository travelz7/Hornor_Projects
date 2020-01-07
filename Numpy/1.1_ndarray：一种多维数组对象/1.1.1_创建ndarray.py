import numpy as np

# 创建数组最简单的办法就是使用array函数
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
print(arr1)
# 嵌套序列（比如由一组等长列表组成的列表）将会被转换为一个多维数组
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print(arr2)
# NumPy数组arr2的两个维度的shape是从data2引入的
print(arr2.ndim)
print(arr2.shape)
# np.array会尝试为新建的这个数组推断出一个较为合适的数据类型,数据类型保存在一个特殊的dtype对象中
print(arr1.dtype)
print(arr2.dtype)
# 除np.array之外，还有一些函数也可以新建数组
# zeros和ones分别可以创建指定长度或形状的全0或全1数组。empty可以创建一个没有任何具体值的数组。要用这些方法创建多维数组，只需传入一个表示形状的元组即可
print(np.zeros(10))
print(np.zeros((3, 6)))
print(np.empty((2, 3, 2)))
# arange是Python内置函数range的数组版
print(np.arange(15))






