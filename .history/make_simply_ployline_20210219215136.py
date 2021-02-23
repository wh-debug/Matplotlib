'''
Author: 零到正无穷
Date: 2021-02-19 21:20:37
LastEditTime: 2021-02-19 21:51:36
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Matplotlib\make_simply_ployline.py
'''
import matplotlib.pyplot as plt 

input_values = [1, 2, 3, 4, 5]
square = [1, 4, 9, 16, 25]

plt.style.use('Solarize_Light2') #todo 使用内置显示格式(或者显示方法)

fig, ax = plt.subplots()
ax.plot(input_values, square, linewidth=3)

ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值得平方", fontsize=14) #todo 注意label而不是lable

ax.tick_params(axis='both', labelsize=14)

plt.show()