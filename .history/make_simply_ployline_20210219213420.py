'''
Author: 零到正无穷
Date: 2021-02-19 21:20:37
LastEditTime: 2021-02-19 21:34:20
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Matplotlib\make_simply_ployline.py
'''
import matplotlib.pyplot as plt 

square = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(square, linewith=3)

ax.set_title("平方数"， fontsize=24)
ax.set_xlable("值", fontsize=14)
ax.set_ylable("值得平方", fontsize=14)

ax.tick_params(axis='both', lablesize=14)

plt.show()