'''
Author: your name
Date: 2021-02-23 20:07:30
LastEditTime: 2021-02-23 20:26:25
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Matplotlib\dice.py
'''
from make_plotly import Die

die = Die()

#todo 创建一个空列表结果存储在空列表中
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
