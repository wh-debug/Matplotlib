'''
Author: your name
Date: 2021-02-20 08:00:13
LastEditTime: 2021-02-20 08:18:04
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Matplotlib\make_scatter.py
'''
import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()