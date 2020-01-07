import numpy as np

arr = np.arange(10)
arr[5:8] = 12
print(arr)
print("------------------------分割线---------------------")
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2)
print("对比：")
print(arr2[:2])

# 你可以一次传入多个切片，就像传入多个索引那样
print("你可以一次传入多个切片，就像传入多个索引那样:")
print(arr2[:2, 1:])
# 将整数索引与切片混合，可以得到低纬维度的切片
# 选取第二行的前两列
print(arr2[1, :2])
# 选择第三列的前两行
print(arr2[:2, 2])
# 选取整行、整列
print(arr2[:1, :])
print(arr2[:, :1])

