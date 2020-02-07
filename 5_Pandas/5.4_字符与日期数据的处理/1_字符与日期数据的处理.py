import pandas as pd
import datetime

pd.set_option('display.max_rows', None)  #显示完整的行
pd.set_option('display.max_columns', None)   #显示完整的列
# 数据读入
df = pd.read_excel(r'D:\Python\Projects\5_Pandas\Data\第5章 Python数据处理工具--Pandas\data_test03.xlsx')
# 查看各变量数据类型
print(df.dtypes)
# 将birthday变量转换为日期型
df.birthday = pd.to_datetime(df.birthday, format='%Y/%m/%d')
# 将手机号转换为字符串
df.tel = df.tel.astype('str')
# 新增年龄和工龄两列
df['age'] = datetime.datetime.now().year - df.birthday.dt.year
df['workage'] = datetime.datetime.now().year - df.start_work.dt.year
# 将手机号中间四位隐藏起来
df.tel = df.tel.apply(func=lambda x: x.replace(x[3: 7], '****'))
# 取出邮箱的域名
df['email_domain'] = df.email.apply(func=lambda x: x.split('@')[1])
# 取出人员的专业信息
# findall() 查找所有符合正则表达式的字符，以数组形式返回
df['profession'] = df.other.str.findall('专业：(.*?)，')
# 去除birthday、start_work和other变量
df.drop(['birthday', 'start_work', 'other'], axis=1, inplace=True)
print(df.head())




# python中时间日期格式化符号：
#
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身