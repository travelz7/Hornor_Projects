import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.style.use('ggplot')

Industry_GDP = pd.read_excel(r'D:\Python\Projects\6_数据可视化\Data\第6章 Python数据可视化\Industry_GDP.xlsx')
# 取出四个不同的季度标签，用作堆叠条形图x轴的刻度标签
Quarters = Industry_GDP.Quarter.unique()
# 取出第一产业的四季度值
Industry1 = Industry_GDP.GDP[Industry_GDP.Industry_Type == '第一产业']
# 重新设置行索引
Industry1.index = range(len(Quarters))
# 取出第二产业的四季度值
Industry2 = Industry_GDP.GDP[Industry_GDP.Industry_Type == '第二产业']
# 重新设置行索引
Industry2.index = range(len(Quarters))
# 取出第三产业的四季度值
Industry3 = Industry_GDP.GDP[Industry_GDP.Industry_Type == '第三产业']
# 重新设置行索引
Industry3.index = range(len(Quarters))
# 如果不重新设置行索引，那么因为每一种产业值前的行索引不同，
# 会导致无法进行Industry1+Indus2的计算

# 绘制堆叠条形图
# 各季度下第一产业的条形图
plt.bar(x=range(len(Quarters)), height=Industry1, color='steelblue',
        label='第一产业', tick_label=Quarters)
# 各季度下第二产业的条形图
plt.bar(x=range(len(Quarters)), height=Industry2, bottom=Industry1,
        color='green', label='第二产业')
# 各季度下第三产业的条形图
plt.bar(x=range(len(Quarters)), height=Industry3, bottom=Industry1 + Industry2,
        color='red', label='第三产业')
# 添加y轴标签
plt.ylabel('生成总值（亿）')
# 添加图形标题
plt.title('2017年各季度三产业总值')
# 显示各产业的图例
plt.legend()
# 显示图形
plt.show()


