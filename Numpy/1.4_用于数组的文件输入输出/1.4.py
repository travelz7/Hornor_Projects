import numpy as np

# np.save,np.load是读写磁盘中数组数据的两个主要函数
# 默认情况下，数组是以未压缩的原始二进制格式保存在扩展名为.npy的文件中的
arr = np.arange(10)
np.save('some_array', arr)

# 如果文件路径末尾没有扩展名.npy，则扩展名会被自动加上
# 然后可以通过np.load读取磁盘上的数组
print(np.load('some_array.npy'))

# 通过np.savez可以将多个数组保存到一个未压缩文件中，将数组以关键字的形式传入即可
np.savez('array_archive', a=arr, b=[1, 2])           # archive ----> 档案文件
arch = np.load('array_archive.npz')
print(arch['b'])

# 如果要将数据压缩，可以使用numpy.savez_compressed
np.savez_compressed('array_compressed.npz', a=arr, b=arr)
