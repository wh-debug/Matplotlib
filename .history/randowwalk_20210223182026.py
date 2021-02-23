'''
Author: your name
Date: 2021-02-23 15:39:37
LastEditTime: 2021-02-23 18:20:26
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Matplotlib\randowwalk.py
'''
from random import choice

class Randomwalk:
    """一个生成随机漫步数据的类"""
    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步的所有的点"""
        while len(self.x_values) < self.num_points:
            #todo 决定前进方向以及沿着个方向前进的距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #todo 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

