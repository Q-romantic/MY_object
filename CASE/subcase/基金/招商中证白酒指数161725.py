# -*- coding: utf-8 -*-
"""
@Time    : 2022/7/3  003 上午 11:00
@Author  : Jan
@File    : 招商中证白酒指数161725.py
"""

import requests

from matplotlib import font_manager
import numpy as np
import matplotlib.pyplot as plt
from working.all_tools.tools import getip
from working.all_tools.tools import getua

""" {} """

headers = {
    "User-Agent": getua(),

}
proxies = {
    'http': 'http://' + getip(),
    # 'https': 'https://' + getip(),
}

code_num = 161725
# code_num = '012757'
# code_num = '161121'

url = f'https://danjuanapp.com/djapi/fund/nav/history/{str(code_num)}?page=1&size=1'
response = requests.get(url, headers=headers, params={}, data={}, proxies=proxies)
data = response.json()
# print(data)
# print(response)
total_items = data["data"]["total_items"]
# total_items = 31    # 可指定最近数据条数
url = f'https://danjuanapp.com/djapi/fund/nav/history/{str(code_num)}?page=1&size={total_items}'
response = requests.get(url, headers=headers, params={}, data={}, proxies=proxies)
data = response.json()
# print(data)
# print(response)
items = data['data']['items']
x = []
y = []
y1 = []
for item in items[::-1]:
    date = item['date']
    try:
        percentage = item['percentage']
    except:
        percentage = "0.0"
    value = item['value']
    x.append(date)
    y.append(float(value))
    y1.append(float(percentage))
    # print("date=" + str(date) + ",percentage=" + str(percentage) + ",value=" + str(value))


### 1.日走势曲线图
def analysis1(x, y):
    myfont = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\simhei.ttf")

    y_up = []
    y_down = []
    for i in y:
        if i >= 1:
            y_up.append(i)
            y_down.append(1)
        else:
            y_down.append(i)
            y_up.append(1)


    # 设置图形大小
    plt.figure(figsize=(20, 8), dpi=80)
    plt.xticks(np.arange(0, len(x), 1 + (len(x) - 6) / 5))  # 设置整体显示第一个和最后一个共6个日期
    plt.plot(x, y_up, label="净值涨")
    plt.plot(x, y_down, label="净值跌")

    # 设置图例
    plt.legend(prop=myfont)
    plt.xlabel("日期", fontproperties=myfont)
    plt.ylabel("值/天", fontproperties=myfont)
    # plt.savefig("./mutiy.png")
    plt.show()


### 2.当日涨、跌百分比
def analysis2(x, y1):
    myfont = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\simhei.ttf")
    y1_up = []
    y1_down = []
    for i in y1:
        if i >= 0:
            y1_up.append(i)
            y1_down.append(0)
        else:
            y1_down.append(i)
            y1_up.append(0)

    bar_width = 0.25

    # 设置图形大小
    plt.figure(figsize=(20, 8), dpi=80)
    # 设置x轴刻度
    plt.xticks(np.arange(0, len(x), 1 + (len(x) - 6) / 5))  # 设置整体显示第一个和最后一个共6个日期
    plt.bar(x, y1_up, width=bar_width, label="当日最高涨")
    plt.bar(x, y1_down, width=bar_width, label="当日最低跌")

    # 设置图例
    plt.legend(prop=myfont)
    plt.xlabel("日期", fontproperties=myfont)
    plt.ylabel("值/天", fontproperties=myfont)

    # plt.savefig("./mutiy.png")
    plt.show()


def merge_month(x, y):  # 压缩日期按月整合
    x_month = []
    y_month = []
    tmp = {}
    for s, d in zip(x, y):
        k, v = s.rsplit("-", 1)
        if k not in x_month:
            x_month.append(k)
            tmp[k] = [d]
        else:
            tmp[k].append(d)
    for i in tmp:
        # print(tmp)
        y_month.append(sum(tmp[i])/len(tmp[i]))
    return x_month, y_month


def merge_year(x, y):  # 压缩日期按年整合
    x_year = []
    y_year = []
    tmp = {}
    for s, d in zip(x, y):
        k, v, r = s.split("-")
        if k not in x_year:
            x_year.append(k)
            tmp[k] = [d]
        else:
            tmp[k].append(d)
    for i in tmp:
        y_year.append(sum(tmp[i])/len(tmp[i]))
    return x_year, y_year

analysis1(x, y)
analysis2(x, y1)

x_month, y_month = merge_month(x, y)
analysis1(x_month, y_month)
x_month, y_month = merge_month(x, y1)
analysis2(x_month, y_month)

x_year, y_year = merge_year(x, y)
analysis1(x_year, y_year)
x_year, y_year = merge_year(x, y1)
analysis2(x_year, y_year)
