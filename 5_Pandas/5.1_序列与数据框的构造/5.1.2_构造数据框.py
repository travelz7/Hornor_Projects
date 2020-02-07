import pandas as pd
import numpy as np

# 构造数据框
df1 = pd.DataFrame([['张三', 23, '男'], ['李四', 27, '女'], ['王二', 26, '女']])
df2 = pd.DataFrame({'姓名': ['张三', '李四', '王二'],
                    '年龄': [23, 27, 26],
                    '性别': ['男', '女', '女']})
df3 = pd.DataFrame(np.array([['张三', 23, '男'], 
                             ['李四', 27, '女'],
                             ['王二', 26, '女']]))
print('嵌套列表构造数据框：\n', df1)
print('字典构造数据框：\n', df2)
print('二维数组构造数据框：\n', df3)
