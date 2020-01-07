import numpy as np
# 通用函数（即ufunc）是一种对ndarray中的数据执行元素级运算的函数
# sqrt和exp
# sqrt是开根号
# exp是以e为底，参数为幂
print("sqrt和exp------------>")
arr = np.arange(10)
print(arr)
print(np.sqrt(arr))
print(np.exp(arr))
# 以上都是一元（unary）ufunc
# 另外一些（如add或maximum）接受2个数组（因此也叫二元（binary）ufunc），并返回一个结果数组
# 这里的maximum计算了x和y中元素级别最大的元素
print("二元通用函数------------->")
x = np.random.randn(8)
y = np.random.randn(8)
print(x)
print(y)
print(np.maximum(x, y))
# 返回多个数组的ufunc并不常见，但也有一些，例如modf，它是Python内置函数divmod的矢量化版本，他会返回浮点数数组的小数和整数部分
print("modf,返回两个数组，分别是浮点数数组的小数和整数部分-------------------------->")
arr = np.random.randn(7)*5
print(arr)
remainder, whole_part = np.modf(arr)
print(remainder)
print(whole_part)
# ufuncs可以接受一个out可选参数，这样就能在数组原地进行操作
print("ufuncs可以接受一个out可选参数，这样就能在数组原地进行操作------------------------->")
print(arr)
print(np.sqrt(arr))
print(np.sqrt(arr, arr))
print(arr)