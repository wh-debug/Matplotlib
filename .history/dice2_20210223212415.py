'''
Author: your name
Date: 2021-02-23 21:14:33
LastEditTime: 2021-02-23 21:23:50
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Matplotlib\dice2.py
'''
'''创建两个骰子投掷'''
from plotly.graph_objs import Bar, Layout
from plotly import offline

from make_plotly import Die

dice_1 = Die()
dice_2 = Die()

#todo 创建一个空列表结果存储在空列表中
results = []

for roll_num in range(1000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

#todo 分析结果
frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)    #todo value是数字几，就会统计列表中相应数字个数
    frequencies.append(frequency)

#todo 将数据进行可视化
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title':'结果', 'dtick': 1}
y_axis_config = {'title': '结果的频率'}
my_layout = Layout(title = '掷两个D6 1000次数结果', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data':data, 'layout': my_layout}, filename='d6_2.html')