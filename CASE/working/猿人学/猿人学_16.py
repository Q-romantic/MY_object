# -*- coding: utf-8 -*-
import requests
from login import login_headers
import time
import execjs

""" 从js代码分析加密参数 """


def btoa(a):
    index = open('index_16.js', 'r', encoding='utf-8')
    js = execjs.compile(index.read())
    a = js.call('get_m_value', a)
    return a


url = 'https://match.yuanrenxue.com/api/match/16'

total = 0
for i in range(1, 6):
    t = str(int(time.time() * 1000))
    params = {
        'page': i,
        'm': btoa(t)[0],
        # 't': btoa(t)[1],
        't': t,
    }
    print(btoa(t))
    response = requests.get(url, headers=login_headers, params=params)
    print(response.text)
    data = response.json()["data"]
    for d in data:
        total += d["value"]

answer = total
print(answer)
url = 'https://match.yuanrenxue.com/api/answers'
params = {'answer': answer, 'id': 16}
resq = requests.get(url, headers=login_headers, params=params)
data = resq.json()
print(data)
