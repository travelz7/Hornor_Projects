import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# 生成各种指数分布随机数
re1 = np.random.exponential(scale=0.5, size=1000)
re2 = np.random.exponential(scale=1, size=1000)
re3 = np.random.exponential(scale=1.5, size=1000)
# 绘图
sns.distplot(re1, hist=False, kde=False, fit=stats.expon,
             fit_kws={'color': 'black', 'label': 'lamda=0.5', 'linestyle': '-'})
sns.distplot(re2, hist=False, kde=False, fit=stats.expon,
             fit_kws={'color': 'red', 'label': 'lamda=1', 'linestyle': '--'})
sns.distplot(re3, hist=False, kde=False, fit=stats.expon,
             fit_kws={'color': 'blue', 'label': 'lamda=1.5', 'linestyle': ':'})
# 呈现图例
plt.legend()
# 呈现图形
plt.show()
