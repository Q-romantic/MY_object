# -*- coding: utf-8 -*-
"""
@Time    : 2023/2/25  025 下午 14:48
@Author  : Jan
@File    : 多线程写入一个文件.py
"""
import threading
import random
import time

""" {} """

N = 30


# 假设每次写入时间不固定，这里随机睡眠，模拟下
def set_random_write_time(string):
    t = random.random()
    print(t, '=====', string)
    time.sleep(t)


# 1、乱序多线程写入，除了乱序，还会产生数据丢失，空白行
def write_string(string, path="aaa.csv"):
    with open(path, 'a') as f:
        set_random_write_time(string)
        f.write(string + "\n")


# 创建新线程
for i in range(N):
    # 这里每次循环都开一个线程，并写入"write_string:" + i，args里指定参数，注意要使用list[]格式
    thread1 = threading.Thread(target=write_string, args=["write_string: " + str(i)])
    thread1.start()

pass
time.sleep(2)

# 2、正序多线程写入
threadLock = threading.Lock()


def write_string(string, path="aaa.csv"):
    threadLock.acquire()  # 加个同步锁就好了
    with open(path, 'a') as f:
        set_random_write_time(string)
        f.write(string + "\n")
    threadLock.release()


# 创建新线程
for i in range(N):
    thread2 = threading.Thread(target=write_string, args=["write_string: " + str(i)])
    thread2.start()
