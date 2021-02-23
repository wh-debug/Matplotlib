'''
Author: your name
Date: 2021-02-23 15:39:37
LastEditTime: 2021-02-23 18:02:14
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
