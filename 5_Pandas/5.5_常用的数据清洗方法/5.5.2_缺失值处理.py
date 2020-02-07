import pandas as pd

df = pd.read_excel(r'D:\Python\Projects\5_Pandas\Data\第5章 Python数据处理工具--Pandas\data_test05.xlsx')
print('数据集中是否存在缺失值：\n', any(df.isnull()))

# 删除法————记录删除
df.dropna()
print('记录删除：\n', df.dropna())
# 删除法————变量删除
df.drop('age', axis=1)
print('变量删除：\n', df.drop('age', axis=1))
# 替换法————向前替换
df.fillna(method='ffill')
print('向前替换:\n', df.fillna(method='ffill'))
# 替换法————向后替换
df.fillna(method='bfill')
print('向后替换：\n', df.fillna(method='bfill'))
# 替换法————常数替换
df.fillna(value=0)
print('常数替换：\n', df.fillna(value=0))
df.fillna(value={'gender': df.gender.mode()[0],
                 'age': df.age.mean(),
                 'income': df.income.median()})
print('统计值替换：\n', df.fillna(value={'gender': df.gender.mode()[0],
                 'age': df.age.mean(),
                 'income': df.income.median()}))






