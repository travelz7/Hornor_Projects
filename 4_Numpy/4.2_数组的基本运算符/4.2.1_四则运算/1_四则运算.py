import numpy as np

# 加法运算
math = np.array([98, 83, 86, 92, 67, 82])
english = np.array([68, 74, 66, 82, 75, 89])
chinese = np.array([92, 83, 76, 85, 87, 77])
tot_symbol = math+english+chinese
tot_fun = np.add(np.add(math, english), chinese)
print('符号加法：\n', tot_symbol)
print('函数加法：\n', tot_fun)

# 除法运算
height = np.array([165, 177, 158, 169, 173])
weight = np.array([62, 73, 59, 72, 80])
BMI_symbol = weight/(height/100)**2
BMI_fun = np.divide(weight, np.divide(height, 100)**2)
print('符号除法：\n', BMI_symbol)
print('函数除法：\n', BMI_fun)

arr7 = np.array([[1, 2, 10], [10, 8, 3], [7, 6, 5]])
arr8 = np.array([[2, 2, 2], [3, 3, 3], [4, 4, 4]])
print('数组arr7:\n', arr7)
print('数组arr8:\n', arr8)
# 求余数
print('计算余数：\n', arr7 % arr8)
# 求整除
print('计算整除：\n', arr7 // arr8)
# 求指数
print('计算指数：\n', arr7 ** arr8)
