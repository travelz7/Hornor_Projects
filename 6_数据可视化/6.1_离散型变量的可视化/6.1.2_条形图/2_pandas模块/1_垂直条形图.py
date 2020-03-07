import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.style.use('ggplot')

# Pandas模块之垂直条形图
# 绘图
GDP = pd.read_excel(r'D:\Python\Projects\6_数据可视化\Data\第6章 Python数据可视化\Province GDP 2017.xlsx')
GDP.GDP.plot(kind='bar',
             width=0.8,
             rot=0,
             color='steelblue',
             title='2017年度6个省份GDP分布')
# 添加y轴标签
plt.ylabel('GDP(万亿)')
# 添加x轴刻度标签
plt.xticks(range(len(GDP.Province)), #指定刻度标签的位置
           GDP.Province #指出具体的刻度标签值
           )
# 为每个条形图添加数值标签
for x, y in enumerate(GDP.GDP):
    plt.text(x-0.1, y+0.2, '%s' % round(y, 1), va='center')
plt.show()

# pandas模块之水平交错条形图
diamonds = pd.read_table(r'D:\Python\Projects\6_数据可视化\Data\第6章 Python数据可视化\diamonds.csv', sep=',')
diamonds_reshape = pd.pivot_table(data=diamonds, index='clarity', columns='cut', values='carat').reset_index()
# 对数据集降序排序
diamonds_reshape.sort_values(by='clarity', ascending=False, inplace=True)
diamonds_reshape.plot(x='clarity', y=['Good', 'Very Good'],
                 kind='bar', color=['steelblue', 'indianred'],
                 rot=0,  #用于旋转x轴刻度标签的角度，0表示水平显示刻度标签
                 width=0.8, title='好、很好宝石重量比较')
# 添加y轴标签
plt.ylabel('克拉')
# plt.xlabel('')
plt.show()
