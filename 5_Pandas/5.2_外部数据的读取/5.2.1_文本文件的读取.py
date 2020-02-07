import pandas as pd

# 读取文本文件中的数据
user_income = pd.read_table(
    r'D:\Python\Projects\5_Pandas\Data\第5章 Python数据处理工具--Pandas\data_test01.txt',
    sep=',', parse_dates={'birthday': [0, 1, 2]}, skiprows=2, skipfooter=3,
    comment='#', encoding='utf-8', thousands='&', engine='python')
print(user_income)
