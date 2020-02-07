import numpy as np

# 范数的计算
arr17 = np.array([1, 3, 5, 7, 9, 10, -12])
# 一范数
res1 = np.linalg.norm(arr17, ord=1)
print('向量的一范数：\n', res1)
# 二范数
res2 = np.linalg.norm(arr17, ord=2)
print('向量的二范数：\n', res2)
res22 = np.dot(arr17, arr17)**0.5
print('验证：\n', res22)
# 无穷范数
res3 = np.linalg.norm(arr17, ord=np.inf)
print('向量的无穷范数：\n', res3)

# 范数常常用来度量某个向量空间（或矩阵）中的每个向量的长度或 大小，
# 它具有三方面的约束条件，分别是非负性、齐次性和三角不等 性。
# 最常用的范数就是p范数，其公式可以表示成ǁxǁp=(|x1|p+|x2|p+… +|xn|p)1/p。
