# -*- coding: utf-8 -*-
"""
@Time    : 2023/2/22  022 上午 1:23
@Author  : Jan
@File    : 字体xml文件解读.py
"""

""" {} """

import requests
from fontTools.ttLib import TTFont
from io import BytesIO

# font = TTFont('1.woff')

url = 'https://j1.58cdn.com.cn/escstatic/webfonts/don58/don58medium.ttf'
response = requests.get(url, headers={}, params={}, data={})
font = TTFont(BytesIO(response.content))

# font.saveXML('2.xml')


# 各节点名称
print(font.keys())

# 按序获取 GlyphOrder 节点 name 值
print(font.getGlyphOrder())
print(font.glyphOrder)
print(font.getGlyphNames())
print(font.getGlyphNames2())

# 获取cmap节点code与name值映射
print(font.getBestCmap())

# 获取字体坐标信息，注意取值 [5:]，可能会有多个无轮廓字体
[print(font['glyf'][i].coordinates) for i in font.getGlyphNames()[5:]]

# 获取坐标的 0 或 1，注：0 表示弧形区域 1 表示矩形
[print(font['glyf'][i].flags) for i in font.getGlyphNames()[5:]]
