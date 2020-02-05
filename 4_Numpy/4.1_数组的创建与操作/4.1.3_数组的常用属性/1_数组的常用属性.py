import numpy as np
stu_score = np.genfromtxt(fname='D:/Python/Projects/4_Numpy/Data/4.1.3_数组的常用属性.txt',
                          delimiter='\t', skip_header=1)
# \t是Tab键打出的空格
print(type(stu_score))
print(stu_score.ndim)
print(stu_score.shape)
print(stu_score.dtype)
print(stu_score.size)
