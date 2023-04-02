# -*- coding: utf-8 -*-
import tkinter as tk

master = tk.Tk()
# 窗口命名
master.title("数据采集v1.0 --徐健")

# 窗口width不可变，height可变
master.resizable(width=False, height=True)
tk.Label(master, text="商品名称：").grid(row=0)
# tk.Label(master, text="作者：").grid(row=1)
e1 = tk.Entry(master)
# e2 = tk.Entry(master)
e1.grid(row=0, column=1, columnspan=4, padx=10, pady=5)
w = tk.Label(master, text=str(0))
tk.Button(master, text="终止爬取", width=8).grid(row=3, column=0, sticky="w", padx=1, pady=5)
tk.Button(master, text="商家爬取", width=8).grid(row=3, column=1, sticky="e", padx=2, pady=2)
tk.Button(master, text="商品爬取", width=8).grid(row=3, column=2, sticky="e", padx=3, pady=5)
tk.Button(master, text="交易数据爬取", width=10).grid(row=3, column=3, sticky="e", padx=4, pady=5)
w.grid(row=4, column=0, columnspan=4, sticky="nesw", padx=0, pady=5)
master.mainloop()
