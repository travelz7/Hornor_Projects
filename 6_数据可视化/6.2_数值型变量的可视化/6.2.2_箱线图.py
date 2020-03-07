import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pylab import mpl
import numpy as np
import seaborn as sns

# 1.Matplotlib模块
# box.plot函数
# plt.boxplot(
#     x,  绘制箱线图的数据
#     notch=None,     是否以凹口的形式展现箱线图，默认非凹口
#     sym=None,       指定异常点的形状，默认为+号显示
#     vert=None,      是否需要将箱线图垂直摆放，默认为垂直摆放
#     whis=None,      指定上下须与上下四分位的距离，默认为1.5倍的四分位差
#     positions=None,     指定箱线图的位置，默认为[0,1,2...]
#     widths=None,    指定箱线图的宽度，默认为0.5
#     patch_artist=None,  bool，是否填充箱体的颜色；默认为False
#     meanline=None,  bool，是否用线的形式表示均值，默认为False
#     showmeans=None,     bool，是否显示均值，默认为False
#     showcaps=None,  bool，是否显示箱线图顶端和末端的两条线（即上下须），默认为True
#     showbox=None,   bool，是否显示箱线图的箱体，默认为True
#     showfliers=None,    是否显示异常值，默认为True
#     boxpros=None,   设置箱体的属性，如边框色，填充色等
#     labels=None,    为箱线图添加标签，类似于图例的作用
#     flierprops=None,    设置异常值的属性，如异常点的形状、大小、填充色等
#     medianprops=None,   设置中位数的属性，如线的类型、粗细等
#     meanprops=None, 设置均值的属性，如点的大小、颜色等
#     capprops=None,  设置箱线图顶端和末端线条的属性，如颜色、粗细等
#     whiskerprops=None   设置须的属性，如颜色、粗细、线的类型等
# )

mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 绘制箱线图
Sec_Buildings = pd.read_excel(r'D:\Python\Projects\6_数据可视化\Data\第6章 Python数据可视化\sec_buildings.xlsx')
plt.boxplot(x=Sec_Buildings.price_unit,
            patch_artist=True,
            showmeans=True,
            boxprops={'color': 'black', 'facecolor': 'steelblue'},
            flierprops={'marker': 'o', 'markerfacecolor': 'red',
                        'markersize': 3},
            meanprops={'marker': 'D', 'markerfacecolor': 'indianred',
                       'markersize': 4},
            medianprops={'linestyle': '--', 'color': 'orange'},
            labels=['']  # 删除x轴的刻度标签，否则显示刻度标签为1
            )
plt.title('二手房单价分布的箱线图')
plt.show()

# 二手房在各行政区域的平均单价
group_region = Sec_Buildings.groupby('region')
avg_price = group_region.aggregate({'price_unit': np.mean}).sort_values(
    'price_unit', ascending=False)
# 通过循环，将不同行政区域的二手房存储到列表中
region_price = []
for region in avg_price.index:
    region_price.append(Sec_Buildings.price_unit[Sec_Buildings.region == region])
# 绘制分组箱线图
plt.boxplot(x=region_price,
            patch_artist=True,
            labels=avg_price.index,  # 添加x轴的刻度标签
            showmeans=True,
            boxprops={'color': 'black', 'facecolor': 'steelblue'},
            flierprops={'marker': 'o', 'markerfacecolor': 'red',
                        'markersize': 3},
            meanprops={'marker': 'D', 'markerfacecolor': 'indianred',
                       'markersize': 4},
            medianprops={'linestyle': '--', 'color': 'orange'})
plt.ylabel('单价（元）')
plt.title('不同行政区域的二手房价对比')
plt.show()

# 2.Seaborn模块
# sns.boxplot(x=None,             指定箱线图的x轴数据
#             y=None,             指定箱线图的y轴数据
#             hue=None,           指定分组变量
#             data=None,          指定用于绘图的数据集
#             order=None,         传递一个字符串列表，用于分类变量的排序
#             hue_order=None,     传递一个字符串列表，用于分类变量hue值的排序
#             orient=None,        指定箱线图的呈现方向，默认为垂直方向
#             color=None,         指定所有箱线图的填充色
#             palette=None,       指定hue变量的区分色
#             saturation=0,       指定颜色的透明度
#             width=None,         指定箱线图的宽度
#             dodge=True,         bool，使用hue参数时，是否绘制水平交错的箱线图，默认为True
#             fliersize=5,        指定异常值点的大小
#             linewidth=None,     指定箱体边框的宽度
#             whis=1.5,           指定上下须与上下四分位的距离，默认为1.5倍的四分位差
#             notch=False,        bool，是否绘制凹口箱线图，默认为False
#             ax=None             指定子图的位置
#             **kwargs=None       关键字参数，可以调用plt.boxplot函数中的其他参数
#             )

# 绘制分组箱线图
sns.boxplot(x='region',
            y='price_unit',
            data=Sec_Buildings,
            order=avg_price.index,
            showmeans=True,
            color='steelblue',
            flierprops={'marker': 'o', 'markerfacecolor': 'red',
                        'markersize': 3},
            meanprops={'marker': 'D', 'markerfacecolor': 'indianred',
                       'markersize': 4},
            medianprops={'linestyle': '--', 'color': 'orange'})
# 更改x轴和y轴标签
plt.xlabel('')
plt.ylabel('单价（元）')
plt.title('不同行政区域的二手房单价对比')
plt.show()




