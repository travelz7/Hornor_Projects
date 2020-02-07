import pymysql
import pandas as pd

# 连接Mysql数据库
conn = pymysql.connect(host='localhost', user='root', password='zs960114.',
                       database='runoob', port=3306, charset='utf8')
# 读取数据
user = pd.read_sql('select * from apps', conn)
# 关闭连接
conn.close()
# 数据输出
print(user)