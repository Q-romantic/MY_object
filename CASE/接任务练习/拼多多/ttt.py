# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/13  013 下午 18:05
@Author  : Jan
@File    : ttt.py
"""
import time

""" {} """

now = time.time()
time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now))
day = time_str.split()[0].split('-')
start_time = day[0] + '-' + day[1] + '-' + str(int(day[2]) - 1) + " 00:00:0"
end_time = day[0] + '-' + day[1] + '-' + str(int(day[2])) + " 00:00:00"
start_time_stamp = time.mktime(time.strptime(start_time, '%Y-%m-%d %H:%M:%S'))
# print(start_time_stamp)
end_time_stamp = time.mktime(time.strptime(end_time, '%Y-%m-%d %H:%M:%S'))
# print(end_time_stamp)
