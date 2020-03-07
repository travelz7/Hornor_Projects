import pandas as pd
import numpy as np

# pandas提供了实现透视表功能的pivot_table函数
# pd.pivot_table(data, values=None, index=None, columns=None,
#                aggfunc='mean', fill_value=None, margins=False,
#                dropna=True, margins_name='All')
# data：指定需要构造透视表的数据集
# values：指定需要拉入“数值”框的字段列表
# index：指定需要拉入“行标签”框的字段列表
# columns：指定需要拉入“列标签”框的字段列表
# aggfunc：指定数值的统计函数，默认为统计均值，也可以指定numpy模块中的其他统计函数
# fill_value：指定一个标量，用于填充缺失值
# margins：bool类型参数，是否需要显示行或列的总计值，默认为False
# dropna：bool类型参数，是否需要删除整列为缺失的字段，默认为True
# margins_name：指定行或列的总计名称，默认为All

# 数据读取
diamonds = pd.read_table(r'D:\Python\Projects\5_Pandas\Data\第5章 Python数据处理工具--Pandas\diamonds.csv', sep=',')
# 单个分组变量的均值统计
x1 = pd.pivot_table(data=diamonds, index='color', values='price', margins=True,
                    margins_name='平均值')
print('单个分组变量的均值统计：\n', x1)
x2 = pd.pivot_table(data=diamonds, index='clarity', columns='cut', values='carat',
                    aggfunc=np.size, margins=True, margins_name='总计')
print('两个分组变量的列联表：\n', x2)
# 对于列联表来说，统计的不再是某个变量的均值，而是观测个数



