import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
# 读入数据
GDP = pd.read_excel(r'D:\Python\Projects\6_数据可视化\Data\Province GDP 2017.xlsx')
# 设置绘图风格（不妨使用R语言中的ggplot风格）
plt.style.use('ggplot')
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# 对读入的数据做升序排序
GDP.sort_values(by='GDP',inplace=True)
# bar是垂直条形图，barh是水平条形图
plt.bar(
        x=range(GDP.shape[0]), #指定条形图x轴的刻度值
        height=GDP.GDP, #指定条形图y轴的数值
        tick_label=GDP.Province, #指定条形图x轴的刻度标签
        color='steelblue', #指定条形图的填充色
        )
# 添加y轴的标签
plt.ylabel=('GDP(万亿)')
plt.title('2017年度6个省份GDP分布')
# 为每个条形图添加数值标签
for x, y in enumerate(GDP.GDP):
    plt.text(x, y+0.1, '%s' % round(y, 1), ha='center')
plt.show()
print(GDP.GDP)
# pyplot子模块中的text函数
# 前两个参数用于定位字符在图形中的位置
# 第三个参数表示呈现的具体字符值
# 第四个参数为ha，表示字符的水平对齐方式，此处为居中对齐
