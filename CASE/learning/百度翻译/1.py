# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/18  018 下午 23:07
@Author  : Jan
@File    : 1.py
"""
import tkinter as tk

""" {} """

root = tk.Tk()
root.title('翻译')
root.geometry("500x300+500+250")
text_1 = tk.Text(root, width=50, height=5)
text_1.pack()


def get_text():
    t = text_1.get(1.0, tk.END)
    # print(t)
    return t


def get_response(datas):
    pass
    return datas


def main():
    t = get_text()
    res = f"get_response({t})"
    text_2.delete(0.0, tk.END)
    text_2.insert(tk.INSERT, res)


btnRead = tk.Button(root, height=1, width=10, text="翻译", command=main)
btnRead.pack()
text_2 = tk.Text(root, width=50, height=10)
text_2.pack()
root.mainloop()
