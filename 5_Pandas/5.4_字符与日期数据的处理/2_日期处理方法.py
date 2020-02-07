import pandas as pd

def get_weekdayName(x):
    weekdayName = {
        0: '星期一',
        1: '星期二',
        2: '星期三',
        3: '星期四',
        4: '星期五',
        5: '星期六',
        6: '星期七',
    }
    return weekdayName[x]

# 常用日期处理方法
dates = pd.to_datetime(pd.Series(['1989-8-18 13:14:55', '1995-2-16']),
                       format='%Y-%m-%d %H:%M:%S')
print(dates)
print('返回日期值：\n', dates.dt.date)
print('返回季度：\n', dates.dt.quarter)
print('返回几点钟：\n', dates.dt.hour)
print('返回年中的天：\n', dates.dt.dayofyear)
print('返回年中的周：\n', dates.dt.weekofyear)
# 原有方法weekday_name失效，原因不明，而weekday方法可以返回星期几索引，故自定义函数，根据索引确定星期几的名称
print('返回星期几的名称：\n', dates.dt.weekday.apply(func=get_weekdayName))
print('返回月份的天数：\n', dates.dt.days_in_month)



