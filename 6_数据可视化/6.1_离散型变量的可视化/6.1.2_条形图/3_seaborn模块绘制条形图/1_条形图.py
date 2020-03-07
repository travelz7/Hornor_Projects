import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.style.use('ggplot')

GDP = pd.read_excel(r'D:\Python\Projects\6_数据可视化\Data\第6章 Python数据可视化\Province GDP 2017.xlsx')
sns.barplot(y='Province',
            x='GDP',
            data=GDP,
            color='steelblue',
            orient='horizontal')
# 重新设置x轴和y轴的标签
plt.xlabel('GDP(万亿)')
plt.ylabel('')
# 添加图形的标题
plt.title('2017年度6个省份GDP分布')
# 为每个条形图添加数值标签
for y, x in enumerate(GDP.GDP):
    plt.text(x, y, '%s' % round(x, 1), va='center')
# 显示图形
plt.show()

Titanic = pd.read_csv(r'D:\Python\Projects\6_数据可视化\Data\第6章 Python数据可视化\titanic_train.csv')
# 绘制水平交错条形图
sns.barplot(x='Pclass', # 指定x轴数据
            y='Age', # 指定y轴数据
            hue='Sex', # 指定分组数据
            data=Titanic, # 指定绘图数据集
            palette='RdBu', # 指定男女性别的不同颜色
            errcolor='blue', # 指定误差棒的颜色
            errwidth=2, # 指定误差棒的线宽
            saturation=1, # 指定颜色的透明度，这里设置为无透明度
            capsize=0.05  # 指定误差棒两端线条的宽度
            )
# 添加图形标题
plt.title('各船舱等级中男女乘客的年龄差异')
# 显示图形
plt.show()