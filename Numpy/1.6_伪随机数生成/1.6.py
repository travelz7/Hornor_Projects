from random import normalvariate
from timeit import timeit as timeit

import numpy as np

# numpy.random模块对Python内置的random进行了补充，增加了一些用于高效生成多种概率分布的样本值的函数
# 例如，你可以使用normal来得到一个标准正态分布的4*4样本数组
samples = np.random.normal(size=(4, 4))
print(samples)

# Python内置的random模块只能一次生成一个样本值
# 如果需要产生大量的样本值，numpy.random快了不止一个数量级
N = 1000000
samples = [normalvariate(0, 1) for _ in range(N)]
np.random.normal(size=N)

# 这些都是伪随机数，因为他们都是通过算法基于随机数生成器种子，在确定的条件下生成的
# 你可以用Numpy的np.random.seed()更改随机数种子
np.random.seed(123)
# numpy.random的数据生成函数使用了全局的随机种子
# 要避免全局状态，你可以使用numpy.random.RandomState，创建一个与其他隔离的随机数生成器
rng = np.random.RandomState(123)
print(rng.randn(10))
