import pandas as pd
import numpy as np
# pd.set_option('display.max_columns', None)   #显示完整的列
# pd.set_option('display.max_rows', None)  #显示完整的行
# 数据读取
sec_cars = pd.read_table(r'D:\Python\Projects\5_Pandas\Data\第5章 Python数据处理工具--Pandas\sec_cars.csv',
                         sep=',')
# 预览数据的前五行
print(sec_cars.head())
# 查看数据的行列数
print('数据集的行列数：\n', sec_cars.shape)
# 查看数据集每个变量的数据类型
print('各变量的数据类型：\n', sec_cars.dtypes)
# 修改二手车上牌时间的数据类型
sec_cars.Boarding_time = pd.to_datetime(sec_cars.Boarding_time,
                                        format='%Y年%m月')
# 修改二手车新车价格的数据类型
# sec_cars.New_price = sec_cars.New_price.str[:-1].astype('float')
# 数据源New_price中，即使去掉末尾的万字，仍不能保证数据源同质性，因为有些数据是“暂无”，暂并没有去掉
# sec_cars.New_price = pd.Series(sec_cars.New_price.str[:-1], dtype=float)
sec_cars.New_price = pd.to_numeric(sec_cars.New_price.str[:-1], errors='coerce')
# 这里去掉万字后，强制将剩下的所有数据类型转换为float64，出现错误即将其置为Nan，之后再将Nan填补，用fillna（）方法
# 如果不去掉万字，那么所有的数值都将被置为Nan
print('修改后的各变量的数据类型：\n', sec_cars.dtypes)
sec_cars.New_price = sec_cars.New_price.fillna(0)
# print(sec_cars)
print('数值型描述：\n', sec_cars.describe())
print('离散型描述：\n', sec_cars.describe(include='object'))
# 离散变量频次、频率统计
Freq = sec_cars.Discharge.value_counts()
Freq_ratio = Freq/sec_cars.shape[0]
Freq_df = pd.DataFrame({'频次': Freq, '频率': Freq_ratio})
print(Freq_df.head())
# 将航索引重设为变量
Freq_df.reset_index(inplace=True)
print(Freq_df.head())
# 挑出所有的数值型变量
num_variables = sec_cars.columns[sec_cars.dtypes != 'object'][1:]
print('num_variables:\n', num_variables)
# 上面得到的num_variables可以看作是一个DataFrame，虽然这里他的类型显示为object
# 自定义函数，计算偏度和峰度
def skew_kurt(x):
    skewness = x.skew()
    kurtsis = x.kurt()
    # 返回偏度值和峰度值
    return pd.Series([skewness, kurtsis], index=['Skew', 'Kurt'])
# 运用apply方法
x = sec_cars[num_variables].apply(func=skew_kurt, axis=0)   #默认axis=0，其实这里的 axis=0 可以省去
print('数值型数据的偏度和峰度：\n', x)
# -如果“raise”，则无效解析将引发异常
# -如果“coerce”，则无效解析将设置为NaN      coerce ---> 强迫；胁迫；迫使
# -如果“ignore”，则无效解析将返回输入

# to_numeric(arg, errors='raise', downcast=None)
#     Convert argument to a numeric type.
#
#     Parameters
#     ----------
#     arg : list, tuple, 1-d array, or Series
#     errors : {'ignore', 'raise', 'coerce'}, default 'raise'
#         - If 'raise', then invalid parsing will raise an exception
#         - If 'coerce', then invalid parsing will be set as NaN
#         - If 'ignore', then invalid parsing will return the input
#     downcast : {'integer', 'signed', 'unsigned', 'float'} , default None
#         If not None, and if the data has been successfully cast to a
#         numerical dtype (or if the data was numeric to begin with),
#         downcast that resulting data to the smallest numerical dtype
#         possible according to the following rules:
#
#         - 'integer' or 'signed': smallest signed int dtype (min.: np.int8)
#         - 'unsigned': smallest unsigned int dtype (min.: np.uint8)
#         - 'float': smallest float dtype (min.: np.float32)
#
#         As this behaviour is separate from the core conversion to
#         numeric values, any errors raised during the downcasting
#         will be surfaced regardless of the value of the 'errors' input.
#
#         In addition, downcasting will only occur if the size
#         of the resulting data's dtype is strictly larger than
#         the dtype it is to be cast to, so if none of the dtypes
#         checked satisfy that specification, no downcasting will be
#         performed on the data.