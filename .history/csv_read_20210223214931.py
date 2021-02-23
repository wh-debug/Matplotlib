'''
Author: your name
Date: 2021-02-23 21:33:21
LastEditTime: 2021-02-23 21:49:31
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Matplotlib\csv_read.py
'''
"""分析CSV格式的数据"""
import csv

filename = 'sitka_weather_07-2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

for index, column_header in enumerate(header_row):
    print(index, column_header)