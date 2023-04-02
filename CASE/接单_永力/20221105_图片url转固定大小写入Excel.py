# -*- coding: utf-8 -*-
"""
@Time    : 2022/11/5  005 下午 14:55
@Author  : Jan
@File    : 20221105_图片url转固定大小写入Excel.py
"""

""" {} """

import glob
import os
import cv2
import requests
import numpy as np
import xlsxwriter

try:
    for i in glob.glob("*.jpg"):
        os.remove(i)
except:
    pass

try:
    os.remove("pic.xlsx")
except:
    pass

li = [
    "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.zjol.com.cn%2Fpic%2F0%2F04%2F76%2F59%2F4765988_953137.jpg&refer=http%3A%2F%2Fimg.zjol.com.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1622370200&t=57fb279892d0cbc60046d2035ef275ac",
    "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.zcool.cn%2Fcommunity%2F010f4457d7be150000018c1b6d538b.png%401280w_1l_2o_100sh.png&refer=http%3A%2F%2Fimg.zcool.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1622370232&t=df22abbb4cad820eeee1701e25f10e8f",
    "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fpic.16xx8.com%2Fallimg%2F180514%2F16xx8-78871-1.thumb.png&refer=http%3A%2F%2Fpic.16xx8.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1622370249&t=3260a132d8817f5361714796e1aa75d2"
]


def get_jpg_small(url, name):
    response = requests.get(url)
    data = response.content
    # print(data)
    # print(response)
    data = np.asarray(bytearray(data), dtype="uint8")
    img = cv2.imdecode(data, cv2.IMREAD_COLOR)

    def changeImgSize(img, *args, **kwargs):
        times = kwargs.get('times')  # times = 0.25  # 图片放大倍数
        size = kwargs.get('size')  # size = (155, 125)  # 注意排序是反的，上下二选一
        y, x = img.shape[0:2]  # 高，宽
        if times:
            size = (int(y * times), int(x * times))  # 注意排序是反的
        img = cv2.resize(img, size)
        return img, x, y

    # img, x, y = changeImg(img, times=0.25)    # 缩小图
    # img, x, y = changeImg(img, times=1)   # 原图
    img, x, y = changeImgSize(img, size=(700, 560))  # 固定大小
    path = f'{name}.jpg'
    cv2.imwrite(path, img)
    return path, x, y


# 定义一下写入的Excel和worksheet的名
book = xlsxwriter.Workbook(r"pic.xlsx")
sheet = book.add_worksheet("pic")
my_format = book.add_format({
    'bold': True,  # 字体加粗
    'align': 'center',  # 水平位置设置：居中
    'valign': 'vcenter',  # 垂直位置设置，居中
    'font_size': 12,  # 字体大小设置
    'underline': True,  # 下划线
})
my_format2 = book.add_format({
    'align': 'fill',  # 水平位置设置：填充
    'valign': 'vcenter',  # 垂直位置设置，居中
    'font_color': 'blue',  # 字体颜色
    'underline': True,  # 下换线
})
sheet.set_column("B:B", 40)  # 设置单元格列宽
sheet.write("A1", "name", my_format)
sheet.write("B1", "url", my_format)
sheet.write("C1", "jpg", my_format)
for i in range(1, len(li) + 1):
    sheet.set_row(i, 50)
    sheet.write(f"A{i + 1}", f"apple{i + 1}", my_format)
    sheet.write_url(f"B{i + 1}", li[i - 1], tip='Click here', cell_format=my_format2)
    path, x, y = get_jpg_small(li[i - 1], i)
    # sheet.insert_image(f"C{i + 1}", path, {"x_scale": 0.45, "y_scale": 0.55, "x_offset": 5, "y_offset": 5})
    sheet.insert_image(f"C{i + 1}", path, {"x_scale": round(58 / x, 4), "y_scale": round(58 / y, 4), "x_offset": 4, "y_offset": 4})
book.close()
for i in glob.glob("*.jpg"):
    os.remove(i)
