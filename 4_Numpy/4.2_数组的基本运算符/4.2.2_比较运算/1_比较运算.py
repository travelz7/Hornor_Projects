import numpy as np

arr7 = np.array([[1, 2, 10], [10, 8, 3], [7, 6, 5]])
arr8 = np.array([[2, 2, 2], [3, 3, 3], [4, 4, 4]])

# 取子集
# 从arr7中取出arr7大于arr8的所有元素
print('arr7:\n', arr7)
print('arr8:\n', arr8)
print('满足条件的二维数组元素获取：\n', arr7[arr7 > arr8])
# 从arr9中取出大于10的元素
arr9 = np.array([3, 10, 23, 7, 16, 9, 17, 22, 4, 8, 15])
print('满足条件的一维数组元素获取：\n', arr9[arr9 > 10])

# 判断操作
# 将arr7中大于7的元素改成5，其余的不变
print('二维数组的条件操作：\n', np.where(arr7 > 7, 5, arr7))
# 将arr9中大于10的元素改为1，否则为，0
print('一维数组的条件操作：\n', np.where(arr9 > 10, 1, 0))
# np.where函 数与Excel中的if函数一样，就是根据判定条件执行不同的分支语句
