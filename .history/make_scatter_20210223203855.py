'''
Author: your name
Date: 2021-02-20 08:00:13
LastEditTime: 2021-02-23 15:27:46
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Matplotlib\make_scatter.py
'''
import matplotlib.pyplot as plt

x_value = range(1, 1001)
y_value = [x**2 for x in x_value] #todo 使用for循环来进行计算

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()

ax.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, s=10) #todo 其中s=200是指定点的大小 也可以指定曲线颜色。也可以指定RGB颜色
#todo 并且使用了颜色的映射

ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

ax.axis([0, 1100, 0, 1100000]) #todo 设置每个坐标轴的取值范围
plt.show()