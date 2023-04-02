# -*- coding: utf-8 -*-
import os
import re
import requests
from subprocess import Popen, PIPE

""" NBA 球星数据网站，数据纯前端渲染，Token 经过加密处理，JavaScript 经过 eval 混淆，适合 JavaScript 逆向分析。 """
""" 提示：
10、jjEncode混淆：去掉最后一对括号()，放在console内运行，得到jjEncode混淆后的结果
11、AAEncode混淆：去掉最后一对括号('_')，放在console内运行，得到jAAEncode混淆后的结果
12、JSFuck混淆：最后一个右括号下的横线，找寻前面相对应的左括号由第一行开始往下找，将括号内的东东copy，放在console内运行，得到JSFuck混淆后的结果
13、JavaScript Obfuscator混淆：Obfuscator混淆？？？
"""
""" 参考：https://blog.csdn.net/lingyuncelia/article/details/119521528 """
""" 参考：https://blog.csdn.net/lingyuncelia/article/details/118879555 """

for spa in [10, 11, 12, 13]:
# for spa in [13]:
    url = f'https://spa{spa}.scrape.center/js/main.js'
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    # print(resp.text)
    with open('tmp.js', mode='wb') as f:
        f.write(resp.content)
    p = Popen(['node', 'tmp.js'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    os.remove('tmp.js')
    # print(out)
    # print(err.decode())
    obj = re.compile('(\[.*?\])', re.S)
    data2 = obj.findall(err.decode())[0] \
        .replace('name', '"name"') \
        .replace('image', '"image"') \
        .replace('birthday', '"birthday"') \
        .replace('height', '"height"') \
        .replace('weight', '"weight"')
    # print(data2)
    for i in eval(data2):
        print(i)
    print(f'---spa{spa}---'*15)
