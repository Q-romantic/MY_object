# -*- coding: utf-8 -*-
import execjs
import time
import requests
from login import login_headers

""" 抠js代码算法，传指定参数 """

""" 方法二
import js2py

def hex_md5(a):
    def load_js():
        code = js2py.EvalJs()
        with open('index_01.js', 'r', encoding='utf-8') as r:
            code.execute(r.read())
        return code

    code = load_js()
    a = code.hex_md5(a)
    return a
"""


def hex_md5(a):
    index = open('index_01.js', 'r', encoding='utf-8')
    js = execjs.compile(index.read())
    a = js.call('hex_md5', a)
    return a


# url = 'https://match.yuanrenxue.com/api/match/1?page=1&m=d8b29869767aaee44813a083ca30de6c丨1651659321'
url = 'https://match.yuanrenxue.com/api/match/1'

total = 0
times = 0
for i in range(1, 6):
    t = int(time.time()) + 100000
    params = {
        'page': i,
        'm': hex_md5(str(t * 1000)) + '丨' + str(t)
        # ('m', hex_md5(str(t * 1000)) + '\u4E28' + str(t))
    }
    response = requests.get(url, headers=login_headers, params=params)
    print(response.text)
    data = response.json()["data"]
    times += len(data)
    for d in data:
        total += d["value"]

answer = int(total / times)
print(answer)
url = 'https://match.yuanrenxue.com/api/answer'
params = {'answer': answer, 'id': 1}
resq = requests.get(url, headers=login_headers, params=params)
data = resq.json()
print(data)

""" 答案固定：4700
{"status": "1", "state": "success", "data": [{"value": 8179}, {"value": 6177}, {"value": 4174}, {"value": 5945}, {"value": 9556}, {"value": 2318}, {"value": 4}, {"value": 2653}, {"value": 4855}, {"value": 1370}]}
{"status": "1", "state": "success", "data": [{"value": 2366}, {"value": 2108}, {"value": 6159}, {"value": 5685}, {"value": 2010}, {"value": 7109}, {"value": 1002}, {"value": 9300}, {"value": 8995}, {"value": 5732}]}
{"status": "1", "state": "success", "data": [{"value": 5535}, {"value": 7126}, {"value": 7472}, {"value": 4129}, {"value": 2724}, {"value": 3475}, {"value": 3605}, {"value": 7729}, {"value": 1860}, {"value": 833}]}
{"status": "1", "state": "success", "data": [{"value": 3937}, {"value": 6420}, {"value": 115}, {"value": 4333}, {"value": 6674}, {"value": 383}, {"value": 5922}, {"value": 7344}, {"value": 7012}, {"value": 8009}]}
{"status": "1", "state": "success", "data": [{"value": 9297}, {"value": 8727}, {"value": 4130}, {"value": 1910}, {"value": 5976}, {"value": 2973}, {"value": 1756}, {"value": 6725}, {"value": 1716}, {"value": 1456}]}
"""
