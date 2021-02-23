'''
Author: your name
Date: 2021-02-23 19:05:50
LastEditTime: 2021-02-23 20:05:56
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Matplotlib\make_plotly.py
'''
from random import randint

class Die:
    """表示一个骰子的类"""
    def __init__(self, num_sides=6):
        """骰子默认六个面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机值"""
        return randint(1, self.num_sides)
        