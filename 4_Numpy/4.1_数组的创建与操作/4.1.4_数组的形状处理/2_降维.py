import numpy as np
arr4 = np.array([[1, 10, 100], [2, 20, 200], [3, 30, 300]])
print('原数组：\n', arr4)

# 默认排序降维
print('数组降维：\n', arr4.ravel())
print(arr4.flatten())
print(arr4.reshape(-1))

# 改变排序模式的降维
print(arr4.ravel(order='F'))
print(arr4.flatten(order='F'))
print(arr4.reshape(-1, order='F'))

# 更改预览值
arr4.flatten()[0] = 2000
print('flatten方法：\n', arr4)
arr4.ravel()[1] = 1000
print('ravel方法：\n', arr4)
arr4.reshape(-1)[2] = 3000
print('reshape方法：\n', arr4)

arr5 = np.array([1, 2, 3])
print('vstack纵向堆叠数组：\n', np.vstack([arr4, arr5]))
print('row_stack纵向堆叠数组：\n', np.row_stack([arr4, arr5]))
arr6 = np.array([[5], [15], [25]])
print('hstack横向合并数组：\n', np.hstack([arr4, arr6]))
print('column_stack横向合并数组：\n', np.column_stack([arr4, arr6]))