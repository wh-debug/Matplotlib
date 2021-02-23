'''
Author: your name
Date: 2021-02-23 20:07:30
LastEditTime: 2021-02-23 20:45:42
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
    frequency = results.count(value)    #todo value是数字几，就会统计列表中相应数字个数
    frequencies.append(frequency)

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
y_values = frequencies
ax.scatter(x_values, y_values, c='green', s = 100)

ax.set_title("骰子朝上统计", fontsize=24)
ax.set_xlabel("次数", fontsize=14)
ax.set_ylabel("骰子值", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)
plt.show()
print(frequencies)
