import numpy as np

# dtype（数据类型）是一个特殊的对象，它含有ndarray将一块内存解释为特定数据类型所需的信息
arr1 = np.array([1, 2, 3], dtype = np.float64)
arr2 = np.array([1, 2, 3], dtype = np.int32)
print(arr1.dtype)
print(arr2.dtype)
# 你可以通过ndarray的astype方法明确地将一个数组从一个dtype转换成另一个dtype
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)
float_arr = arr.astype(np.float64)
print(float_arr.dtype)
# 如果将浮点数转换成整数，则小数部分将会被截取删除
arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
print(arr)
print(arr.astype(np.int32))
# 如果某字符串数组表示的全是数字，也可以用astype将其转换为数值形式
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
print(numeric_strings.astype(float))
