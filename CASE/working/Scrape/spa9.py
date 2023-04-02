# -*- coding: utf-8 -*-
import os
import re
import requests
from subprocess import Popen, PIPE

""" NBA 球星数据网站，数据纯前端渲染，Token 经过加密处理，JavaScript 经过 eval 混淆，适合 JavaScript 逆向分析。 """
""" 提示：没看懂 + 乱码无头绪 """
""" 参考：https://blog.csdn.net/lingyuncelia/article/details/118879583 """

url = 'https://spa9.scrape.center/'
resp = requests.get(url)
resp.encoding = 'utf-8'  # 处理网页中文编码乱码
obj = re.compile('eval\((.*?\{\}\))', re.S)
js_fn = 'fn=' + obj.findall(resp.text)[0] + ';console.log(fn);'
# print(js_fn)
with open('tmp.js', mode='w') as f:
    f.write(js_fn)
out = Popen(['node', 'tmp.js'], stdout=PIPE).stdout.read().decode()
os.remove('tmp.js')
obj = re.compile('\[.*?\]', re.S)
data1 = obj.findall(out)[0] \
    .replace('name', '"name"') \
    .replace('image', '"image"') \
    .replace('birthday', '"birthday"') \
    .replace('height', '"height"') \
    .replace('weight', '"weight"')
# for i in eval(data1):  # 中文有乱码
#     print(i)

# 如下方法获取数据不完整，有数据替换映射关系
url = 'https://spa9.scrape.center/'
resp = requests.get(url)
resp.encoding = 'utf-8'  # 处理网页中文编码乱码
obj = re.compile('h=(\[.*?\])', re.S)
data2 = obj.findall(resp.text)[0].replace('\\', '')
# for i in eval(data2):  # 数据不完整
#     print(i)

for i, j in zip(eval(data1), eval(data2)):  # 巧妙二合一
    i['name'] = j[0]
    print(i)
    # break
