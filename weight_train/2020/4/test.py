# 获取重复的数据
import pandas as pd

data = {'state': [1, 1, 2, 2, 1, 2, 2], 'pop': ['a', 'b', 'c', 'd', 'b', 'c', 'd']}
frame = pd.DataFrame(data)
print(frame)

a = frame.drop_duplicates(subset=['pop'], keep='first')  # 保留重复数据的第一个

b = frame.drop_duplicates(subset=['pop'], keep=False)  # 去掉重复的数据

c = a.append(b).drop_duplicates(subset=['pop'], keep=False)  # 合并两者，再去掉重复的数据

data_cf = frame.loc[frame['pop'].isin(c['pop'])]  ##获得了原数据的所有重复项

# data_cf = data_cf.sort_values('pop', ascending=True)  ##排序
print(data_cf)
print('duplicates:\n', frame.duplicated('state'))