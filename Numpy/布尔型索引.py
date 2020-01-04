import numpy as np

names = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
data = np.random.randn(7, 4)
print(names)
print(data)

# 对names和字符串“a”的比较运算会产生一个布尔型数组
print(names == 'a')
# 这个布尔型数组可用于数组索引：
print(data[names == 'a'])
# 获取names == 'a'的行，并索引列
print(data[names == 'a', 2:])
print(data[names == 'a', 3])
# 要选择‘a’之外的值，可以用（！=），也可以用（~）对条件进行否定
print(names != 'a')
print(data[~(names == 'a')])
# 操作符~用来反转条件很好用
cond = names == 'a'
print(data[~cond])
# 选取多个名字需要组合应用多个布尔条件，使用&（和）、|（或）之类的布尔算术运算符即可
mask = (names == 'a') | (names == 'b')
print(mask)
print(data[mask])
# 通过布尔型数组设置值是一种经常用到的手段
# 将data中的所有负值都设置为0
data[data < 0] = 0
print(data)
# 通过一维布尔数组设置整行或整列的值也很简单
data[names != 'a'] = 7
print(data)
