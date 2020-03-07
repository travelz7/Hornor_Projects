import pandas as pd
import numpy as np

data = pd.read_csv(
    r'D:\\Python\Projects\\5_Pandas\Data\\fd-export.csv'
)
data = data.loc[0: 1000, ['user_id', 'age', 'sex', 'country', 'trackable_value']]
# 去除重复值
data.drop_duplicates(inplace=True)
# 去除缺失值
data.dropna(inplace=True)
data.age = pd.to_numeric(data.age[:-1], errors='coerce')
data.trackable_value = pd.to_numeric(data.trackable_value[:-1], errors='coerce')
# 按国家和性别分组
data = data.groupby(by=['country', 'sex'])
data = data.aggregate({
    'age': np.mean,
    'trackable_value': np.mean
})
print(data)




