import numpy as np

# numpy.where函数是三元表达式 x if condition else y 的矢量化版本
# 假设我们有一个布尔数组和两个值数组
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
print(result)

# 这有几个问题：
# 1.他对大树组的处理速度不是很快，因为所有工作都是由纯python完成的
# 2.无法用于多维数组
# 如果使用np.where，则可以将该功能写的非常简洁
result = np.where(cond, xarr, yarr)
print(result)

# np.where的第二个和第三个参数不必是数组，他们都可以是标量值
# 在数据分析工作中，where通常用于根据另一个数组而产生一个新的数组
# 假设有一个由随机数组成的矩阵，你希望将所有正值替换为2，所有负值替换为-2
# 若利用np.where，则会非常简单
arr = np.random.randn(4, 4)
print(arr)
print(arr > 0)
print("将数组中所有正值替换为2，所有负值替换为-2：")
print(np.where(arr > 0, 2, -2))
# 使用np.where，可以将标量和数组结合起来
# 例如，我可用常数2替换arr中所有正的值
print("用常数2替换arr中所有正的值:")
print(np.where(arr > 0, 2, arr))
# 传递给where的数组大小可以不相等，甚至可以是标量值