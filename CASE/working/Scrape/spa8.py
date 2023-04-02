# -*- coding: utf-8 -*-
import re
import requests

""" NBA 球星数据网站，数据纯前端渲染，Token 经过加密处理，JavaScript 代码一行混入 HTML 代码，防止直接调试，适合 JavaScript 逆向分析。 """
""" 提示：没看懂 """

url = 'https://spa8.scrape.center/'
resp = requests.get(url)
resp.encoding = 'utf-8'  # 处理网页中文编码乱码
obj = re.compile('\[.*?\]', re.S)
data = obj.findall(resp.text)[0] \
    .replace('name', '"name"') \
    .replace('image', '"image"') \
    .replace('birthday', '"birthday"') \
    .replace('height', '"height"') \
    .replace('weight', '"weight"')
for i in eval(data):
    print(i)
