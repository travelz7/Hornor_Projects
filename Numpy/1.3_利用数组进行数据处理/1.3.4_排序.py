import numpy as np

# numpy.sort函数返回输入数组的排序副本
# 它有以下参数：numpy.sort（a, axis, kind, order）
# a：要排序的数组
# aixs：沿着他排序数组的轴，如果没有数组会被展开，沿着最后的轴排序
# kind：默认为‘quicksort’（快速排序）
# order：如果数组包含字段，则是要排序的字段
a = np.array([[3, 7], [9, 1]])
print('我们的数组是：')
print(a)
print('\n')
print('调用sort（）函数')
print(np.sort(a))
print('\n')
print('沿轴0排序：')
print(np.sort(a, axis=0))
print('\n')
# 在sort中排序字段
dt = np.dtype([('name', 'S10'), ('age', int)])
a = np.array([("zs", 21), ("grf", 22), ("xj", 23)], dtype=dt)
print('我们的数组是：')
print(a)
print('\n')
print('按name排序：')
print(np.sort(a, order='name'))

# Numpy。argsort（）函数对输入数组沿给定轴执行间接排序，并使用指定排序类型返回数据的索引数组
# 这个索引数组用于构造排序后的数组
print("Numpy.argsort()的使用,argsort()返回排序后的索引：")
arr = np.random.randn(5, 3)
print(arr)
arr.sort(1)
print(arr)

x = np.array([3, 1, 2])
print('我们的数组是：')
print(x)
print('\n')
print('对x调用argsort（）函数：')
y = np.argsort(x)
print(y)
print('\n')
print('以排序后的顺序重构原数组：')
print(x[y])
print('\n')
print('使用循环重构数组：')
for i in y:
    print(x[i])

# numpy.lexsort()
print("函数使用键序列执行间接排序，该函数返回一个索引数据，使用他可以获得排序数据，最后一个键恰好是sort的主键")
nm = ('c', 'a', 'd', 'b')
dv = ('1', '2', '3', '4')
ind = np.lexsort((dv, nm))
print('调用lexsort函数：')
print(ind)
print('\n')
print('使用这个索引来获取排序后的数据：')
print([nm[i] + "," +dv[i] for i in ind])
