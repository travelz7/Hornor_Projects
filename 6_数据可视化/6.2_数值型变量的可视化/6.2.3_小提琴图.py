import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

tips = pd.read_csv(r'D:\Python\Projects\6_数据可视化\Data\第6章 Python数据可视化\tips.csv')
sns.violinplot(
    x='day',
    y='total_bill',
    hue='sex',
    data=tips,
    order={'Thur', 'Fri', 'Sat', 'Sun'},
    scale='count',
    split=True,
    palette='RdBu'
)
plt.title('每天不同性别客户的消费额情况')
plt.legend()
plt.show()





