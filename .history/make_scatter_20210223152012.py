'''
Author: your name
Date: 2021-02-20 08:00:13
LastEditTime: 2021-02-23 15:20:12
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Matplotlib\make_scatter.py
'''
import matplotlib.pyplot as plt

x_value = [1, 2, 3, 4, 5]
y_value = [1, 2, 9, 16, 25]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_value, y_value, s=200) #todo 其中s=200是指定点的大小

ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()