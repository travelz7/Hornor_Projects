# 下面以“芝麻信用”失信用户数据为例（数据来源于财新 网），分析近300万失信人群的学历分布，pie函数绘制饼图的详细代码

# 导入第三方模块
import matplotlib
import matplotlib.pyplot as plt

# 构造数据
edu = [0.2515, 0.3724, 0.3336, 0.0368, 0.0057]
labels = ['中专', '大专', '本科', '硕士', '其他']
# 突出显示大专学历人群
explode = [0, 0.1, 0, 0, 0]
# 自定义颜色
colors = ['gray', 'red', 'blue', 'yellow', 'darkgreen']

# 解决汉字乱码问题
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# 解决负号问题
plt.rcParams['axes.unicode_minus'] = False
# 绘制饼图
plt.pie(x=edu,  # 绘图数据
        explode=explode,  # 突出显示大专人群
        colors=colors,  # 自定义填充颜色
        labels=labels,  # 添加教育水平标签
        autopct='%.1f%%',  # 设置百分比的格式，这里保留一位小数
        pctdistance=0.8,  # 设置百分比标签与圆心的距离
        labeldistance=1.1,  # 设置教育水平标签与圆心的距离
        startangle=180,  # 设置饼图的初始角度
        radius=1.2,  # 设置饼图半径
        counterclock=False,  # 是否逆时针，这里设置为顺时针
        wedgeprops={'linewidth':1, 'edgecolor':'green'},  # 设置饼图内外边界的属性值
        textprops={'fontsize':10, 'color':'black'}  # 设置文本标签的属性值
        )
# 显示图标题
plt.title('失信用户的受教育水平分布')
# 显示图形
plt.show()