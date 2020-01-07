import numpy as np

# 在1.3.2叙述的方法中，例如sum、mean、cumsum、cumprod，布尔型会被强制转换为1（True）和0（False）
# 因此，sum经常被用来对布尔型数组中的True值计数
arr = np.random.randn(100)
print((arr > 0).sum())

# 另外还有两个方法，any和all，他们对布尔型数组非常有用
print("any用来测试数组中个是否存在一个或多个True:")
bools = np.array([False, False, True, False])
print(bools.any())
print("all用来测试数组中是否全是True：")
print(bools.all())
print("这两个方法也可以用于非布尔型数组，所有非0元素将会被当做True")