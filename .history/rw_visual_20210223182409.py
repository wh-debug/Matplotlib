'''
Author: your name
Date: 2021-02-23 18:21:32
LastEditTime: 2021-02-23 18:24:09
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Matplotlib\rw_visual.py
'''
import matplotlib.pyplot as plt
from randowwalk import Randomwalk

rw = Randomwalk()
re.fill_walk()
plt.style.use('classic')
fig, ax = plt.subplots()

ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()