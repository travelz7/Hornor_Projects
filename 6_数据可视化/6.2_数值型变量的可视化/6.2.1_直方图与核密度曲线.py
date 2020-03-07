import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
import seaborn as sns

# 1.Matplotlib模块
# Matplotlib模块中的hist函数就是用来绘制直方图的
# plt.hist(x, 绘图数据
#          bins=10, 直方图条形个数
#          range=None, 指定直方图数据的上下界，默认包含绘图数据的最大值和最小值
#          normed=False, 是否将直方图的频数转换成频率
#          weights=None, 该参数可为每一个数据点设置权重
#          cumulative=False, 是否需要计算累计频数或频率
#          bottom=None, 可以为直方图的每个条形添加基准线，默认为0
#          histtype='bar', 指定直方图的类型，默认为bar，还有barstacked，step，stepfilled
#          align='mid', 设置条形边界值的对齐方式，默认为mid，还有left，right
#          orientation='vertical', 直方图的摆放方向，默认为垂直方向
#          rwidth=None, 设置直方图条形的宽度
#          log=False, 是否需要对绘图数据进行log变换
#          color=None, 设置直方图的填充色
#          edgecolor, 设置直方图边框色
#          label=None, 设置直方图的标签，可通过legend展示其图例
#          stacked=False 当有多个数据时，是否需要将直方图呈堆叠摆放，默认水平摆放
#          )
mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('ggplot')
Titanic = pd.read_table(r'D:\Python\Projects\6_数据可视化\Data\第6章 Python数据可视化\titanic_train.csv', sep=',')
print('检查年龄是否有缺失：', any(Titanic.Age.isnull()))
# 删除含有缺失年龄的观察
Titanic.dropna(subset=['Age'], inplace=True)
# 绘制直方图
plt.hist(x=Titanic.Age,  # 绘图数据
         bins=20,  # 指定直方图中条块的个数
         color='steelblue',  # 指定直方图的填充色
         edgecolor='black'  # 指定直方图的边框色
         )
# 添加x轴、y轴标签
plt.xlabel('年龄')
plt.ylabel('频数')
# 添加标题
plt.title('乘客年龄分布')
# 显示图形
plt.show()

# 2.Pandas模块
# 绘制直方图
Titanic.Age.plot(kind='hist',
                 bins=20,
                 color='steelblue',
                 edgecolor='black',
                 density=True,
                 label='直方图')
# 绘制核密度图
Titanic.Age.plot(kind='kde', color='red', label='核密度图')
# 添加x轴、y轴标签
plt.xlabel('年龄')
plt.ylabel('核密度值')
# 添加标题
plt.title('乘客年龄分布')
# 显示图例
plt.legend()
# 显示图形
plt.show()

# 3.Seaborn模块
# sns.distplot(a,     指定绘图数据，可以是序列、一维数组、列表
#              bins=None,     指定直方图条形的个数
#              hist=True,     bool类型的参数，是否绘制直方图，默认为True
#              kde=True,      bool，是否绘制核密度图，默认为True
#              rug=False,     bool，是否绘制须图，默认为False，数据密集时，该参数比较有用
#              fit=None,      指定一个随机分布对象（需要调用scipy模块中的随机分布函数），
#                             用于绘制随机分布的概率密度曲线
#              hist_kws=None,        以字典形式传递直方图的其他修饰属性，
#                                     如填充色、边框色、宽度等
#              kde_kws=None,      以字典形式传递核密度图的其他属性，
#                                 如线的颜色、线的类型等
#              rug_kws=None,      以字典形式传递须图的其他修饰属性，
#                                 如线的颜色、线的宽度等
#              fit_kws==None,     以字典形式传递概率密度曲线的其他修饰属性，
#                                 如线条颜色、形状、宽度等
#              color=None,        图形颜色，除了随机分布曲线的颜色
#              vertical=False,    bool，是否将图形垂直显示，默认为True
#              norm_hist=False,   bool，是否将频数更改为频率，默认为False
#              axlabel=None,      用于显示轴标签
#              label=None,        指定图形的图例，需要结合plt.legend()一起使用
#              ax=None        指定子图的位置
#              )

# 取出男性年龄
Age_Male = Titanic.Age[Titanic.Sex == 'male']
# 取出女性年龄
Age_Female = Titanic.Age[Titanic.Sex == 'female']

# 绘制男女乘客年龄的直方图
sns.distplot(Age_Male, bins=20, kde=False,
             hist_kws={'color': 'steelblue'}, label='男性')
# 绘制女性年龄的直方图
sns.distplot(Age_Female, bins=20, kde=False,
             hist_kws={'color': 'purple'}, label='女性')
plt.title('男女乘客的年龄直方图')
plt.legend()
plt.show()

# 绘制男女乘客年龄的核密度图
sns.distplot(Age_Male,
             hist=False,
             kde_kws={'color': 'red', 'linestyle': '-'},
             norm_hist=True,
             label='男性')
sns.distplot(Age_Female,
             hist=False,
             kde_kws={'color': 'black', 'linestyle': '--'},
             norm_hist=True,
             label='女性')
plt.title('男女乘客的年龄核密度图')
# 显示图例
plt.legend()
# 显示图形
plt.show()
















