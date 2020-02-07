import pandas as pd

df = pd.read_excel(r'D:\Python\Projects\5_Pandas\Data\第5章 Python数据处理工具--Pandas\data_test04.xlsx')
print('数据中是否存在重复观测：\n', any(df.duplicated()))
# 删除重复项
df.drop_duplicates(inplace=True)
print(df)
