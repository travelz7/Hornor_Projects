import numpy as np

# 各输入数组维度一致，对应维度值相等
arr10 = np.arange(12).reshape(3, 4)
arr11 = np.arange(101, 113).reshape(3, 4)
print('3*4的二维矩阵运算：\n', arr10 + arr11)
# 各输入数组维度不一致，对应维度值相等
arr12 = np.arange(60).reshape(5, 4, 3)
arr10 = np.arange(12).reshape(4, 3)
print('维度不一致，但末尾的维度值一致：\n', arr12 + arr10)
# 各输入数组维度不一致，对应维度值不相等，但其中有一个为1
arr12 = np.arange(60).reshape(5, 4, 3)
arr13 = np.arange(4).reshape(4, 1)
print('维度不一致，维度值也不一致，但维度值至少一个为1：\n', arr12 + arr13)
# 加1补齐
arr14 = np.array([5, 15, 25])
print('arr14的维度自动补齐为(1,3):\n', arr10 + arr14)

