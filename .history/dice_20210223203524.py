'''
Author: your name
Date: 2021-02-23 20:07:30
LastEditTime: 2021-02-23 20:35:24
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Matplotlib\dice.py
'''
from make_plotly import Die
import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5, 6]
y_values = []

die = Die()

#todo 创建一个空列表结果存储在空列表中
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value) #todo value是数字几，就会统计列表中相应数字个数
    frequencies.append(frequency)



print(frequencies)
