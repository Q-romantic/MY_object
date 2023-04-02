# -*- coding: utf-8 -*-
import re
import os
import base64
import requests
from login import login_headers
from fontTools.ttLib import TTFont
from io import BytesIO

""" 动态字体，woff字体转xml，利用High-Logic FontCreator工具分析变与不变的对应关系 """

link_dic = {
    '100110101001010101011110101000': 2,
    '1110101001001010110101010100101011111': 5,
    '101010101101010001010101101010101010010010010101001000010': 8,
    '111111111111111': 4,
    '1001101111': 1,
    '10100100100101010010010010': 0,
    '1111111': 7,
    '10101010100001010111010101101010010101000': 6,
    '10101100101000111100010101011010100101010100': 3,
    '10010101001110101011010101010101000100100': 9,
}

url1 = 'https://match.yuanrenxue.com/match/7'
url2 = 'https://match.yuanrenxue.com/api/match/7'

resp = requests.get(url1)
resp.encoding = 'utf-8'
obj = re.compile('let name=(?P<names>.*?);', re.S)
names = obj.search(resp.text).group('names')
li = eval(names)
# print(li)
print(li[1:51])
print('---' * 30)

# for i in range(1, 6):
#     l = []
#     for j in range(1, 11):
#         (i == 1) and l.append(li[(i - 1) * 10 + j])
#         (i == 2) and l.append(li[(i - 1) * 10 + j])
#         (i == 3) and l.append(li[(i - 1) * 10 + j])
#         (i == 4) and l.append(li[(i - 1) * 10 + j])
#         (i == 5) and l.append(li[(i - 1) * 10 + j])
#     print(l)
# print('---' * 30)

total = []
woff_dic = {}
for i in range(1, 6):
    params = {'page': i}
    response = requests.get(url2, headers=login_headers, params=params)
    # print(response.text)
    data = response.json()['data']
    woff = response.json()['woff']
    # with open(f'7-{i}.woff', 'wb') as f:
    #     f.write(base64.b64decode(woff))
    # font = TTFont(f'7-{i}.woff')
    # font.saveXML(f'7-{i}.xml')
    byte_woff = base64.b64decode(woff)
    font = TTFont(BytesIO(byte_woff))
    font.saveXML(f'7-{i}.xml')
    with open(f'7-{i}.xml', 'r') as f:
        txt = f.read()
        obj1 = re.compile('(<TTGlyph.*?</TTGlyph>)', re.S)
        obj2 = re.compile('name="(?P<name>.*?)"', re.S)
        obj3 = re.compile('on="(.*?)"/>', re.S)
        woff_dic[f'p_{i}'] = {}
        for num in obj1.findall(txt):
            name = obj2.search(num).group('name')
            x = obj3.findall(num)
            # print(name, ''.join(x))
            woff_dic[f'p_{i}'][name] = ''.join(x)

    for value in data:
        s = value['value'].replace('&#x', 'uni').strip()
        s1 = ''
        for ss in s.split(' '):
            s1 += str(link_dic[woff_dic[f'p_{i}'][ss]])
        total.append(int(s1))
    # os.remove(f'7-{i}.woff')
    os.remove(f'7-{i}.xml')
print(total)
print('---' * 30)

for i, j in zip(total, li[1:51]):
    if i == max(total):
        answer = j
        print(i, answer)
        url = 'https://match.yuanrenxue.com/api/answer'
        params = {'answer': answer, 'id': 7}
        resq = requests.get(url, headers=login_headers, params=params)
        data = resq.json()
        print(data)
        break

"""答案固定：冷视天下
[3236, 5041, 3958, 8550, 7037, 8898, 2190, 8400, 4500, 7478, 
2342, 1926, 5826, 2827, 369, 4384, 2934, 5468, 9107, 2132, 
5553, 687, 5688, 6179, 7722, 35, 6301, 9221, 6534, 9711, 
6995, 3705, 5413, 2333, 5660, 7142, 8826, 9291, 5778, 2920, 
5983, 9015, 1533, 4337, 746, 4349, 4229, 4928, 2830, 1206]
"""