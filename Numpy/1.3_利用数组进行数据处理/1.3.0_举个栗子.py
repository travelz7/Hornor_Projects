import numpy as np
import matplotlib.pyplot as plt

# Numpy数组使你可以将许多种数据处理任务表述为简洁的数组表达式（否则需要编写循环）。
# 用数组表达式代替循环的做法，通常被称为矢量化

# 假设我们想要在一组值（网格型）上计算函数sqrt（x^2 + y^2）
# arange(start, stop, step, dtype = None)
points = np.arange(-5, 5, 0.01)
print(points)
xs, ys = np.meshgrid(points, points)
print(xs)
print(ys)
z = np.sqrt(xs ** 2 + ys ** 2)
print(z)

# 使用matplotlib将这个二维数组可视化
plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
plt.show()
