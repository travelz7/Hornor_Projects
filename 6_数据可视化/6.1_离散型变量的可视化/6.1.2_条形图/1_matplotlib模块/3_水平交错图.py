import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.style.use('ggplot')

Industry_GDP = pd.read_excel(r'D:\Python\Projects\6_数据可视化\Data\第6章 Python数据可视化\Industry_GDP.xlsx')
# 取出四季标签
Quarters = Industry_GDP.Quarter.unique()
# 取出第一、第二产业各季度GDP值
Industry1 = Industry_GDP.GDP[Industry_GDP.Industry_Type == '第一产业']
Industry2 = Industry_GDP.GDP[Industry_GDP.Industry_Type == '第二产业']

# 绘制水平交错条形图
bar_width = 0.4
plt.bar(x=np.arange(len(Quarters)),
        height=Industry1,
        label='第一产业',
        color='steelblue',
        width=bar_width)
plt.bar(x=np.arange(len(Quarters))+bar_width,
        height=Industry2,
        label='第二产业',
        color='indianred',
        width=bar_width)
# 添加刻度标签
plt.xticks(np.arange(4)+0.2, Quarters)
# 添加图例
plt.legend()
# 显示图形
plt.show()

