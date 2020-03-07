import pandas as pd
import matplotlib.pyplot as plt

# 数据读入
sunsports = pd.read_table(r'D:\Python\Projects\5_Pandas\Data\第5章 Python数据处理工具--Pandas\sunspots.csv', sep=',')
# 异常值检测————标准差法
xbar = sunsports.counts.mean()
xstd = sunsports.counts.std()
print('标准差法异常值上限检测：\n', any(sunsports.counts > xbar + 2 * xstd))
print('标准差法异常值下限检测：\n', any(sunsports.counts < xbar - 2 * xstd))

# 异常值检测————箱线图法
Q1 = sunsports.counts.quantile(q=0.25)
Q3 = sunsports.counts.quantile(q=0.75)
IQR = Q3 - Q1
print('箱线图法异常值上限检测：\n', any(sunsports.counts > Q3 + 1.5 * IQR))
print('箱线图法异常值下限检测：\n', any(sunsports.counts < Q1 - 1.5 * IQR))

# 设置绘图风格
plt.style.use('ggplot')
# 绘制直方图
sunsports.counts.plot(kind='hist', bins=30, density=True)
# 绘制核密度图
sunsports.counts.plot(kind='kde')
plt.show()

# 替换法处理异常值
print('异常值替换前的数据统计特征：\n', sunsports.counts.describe())
# 箱线图中的异常值判别上限
UL = Q3 + 1.5 * IQR
print('判别异常值的上限临界值：\n', UL)
# 从数据中找出低于判别上限的最大值
replace_value = sunsports.loc[sunsports.counts < UL, 'counts'].max()
print('用以替换异常值的数据：\n', replace_value)

# 替换超过判别上限异常值
sunsports.loc[sunsports.counts > UL, 'counts'] = replace_value
print('异常值替换后的数据统计特征：\n', sunsports.counts.describe())

