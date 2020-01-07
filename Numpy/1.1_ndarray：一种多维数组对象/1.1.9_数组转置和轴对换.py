import numpy as np

#转置会返回原数组视图，不会进行复制
# 转置不仅有transpose方法，还与一个特殊的属性T
print("矩阵的转置------->")
arr = np.arange(15).reshape((3, 5))
print(arr)
print(arr.T)
print(arr.transpose())
print("矩阵的内积------->")
arr = np.random.randn(6, 3)
print(np.dot(arr.T, arr))
print("高维数组的转置--------->")
# 高维数组的转置，transpose需要得到一个由轴编号组成的元组才能对这些轴进行转置
arr = np.arange(16).reshape(2, 2, 4)
print(arr)
print(arr.transpose((1, 0, 2)))
# ndarray还有一个swapaxes方法，他需要接受一对轴编号
print(arr.swapaxes(1, 2))