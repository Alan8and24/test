#本题主要用的是matplotlib和pandas
#需要将此代码与'田字型散点.csv'放在同一路径下
#代码中先使用pandas读取csv文件，并将横坐标、纵坐标和标签分别保存在x、y和labels变量中，
#然后使用matplotlib库中的scatter()函数绘制散点图，并根据标签的不同将点的颜色分别设置为蓝色和红色。再画上xy轴最后添加图例、标题和标签，并显示图像。

import matplotlib.pyplot as plt
import pandas as pd

# 读取csv文件
df = pd.read_csv('田字型散点.csv', header=None)

# 获取x坐标、y坐标、标签
x = df.iloc[0].values
y = df.iloc[1].values
labels = df.iloc[2].values

#将x轴y轴显现出来
fig, ax = plt.subplots()

ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 绘制散点图
plt.scatter(x[labels==0], y[labels==0], c='blue')
plt.scatter(x[labels==1], y[labels==1], c='red')

# 添加图例、标题和标签
plt.legend(['label 0', 'label 1'])
plt.title('Scatter Plot of Point Labels')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 显示图像
plt.show()
