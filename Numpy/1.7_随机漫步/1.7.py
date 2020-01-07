#通过内置的random模块以纯Python的方式实现1000步的随机漫步
import random

import numpy as np
from matplotlib import pyplot as plt

position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position = position + step
    walk.append(position)
plt.plot(walk[:100])
plt.show()

# 我们用np.random模块一次性随机产生1000个“抛硬币”结果（即两个数中任选一个），将其分别设置为1或-1，然后计算累计和
nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
walk = np.cumsum(steps)

print(walk.min())
print(walk.max())
plt.plot(walk[:1000])
plt.show()

# 首次穿越时间，即随机漫步过程中第一次到达某个特定值的时间
# 假设我们想要知道本次随机漫步需要多久才能距离初始0点至少10步远（任意方向均可）
# 用 np.abs(walk)>=10 来判断是否达到或超过10，返回一个布尔型数组
# 用argmax来得到该布尔型数组最大值的索引（即True）
print((np.abs(walk > 10)).argmax())

# 模拟多个随机漫步过程
# 只需要给numpy.random的函数传入一个二元元组，就可以产生一个二维数组
# 然后我们就可以一次性计算5000个随机漫步过程（一行一个）了
nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps))
print("draws:")
print(draws)
steps = np.where(draws > 0, 1, -1)
print("steps:")
print(steps)
# 这里的comsum（1）是指axis=1，即求各行的累加值
walks = steps.cumsum(1)
print("walks:")
print(walks)
print(walks.min())
print(walks.max())

# 得到walks的数据后，我们来计算首次达到30或-30的时间，即最小穿越时间
# 因为不是5000个过程都达到了30或-30，所以用any方法来进行检查
hits = (np.abs(walks) >= 30).any(1)
print(hits)
print(hits.sum())
# 然后我们用这个布尔型数组，选出那些穿越了30（绝对值）的随机漫步（行），并调用argmax在轴1上获取时间
crossing_times = (np.abs(walks[hits]) >= 30).argmax(1)
print(crossing_times.mean())

# 也可以使用其他分布方式得到漫步数据，只需要使用不同的随机数生成函数即可
# 例如，normal用于生成指定均值和标准差的正态分布数据
steps = np.random.normal(loc=0, scale=0.25, size=(nwalks, nsteps))
walks = steps.cumsum(1)
hits = (np.abs(walks) >= 30).any(1)
crossing_times = (np.abs(walks[hits]) >= 30).argmax(1)
print(crossing_times.mean())
plt.plot(crossing_times[:100])
plt.show()