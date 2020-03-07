import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# 解决汉字乱码问题
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# 解决负号问题
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_csv(
    r'D:\\Python\Projects\\5_Pandas\Data\\fd-export.csv'
)
data = data.loc[0:100, ['age', 'sex', 'country', 'trackable_value']]
# 去除重复值
data.drop_duplicates(inplace=True)
# 去除缺失值
data.dropna(inplace=True)
# 去除性别未知及其他
data = data[~data['sex'].isin(['doesnt_say', 'other'])]
# 重置索引
data.reset_index(drop=True, inplace=True)
# 国家出现频次统计
data['count'] = data['country'].apply(
    lambda x: dict(data['country'].value_counts())[x]
)
# 只保留第一个出现的不同国家的数据集
data_country_dif = data.drop_duplicates(subset='country', keep='first')
# 构建国家（标签）序列
country_dif = []
for i in data_country_dif['country']:
    country_dif.append(i)
# 构建频次序列
country_dif_counts = []
for i in data_country_dif['count']:
    country_dif_counts.append(i)
# 绘制饼图
plt.pie(x=country_dif_counts,  # 绘图数据
        labels=country_dif,  # 添加教育水平标签
        autopct='%.1f%%',  # 设置百分比的格式，这里保留一位小数
        pctdistance=0.8,  # 设置百分比标签与圆心的距离
        labeldistance=1.1,  # 设置教育水平标签与圆心的距离
        startangle=180,  # 设置饼图的初始角度
        radius=1.2,  # 设置饼图半径
        counterclock=False,  # 是否逆时针，这里设置为顺时针
        wedgeprops={'linewidth':1, 'edgecolor':'green'},  # 设置饼图内外边界的属性值
        textprops={'fontsize':10, 'color':'black'}  # 设置文本标签的属性值
        )
# 显示图标题
plt.title('不同国家的检查占比')
# 显示图形
plt.show()
# # 数值化要聚合的列
# data.age = pd.to_numeric(data.age[:-1], errors='coerce')
# data.trackable_value = pd.to_numeric(data.trackable_value[:-1], errors='coerce')
# # 按国家和性别分组
# data = data.groupby(by=['country', 'sex'])
# data = data.aggregate({
#     'age': np.mean,
#     'trackable_value': np.mean,
#     'count': np.mean
# })
# print(data)


