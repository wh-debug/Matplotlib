'''
Author: your name
Date: 2021-02-23 18:21:32
LastEditTime: 2021-02-23 18:49:22
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Matplotlib\rw_visual.py
'''
import matplotlib.pyplot as plt
from randowwalk import Randomwalk

while True:
    rw = Randomwalk()
    rw.fill_walk()
    plt.style.use('classic')
    fig, ax = plt.subplots()

    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)                          #todo 绘制起点
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)#todo 绘制终点

    #TODO 隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()

    keep_running = input("Make another walk? (y/n): " )
    if keep_running == 'n':
        break