import pandas as pd
import numpy as np

# 构造序列
gdp1 = pd.Series([2.8, 3.01, 8.99, 8.59, 5.18])
gdp2 = pd.Series({'北京': 2.8, '上海': 3.01, '广东': 8.99,
                  '江苏': 8.59, '浙江': 5.18})
gdp3 = pd.Series(np.array((2.8, 3.01, 8.99, 8.59, 5.18)))
print(gdp1)
print(gdp2)
print(gdp3)
# 取出gdp1中的第一、第四和第五个元素
print('行号风格的序列：\n',gdp1[[0, 3, 4]])
# 取出gdp2中的第二、第四和第五个元素
print('行名称风格的序列：\n', gdp2[[1, 3, 4]])
# 取出gdp2中上海、江苏和浙江的GDP值
print('行名称风格的序列：\n', gdp2[['上海', '江苏', '浙江']])
# 数学函数--取对数
print('通过numpy函数：\n', np.log(gdp1))
# 平均gdp
print('通过numpy函数：\n', np.mean(gdp1))
print('通过序列的方法：\n', gdp1.mean())
