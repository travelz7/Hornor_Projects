import pandas as pd

child_cloth = pd.read_excel(
    io=r'D:\Python\Projects\5_Pandas\Data\第5章 Python数据处理工具--Pandas\data_test02.xlsx',
    hearder=None, converters={0: str}, names=['商品ID', '商品名称', '商品颜色', '商品价格']
                            )

print(child_cloth)

# python操作excel主要用到xlrd和xlwt这两个库，即xlrd是读excel，xlwt是写excel的库
