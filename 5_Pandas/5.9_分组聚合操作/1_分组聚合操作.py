import pandas as pd
import numpy as np

diamonds = pd.read_table(r'D:\Python\Projects\5_Pandas\Data\第5章 Python数据处理工具--Pandas\diamonds.csv', sep=',')
grouped = diamonds.groupby(by=['color', 'cut'])
result = grouped.aggregate({'color': np.size,
                            'carat': np.min,
                            'price': np.mean,
                            })
print('初步处理：\n', result)
result = pd.DataFrame(result, columns=['color', 'carat', 'price', ])
print('顺序调整：\n', result)
result.rename(columns={'color': 'counts',
                       'carat': 'min_weight',
                       'price': 'avg_price',
                       },
              inplace=True)
print('数据集重命名：\n', result)
result.reset_index(inplace=True)
print('将行索引转换为数据库的变量：\n', result)





