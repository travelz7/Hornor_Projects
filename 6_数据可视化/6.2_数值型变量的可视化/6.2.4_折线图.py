import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pylab import mpl
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

wechat = pd.read_excel(r'D:\Python\Projects\6_数据可视化\Data\第6章 Python数据可视化\wechat.xlsx')
plt.plot(
    wechat.Date,
    wechat.Counts,
    linestyle='-',
    linewidth=2,
    color='steelblue',
    marker='o',
    markersize=6,
    markeredgecolor='black',
    markerfacecolor='brown'
)
plt.ylabel('人数')
plt.title('每天微信文章阅读人数趋势')
plt.show()

plt.plot(
    wechat.Date,
    wechat.Counts,
    linestyle='-',
    color='steelblue',
    label='阅读人数'
)
plt.plot(
    wechat.Date,
    wechat.Times,
    linestyle='--',
    color='indianred',
    label='阅读人次'
)
# 获取图标的坐标信息
ax = plt.gca()
# 设置日期的显示格式
date_format = mpl.dates.DateFormatter('%m-%d')
ax.xaxis.set_major_formatter(date_format)
# 设置x轴显示多少个日期刻度
# xlocator = mpl.ticker.LinearLocator(10)
# 设置x轴每个刻度的间隔天数
xlocator = mpl.ticker.MultipleLocator(7)
ax.xaxis.set_major_locator(xlocator)
# 为了避免x轴刻度标签的紧凑，将刻度标签旋转45度
plt.xticks(rotation=45)

plt.ylabel('人数')
plt.title('每天微信文章阅读人数与人次趋势')
plt.legend()
plt.show()


