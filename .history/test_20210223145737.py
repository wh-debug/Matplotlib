'''
Author: your name
Date: 2021-02-23 14:57:33
LastEditTime: 2021-02-23 14:57:37
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Matplotlib\test.py
'''
import matplotlib.pyplot as plt
from matplotlib import font_manager

for font in font_manager.fontManager.ttflist:
    # 查看字体名以及对应的字体文件名
    print(font.name, '-', font.fname)

    