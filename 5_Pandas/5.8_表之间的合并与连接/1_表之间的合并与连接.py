import pandas as pd

df1 = pd.DataFrame({'name': ['张三', '李四', '王二'],
                    'age': [21, 25, 22],
                    'gender': ['男', '女', '男']})
df2 = pd.DataFrame({'name': ['丁一', '赵五'],
                    'age': [23, 22],
                    'gender': ['女', '女']})
# print(df1)
# print(df2)
# 数据集的纵向合并
# keys：为合并后的数据添加新索引，用于区分各个数据部分
x1 = pd.concat([df1, df2], keys=['df1', 'df2'])
print('合并df1，df2：\n', x1)
df2 = pd.DataFrame({'Name': ['丁一', '赵五'],
                    'age': [23, 22],
                    'gender': ['女', '女']})
# 数据集的纵向合并
x2 = pd.concat([df1, df2])
print('合并df1，df2：\n', x2)

df3 = pd.DataFrame({'id': [1, 2, 3, 4, 5],
                    'name': ['张三', '李四', '王二', '丁一', '赵五'],
                    'age': [27, 24, 25, 23, 25],
                    'gender': ['男', '男', '男', '女', '女']})
df4 = pd.DataFrame({'Id': [1, 2, 3, 4, 4, 4, 5],
                    'score': [83, 81, 87, 75, 86, 74, 88],
                    'kemu': ['科目1', '科目1', '科目2', '科目1', '科目2', '科目3', '科目1']})
df5 = pd.DataFrame({'id': [1, 3, 5],
                    'name': ['张三', '王二', '赵五'],
                    'income': [13500, 18000, 15000]})
# 三表的数据连接
# 首先df3和df4连接
merge1 = pd.merge(left=df3, right=df4, how='left', left_on='id', right_on='Id')
print('merge1:\n', merge1)
merge2 = pd.merge(left=merge1, right=df5, how='left')
print('merge2:\n', merge2)

