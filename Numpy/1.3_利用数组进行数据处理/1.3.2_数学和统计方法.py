import numpy as np

# 可以通过数组上的一组数学函数对整个数组或某个轴向的数据进行统计计算
# sum、mean以及标准差std等局和计算（aggregation，通常叫做约简（reduction）既可以当做数组的实例方法调用，
#                                                                    也可以当做顶级Numpy函数使用）
arr = np.random.randn(5, 4)
print(arr)
print(arr.mean())
print(np.mean(arr))
print(arr.sum())

# mean和sum这类的函数可以接受一个axis选项函数，用于计算改轴向上的统计值，最终结果是一个少一维的数组
# axis  轴
print(arr.mean(axis=1))
print(np.mean(arr, axis=0))
# axis = 1是计算行，axis = 0是计算列

# 其他如cumsum和sumprod之类的方法则不聚合，而是产生一个由中间结果组成的数组
# cumsum是加，cumprod是乘
print("cumsum和cumprod的用法--------------------------->")
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
print(arr.cumsum())
print(arr.cumprod())
# 在多维数组中，累加函数（如cumsum）返回的是同样大小的数组，但是会根据每个低维的切片沿着标记轴计算部分聚类
arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(arr)
print(arr.cumsum(axis=0))
print(arr.cumprod(axis=1))