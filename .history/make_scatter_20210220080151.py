'''
Author: your name
Date: 2021-02-20 08:00:13
LastEditTime: 2021-02-20 08:01:51
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Matplotlib\make_scatter.py
'''
import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2, 4)

plt.show()