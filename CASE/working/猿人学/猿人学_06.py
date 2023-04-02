# -*- coding: utf-8 -*-
import requests
from login import login_headers
import execjs
import time

""" 抠整个js代码稍加修改，其中 q 参数有干扰，实际未累对其加使用 """


def get_m(time, page):
    index = open('index_06.js', 'r', encoding='utf-8')
    js = execjs.compile(index.read())
    a = js.call('z', time, page)
    return a


url = 'https://match.yuanrenxue.com/api/match/6'
url1 = 'https://match.yuanrenxue.com/match/6'

# resp = requests.get(url1)
# print(resp.text)

total = 0
for i in range(1, 6):
    t = int(time.time()) * 1000
    q = f'{i}-{t}|'
    params = {
        'page': i,
        'm': get_m(t, i),
        'q': q,
    }
    response = requests.get(url, headers=login_headers, params=params)
    print(response.text)
    data = response.json()["data"]
    for d in data:
        total += d["value"]

answer = total * 24
print(answer)

url = 'https://match.yuanrenxue.com/api/answer'
params = {'answer': answer, 'id': 6}
resq = requests.get(url, headers=login_headers, params=params)
data = resq.json()
print(data)
