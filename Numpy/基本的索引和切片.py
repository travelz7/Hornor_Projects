import numpy as np
import copy
# 一维数组很简单。从表面上看，它们跟Python列表的功能差不多
arr = np.arange(10)
print(arr)
# arr的第6个元素
print(arr[5])
# arr的第6-8个元素，[5:8]左闭右开
print(arr[5:8])
arr[5:8] = 12
print(arr)

# 给切片赋值时，会直接更改数组的值。因为切片是原始数组的视图，仕途上的任何修改都会直接反映到原数组上
arr_slice = arr[5:8]
print(arr_slice)

# 现在直接修改arr_slice的值，变动也会体现在原始数组中
arr_slice[1] = 12345
print(arr)

# 切片[:]会给数组中的所有值赋值
arr_slice[:] = 64
print(arr)

# 对于高维数组，能做的事情更多。在一个二维数组中，各索引位置上的元素不再是标量二是一维数组
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[2])
# 因此，可以对各个元素进行递归访问，但这样需要做的事情有点多
# 所以，还可以用一个逗号隔开的索引列表来选取单个元素，这两个方法是等价的
print(arr2d[0][0])
print(arr2d[0, 0])
# 在多维数组中，如果省略了后面的索引，则返回对象会是一个维度低一点的ndarray
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)
print(arr3d[0])
# 标量值和数组都可以被赋值给arr3d
# 将arr3d[0]的数据进行备份
old_values = arr3d[0].copy()
# 修改arr3d[0]的值为42
arr3d[0] = 42
print(arr3d)
print("-------------------------")
arr3d[0] = old_values
print(arr3d)
# 相似的，让我们进一步访问数组，返回一维数组
print(arr3d[1, 0])
# x = arr3d[1]
# # print(x)
# # print(x[0])

