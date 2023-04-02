# -*- coding: utf-8 -*-
import re
import requests

""" NBA 球星数据网站，数据纯前端渲染，Token 经过加密处理，适合基础 JavaScript 模拟分析。 """
""" 提示：没看懂 """

url = 'https://spa7.scrape.center/js/main.js'
resp = requests.get(url)
obj = re.compile('\[.*?\]', re.S)
data = obj.findall(resp.text)[0] \
    .replace('name', '"name"') \
    .replace('image', '"image"') \
    .replace('birthday', '"birthday"') \
    .replace('height', '"height"') \
    .replace('weight', '"weight"')
for i in eval(data):
    print(i)
