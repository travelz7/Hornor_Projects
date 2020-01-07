import numpy as np
from numpy.linalg import inv, qr

# 有些语言（如MATLAB），通过 * 对两个二维数组相乘得到的是一个元素级的积，而不是一个矩阵点积
# 因此，Numpy提供了一个用于矩阵乘法的dot函数，它既是一个数组方法，也是numpy命名空间中的一个函数
x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[6, 7], [8, 9], [1, 2]])
print(x)
print(y)
print(np.dot(x, y))
print(x.dot(y))

# 一个二维数组，跟一个大小合适的一维数组，矩阵点积运算后，将会得到一个一维数组
print("一个二维数组，跟一个大小合适的一维数组，矩阵点积运算后，将会得到一个一维数组:")
print(np.ones(3))
print(np.dot(x, np.ones(3)))

print(" @ 符号可以用作中缀运算符，进行矩阵乘法：")
print(x @ np.ones(3))

# numpy.linalg中有一组标准的矩阵分解运算以及诸如求逆和行列式之类的东西
# 他们跟MATLAB和R语言所使用的是相同的行业标准线性代数库，如BLAS、LAPACK、Intel MKL等
print("inv()矩阵求逆, qr()分接矩阵为q和r，q是正交矩阵，r是上三角矩阵")
# 另外，numpy.linalg()是求矩阵行列式
X = np.random.randn(5, 5)
mat = X.T.dot(X)
print(inv(mat))
print(mat.dot(inv(mat)))
q, r = qr(mat)
print(r)