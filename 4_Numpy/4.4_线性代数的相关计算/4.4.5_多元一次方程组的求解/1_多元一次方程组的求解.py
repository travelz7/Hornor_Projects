import numpy as np

# 多元线性方程组
A = np.array([[3, 2, 1], [2, 3, 1], [1, 2, 3]])
b = np.array([39, 34, 26])
X = np.linalg.solve(A, b)
print('三元一次方程的解：\n', X)

#   3x + 2y + z = 39
#   2x + 3y + z = 34
#   x + 2y + 3z = 26
# 在线性代数中，这个方程组就可以表示成AX=b,
# A代表等号左边数 字构成的矩阵，X代表三个未知数，b代表等号右边数字构成的向量。
# 如 需求解未知数X，可以直接使用linalg子模块中的solve函数
