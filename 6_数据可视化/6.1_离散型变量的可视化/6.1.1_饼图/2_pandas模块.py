# 导入第三方模块
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# 构建序列
data1 = pd.Series({'中专':0.2515,'大专':0.3724,'本科':0.3336,'硕士':0.0368,'其他':0.0057})
# 将序列名称设置为空字符，否则绘制的图形左边会出现None的字眼
data1.name = ''
# 控制饼图为正圆，即保持坐标轴比例相等
plt.axes(aspect='equal')
# 解决中文乱码
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# 绘图
data1.plot(kind='pie', #选择图形类型
           autopct='%.1f%%', #并图中添加数值标签
           radius=1, #设置饼图半径
           startangle=180, #设置饼图的初始角度
           counterclock=False, #将饼图的顺序设置为顺时针方向
           title='是新用户的受教育水平分布', #添加标题
           wedgeprops={'linewidth':1.5,'edgecolor':'blue'}, #设置饼图内边界的属性值
           textprops={'fontsize':10,'color':'black'} #设置文本标签的属性值
           )
plt.show()