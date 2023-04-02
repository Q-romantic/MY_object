# -*- coding: utf-8 -*-
"""
@Time    : 2022/6/30  030 下午 15:50
@Author  : Jan
@File    : 时钟.py
"""

from tkinter import *
import math, time
from PIL import Image, ImageTk


# 定义时针上的刻度1~12
def points():
    # 绘制表盘数字
    for i in range(1, 13):
        # 表盘中心的位置是200,200，由此计算刻度的位置
        x = 200 + 120 * math.sin(2 * math.pi * i / 12)
        y = 200 - 120 * math.cos(2 * math.pi * i / 12)
        canvas.create_text(x, y, text=i, font=('黑体', 18), fill='Navy')  # 颜色是海军蓝
    # 绘制表盘刻度
    for i in range(1, 61):  # 定义时针刻度（1~12h）
        if i % 5 == 0:  # 5的倍数要长一些
            r = 150
        else:
            r = 145
        x = 200 + 140 * math.sin(2 * math.pi * i / 60)
        y = 200 - 140 * math.cos(2 * math.pi * i / 60)
        x2 = 200 + r * math.sin(2 * math.pi * i / 60)
        y2 = 200 - r * math.cos(2 * math.pi * i / 60)
        canvas.create_line(x, y, x2, y2)


# 定义指针
def createline(radius, line_width, rad):
    x = 200 + radius * math.sin(rad)
    y = 200 - radius * math.cos(rad)
    i = canvas.create_line(200, 200, x, y, width=line_width, fill='black')
    List.append(i)


root = Tk()
root.attributes('-topmost', True)  # 窗口置顶
root.title("驯鹿时钟")
root.geometry("400x500")
canvas = Canvas(root, width=400, height=500)
canvas.pack()
# 生成外圆，圆内填充颜色是白色
canvas.create_oval(50, 50, 350, 350, fill='white')
# 绘制表盘中央的驯鹿图片
path1 = "test.jpg"
load = Image.open(path1)
render = ImageTk.PhotoImage(load)
canvas.create_image(195, 200, image=render)  # 这个位置是自己调的
List = []  # 用来记录绘制的图形编号

points()

# 定义循环
while True:
    try:
        tm = time.localtime()  # 获取当前时间
        t_hour = 0
        # 转换成12小时制
        if tm.tm_hour <= 12:
            t_hour = tm.tm_hour
        else:
            t_hour = tm.tm_hour - 12
        # 定义指针大小
        rad1 = 2 * math.pi * (t_hour + tm.tm_min / 60) / 12  # 时针
        rad2 = 2 * math.pi * (tm.tm_min + tm.tm_sec / 60) / 60  # 分针
        rad3 = 2 * math.pi * tm.tm_sec / 60  # 秒针
        # 画指针
        createline(50, 6, rad1)  # 时针
        createline(90, 3, rad2)  # 分针
        createline(120, 1, rad3)  # 秒针
        # 显示数字时间
        cur_time = time.strftime('%Y-%m-%d\n\n %X', time.localtime())
        time_text = canvas.create_text(200, 420, text=cur_time, font=10, fill='purple')
        root.update()
        time.sleep(1)  # 每秒刷新一次
        # 删除画布上的之前绘制的图形，否则有残影
        for j in List:
            canvas.delete(j)
        canvas.delete(time_text)
    except:
        break

root.mainloop()
