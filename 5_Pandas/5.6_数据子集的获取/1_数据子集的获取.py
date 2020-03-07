import pandas as pd

# 构造数据集
df1 = pd.DataFrame({'name': ['张三', '李四', '王二', '丁一', '李五'],
                    'gender': ['男', '女', '女', '女', '男'],
                    'age': [23, 26, 22, 25, 27]},
                   columns=['name', 'gender', 'age'])
# 取出数据集的中间三行（即所有女性），并且返回姓名和年龄两列
print('iloc:\n', df1.iloc[1:4, [0, 2]])
print('loc:\n', df1.loc[1:3, ['name', 'age']])
# 从pandas0.20.0之后，ix函数已经被弃用
# df1.ix[1:3, [0, 2]]

# 将员工的姓名用作行标签
df2 = df1.set_index('name')
# 取出数据集的中间三行
print('iloc:\n', df2.iloc[1:4, :])
print('loc:\n', df2.loc[['李四', '王二', '丁一'], :])



