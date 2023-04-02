# -*- coding: utf-8 -*-
import json
import pprint
from tkinter import scrolledtext

import m3u8
import parsel
import requests

# from working.IP_Headers_Proxies import headers
# from working.IP_Headers_Proxies import str_to_dic

# url = 'https://mapi.guazi.com/car-source/carList/pcList'
# for page in range(1, 6):
#     params = {
#         'page': page,
#         'pageSize': '20',
#         'city_filter': '12',
#         'city': '12',
#         'guazi_city': '12',
#         'deviceId': 'd4500b77-400c-44bd-8f79-cbded611069a',
#     }
#     response = requests.get(url, headers=headers, params=params)
#     pprint.pprint(response.json())


# def str_to_dic(s: str, flags: [bool, int] = 0) -> dict:
#     import re
#     from working.IP_Headers_Proxies import headers
#     # pattern = '^(.*?):\s{0,}(.*)$'    # 上下等价
#     pattern = '^(.*?):\s*(.*)$'
#     h = headers
#     for line in s.splitlines():
#         if line == '' or line.startswith('#'):
#             continue
#         s = re.sub(pattern, '{\'\\1\': \'\\2\'}', line)
#         h.update(eval(s))
#         if flags:
#             print(re.sub(pattern, "\'\\1\': \'\\2\',", line))
#     return h


headers_str = """Host: sou.zhaopin.com
origin: https://sou.zhaopin.com
referer: https://sou.zhaopin.com/?p=3&jl=765&kw=python&kt=3
sec-fetch-dest:empty
sec-fetch-mode:    cors
sec-fetch-site: same-site
"""

# from tkinter import *
# import easygui
#
# master = Tk()
#
# frame = Frame(master)  # 确定一个框架用于美观
#
# frame.pack(padx=20, pady=20)
#
# v1 = StringVar()  # 分别用于储存需要计算的数据和 结果
# v2 = StringVar()
# v3 = StringVar()
#
#
# def test(content):
#     return content.isdigit()  # 检查是不是数字 .
#
#
# testCMD = frame.register(test)  # 将函数 进行包装 .
#
# e1 = Entry(frame, width=60, textvariable=v1, validate='key', validatecommand=(test, '%p')).grid(row=0, column=0, pady=10)  # %p 是输入框的最新内容 . 当输入框允许改变的时候该值有效 ,
# Label(frame, text='', padx=10).grid(row=0, column=1)
#
# e2 = Entry(frame, width=10, textvariable=v2, validate='key', validatecommand=(test, '%p')).grid(row=0, column=2)
# Label(frame, text='', padx=10).grid(row=0, column=3)
#
# e3 = Entry(frame, width=60, textvariable=v3, state='readonly').grid(row=0, column=4)
#
#
# def calc():
#     if v1.get() == '':
#         easygui.msgbox('请先输入内容 !')
#         return
#     result = int(v1.get()) + int(v2.get())
#     v3.set(result)
#
#
# Button(frame, text='计算结果', command=calc).grid(row=1, column=2, pady=5)
#
# mainloop()

# from tkinter import *
#
# root = Tk()  # 建立tkinter窗口
# root.title("headers")  # 设置标题
# text = Text(
#     root,
#     # width=60,
#     # height=60,
#     # padx=20,
#     # pady=20,
#     highlightcolor='red',
#     highlightthickness=1
# )  # 这个意思是每行三十个字符  两行 .
#
# text.pack()
# text.grid(
#     row=0,
#     column=0,
#     padx=10,
#     pady=10,
# )
# root.geometry("600x800")
# text.insert(INSERT, "I Love \n")  # 第一个表示插入的位置　第二个是内容　其中第一个必须有　，　INSERT　是光标所在位置
# text.insert(END, "Fishc.com !")  # END 表示 在上一次输入结束的位置继续 .
#
# mainloop()

# import tkinter as tk
# from tkinter import INSERT
# from tkinter import END
#
# app = tk.Tk()
# app.title("test")
# entryExample1 = tk.Text(app, highlightcolor='red', highlightthickness=1)
# entryExample2 = tk.Text(app, highlightcolor='red', highlightthickness=1)
# entryExample3 = tk.Text(app, highlightcolor='red', highlightthickness=1)
#
# entryExample1.grid(
#     row=65,
#     column=65,
#     padx=10,
#     pady=10,
#     # ipadx=1,
#     # ipady=1,
# )
# entryExample2.grid(row=0,
#                    column=1,
#                    padx=10,
#                    pady=10,
#                    ipadx=65,
#                    ipady=280)
# entryExample3.grid(row=1,
#                    column=0,
#                    padx=10,
#                    pady=10,
#                    ipadx=65,
#                    ipady=10)

# app.geometry("600x800")
# entryExample1.insert(INSERT, "I Love \n")
# entryExample1.insert(END, "Fishc.com !")
# app.mainloop()

# coding:utf-8
# from tkinter import *
# root = Tk()
# root.title("test")
# root.geometry("600x800")
# root.resizable(width=False, height=False)
# l = Entry(root, highlightcolor='red', highlightthickness=1)  # highlightcolor:颜色
# l.place(width=300, height=100)  # width:长度；height:高度
# root.mainloop()


# import tkinter as tk
#
# app = tk.Tk()
# app.geometry("600x800")
#
# textExample1 = tk.Text(
#     app,
#     width=10,  # 文本框宽度
#     height=5,  # 文本框高度的一半
#     highlightcolor='red',  # 边框颜色
#     highlightthickness=1,  # 加粗
# )
#
# textExample1.pack(
#     side=tk.LEFT,  # 左对齐
#     padx=10,  # 左右边距
# )
# textExample1.place(
#     x=10,   # 左边距
#     y=10,   # 上边距
#     # width=200,
#     # height=100,
# )
#
# textExample2 = tk.Text(
#     app,
#     width=10,  # 文本框宽度
#     height=5,  # 文本框高度的一半
#     highlightcolor='red',  # 边框颜色
#     highlightthickness=1,  # 加粗
# )
#
# textExample2.pack(
#     side=tk.RIGHT,  # 左对齐
#     padx=10,  # 左右边距
# )
#
# textExample3 = tk.Text(
#     app,
#     width=10,  # 文本框宽度
#     height=5,  # 文本框高度的一半
#     highlightcolor='red',  # 边框颜色
#     highlightthickness=1,  # 加粗
# )
#
# textExample3.pack(
#     side=tk.LEFT,  # 左对齐
#     padx=10,  # 左右边距
# )
# textExample4 = tk.Text(
#     app,
#     width=10,  # 文本框宽度
#     height=5,  # 文本框高度的一半
#     highlightcolor='red',  # 边框颜色
#     highlightthickness=1,  # 加粗
# )
#
# textExample4.pack(
#     side=tk.BOTTOM,  # 左对齐
#     pady=10,  # 上下边距
# )
# textExample4.place(
#     # x=100,   # 左边距
# )
# app.mainloop()


# import tkinter as tk
#
# root = tk.Tk()
#
# letter = ['A', 'B', 'C', 'D']
#
# for i in letter[:-1]:
#     tk.Label(root, text=i, relief='groove').pack(anchor='w', fill='y', expand=True)
# for i in letter[-1:]:
#     tk.Label(root, text=i, relief='groove').pack(anchor='e', fill='y', expand=True)
#
# root.mainloop()


# import tkinter
# from tkinter import ttk, scrolledtext
# from tkinter import INSERT
# from tkinter import END
#
# win = tkinter.Tk()
# win.title("Kahn Software v1")  # #窗口标题
# # win.geometry("600x800")  # #窗口位置500后面是字母x
# win.geometry()  # #窗口位置500后面是字母x
# # win.state('zoomed')   # 窗口最大化
# # win.attributes('-fullscreen', True)  # 窗口全屏
# win.attributes('-topmost', True)  # 窗口置顶
# '''
# 相对布局,窗体改变对空间有影响
# '''
#
# text1 = scrolledtext.ScrolledText(win, highlightcolor='red', highlightthickness=1.5)
# text2 = scrolledtext.ScrolledText(win, highlightcolor='red', highlightthickness=1.5)
# text3 = scrolledtext.ScrolledText(win, highlightcolor='red', highlightthickness=1.5)
# text4 = scrolledtext.ScrolledText(win, highlightcolor='red', highlightthickness=1.5)
#
# # text1.tag_configure("center", justify='center')
# # text1.tag_add("center", 1.0, "end")
#
# """
# Host: www.bilibili.com
# referer: https://www.bilibili.com/
# """
#
#
# # 第6步，获取文本框输入
# def getTextInput():
#     # Tkinter 文本框控件中第一个字符的位置是 1.0，可以用数字 1.0 或字符串"1.0"来表示。
#     # "end"表示它将读取直到文本框的结尾的输入。我们也可以在这里使用 tk.END 代替字符串"end"。
#     def s_to_dic(title, s):
#         dic = dict([line.split(": ", 1) for line in s.split("\n") if line != ''])
#         data = json.dumps(dic, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':'))
#         text4.insert(INSERT, f"\n{title} = {data}\n")
#
#     s = text1.get(1.0, END)  # 获取文本输入框的内容
#     s_to_dic('headers', s)
#
#     s = text2.get(1.0, END)  # 获取文本输入框的内容
#     s_to_dic('params', s)
#
#     s = text3.get(1.0, END)  # 获取文本输入框的内容
#     s_to_dic('data', s)
#
#
# # 第7步，在图形化界面上设定一个button按钮（#command绑定获取文本框内容的方法）
# btnRead = tkinter.Button(win, height=1, width=5, text="Read", command=getTextInput)  # command绑定获取文本框内容的方法
# # 第8步，安置按钮
# btnRead.pack(fill=tkinter.Y, side=tkinter.RIGHT, expand=False)  # 显示按钮
#
#
# tkinter.Label(win, text='headers', anchor='w', padx=10).pack(fill=tkinter.X, side=tkinter.TOP)
# # tkinter.Label(win, text='copy', anchor='e', padx=10).pack(fill=tkinter.Y, side=tkinter.TOP)
#
# text4.pack(fill=tkinter.Y, side=tkinter.RIGHT, expand=True, anchor='center')
# text1.pack(fill=tkinter.X, side=tkinter.TOP, expand=True)
# tkinter.Label(win, text='params', anchor='w', padx=10).pack(fill=tkinter.X, side=tkinter.TOP)
# text2.pack(fill=tkinter.X, side=tkinter.TOP, expand=True)
# tkinter.Label(win, text='data', anchor='w', padx=10).pack(fill=tkinter.X, side=tkinter.TOP)
# text3.pack(fill=tkinter.X, side=tkinter.TOP, expand=True)
#
# win.mainloop()  # #窗口持久化


from tkinter import *

'''
创建一个文本框，在文本框中点击右键弹出“剪切、复制、粘贴”菜单，
并实现其功能。
'''
# root = Tk()
# root.title("绑定鼠标右键测试")
# root.geometry("500x300")
# t = Entry(root, width=51, font=("微软雅黑", 10))
# t.place(x=40, y=100, height="35px")
#
#
# def callback1(event=None):
#     global root
#     t.event_generate('<<Cut>>')
#
#
# def callback2(event=None):
#     global root
#     t.event_generate('<<Copy>>')
#
#
# def callback3(event=None):
#     global root
#     t.event_generate('<<Paste>>')
#
#
# '''创建一个弹出菜单'''
# menu = Menu(root,
#             tearoff=False,
#             # bg="black",
#             )
# menu.add_command(label="剪切", command=callback1)
# menu.add_command(label="复制", command=callback2)
# menu.add_command(label="粘贴", command=callback3)
#
#
# def popup(event):
#     menu.post(event.x_root, event.y_root)  # post在指定的位置显示弹出菜单
#
#
# t.bind("<Button-3>", popup)  # 绑定鼠标右键,执行popup函数
# root.mainloop()


# from tkinter import *
#
# class Application(Frame):
#     def __init__(self, master):
#         self.root = master
#         self.frm1 = Frame(self.root)
#         self.createpage()
#
#         super(Application, self).__init__(master)
#         self.grid()
#         self.place(x=10, y=10)
#
#
#
#         self.bttn_clicks = 0
#         self.create_widget()
#     def create_widget(self):
#         self.bttn = Button(self)
#         self.bttn['text'] = "GO"
#         self.bttn['height'] = 3
#         self.bttn['width'] = 4
#         self.bttn['command'] = self.update_count
#         self.bttn.grid()
#     def update_count(self):
#         self.bttn_clicks += 1
#         if self.bttn_clicks %2==0:
#             self.bttn['text'] = "GO"
#         else:
#             self.bttn['text'] = "清除"
#
#     def createpage(self):
#         self.frm1.config(height=80, width=80)
#         Label(self.frm1, text='headers').place(anchor=NW)
#         self.frm1.place(x=10, y=5)
#         text1 = scrolledtext.ScrolledText(self.frm1, highlightcolor='red', highlightthickness=1.5)
#         text1.place(x=0, y=23, height=80, width=80)
#
#
# root = Tk()
# root.title("Click Counter")
# root.geometry('300x500')
# root.attributes('-topmost', True)  # 窗口置顶
# app = Application(root)
# root.mainloop()

# from tkinter import *
#
#
# def go():
#     txt = '窗口的左上角坐标为：（%s,%s）\n窗口的高度为：%s窗口的宽度为：%s' \
#           % (root.winfo_x(), root.winfo_y(), root.winfo_width(), root.winfo_height())
#     label1.configure(text=txt)
#     li = [root.winfo_width(), root.winfo_height(), root.winfo_x(), root.winfo_y()]
#     # print(li)
#     text1 = scrolledtext.ScrolledText(root, highlightcolor='red', highlightthickness=1.5)
#     text1.place(x=5, y=5, height=li[0] - 100, width=li[1] - 100)
#     root.after(17, go)
#
#
#
# root = Tk()
# root.geometry("300x200+100+50")
# label1 = Label(root)
# label1.pack(expand=YES)
# frm1 = Frame(root)
#
# # frm1.config(height=33, width=32)
# # Label(frm1, bg='red', text='headers').place(anchor=NW)
# # frm1.place(x=10, y=5)
#
# li = go()
#
# root.mainloop()


play_list = m3u8.load('http://1306251229.vod2.myqcloud.com/2d6b49e9vodtranscq1306251229/18123491387702302076299704/adp.10.m3u8?t=7fffffff&exper=30&us=81dd710dad414b55b3a4e799ab1f57c2&sign=2c915945a2fba36b4f81a50a872d6e0b')

for index, segment in enumerate(play_list.segments):
    ur = segment.uri
    print(ur)