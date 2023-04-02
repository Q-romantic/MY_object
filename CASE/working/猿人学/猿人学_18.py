# -*- coding: utf-8 -*-
import os
import execjs
import requests
import re
import subprocess
import time
from login import login_cookies
from login import login_headers

""" ? """


def get_v(t, page):
    index = open('index_18.js', 'r', encoding='utf-8')
    js = execjs.compile(index.read())
    a = js.call('get_v', t, page)
    return a


total = 0
for page in range(1, 6):
    url = 'https://match.yuanrenxue.com/match/18data?page=' + str(page)
    t = int(time.time())
    params = {
        'page': page,
        't': t,
        'v': get_v(t, page),
    }
    response = requests.get(url, cookies=login_cookies, headers={'User-Agent': 'yuanrenxue.project'}, params=params)
    print(response.text)
    data = response.json()["data"]
    for d in data:
        total += d["value"]
    # break

answer = total
print(answer)
url = 'https://match.yuanrenxue.com/api/answers'
params = {'answer': answer, 'id': 18}
resq = requests.get(url, headers=login_headers, params=params)
data = resq.json()
print(data)

"""答案：64829
{"status": "1", "state": "success", "data": [{"value": 4838}, {"value": 458}, {"value": 3093}, {"value": 4305}, {"value": -2295}, {"value": -2048}, {"value": -3975}, {"value": -708}, {"value": -3991}, {"value": -287}]}
{"status": "1", "state": "success", "data": [{"value": 1077}, {"value": 3873}, {"value": 1801}, {"value": 1783}, {"value": 3426}, {"value": 969}, {"value": -143}, {"value": 5129}, {"value": 295}, {"value": -1955}]}
{"status": "1", "state": "success", "data": [{"value": 1930}, {"value": 4369}, {"value": 4370}, {"value": 5548}, {"value": -1504}, {"value": 5674}, {"value": -554}, {"value": 4832}, {"value": 4086}, {"value": -3756}]}
{"status": "1", "state": "success", "data": [{"value": 5839}, {"value": 3139}, {"value": 2201}, {"value": -1256}, {"value": 3949}, {"value": -2260}, {"value": -708}, {"value": 2122}, {"value": -1800}, {"value": -2103}]}
{"status": "1", "state": "success", "data": [{"value": 4041}, {"value": -3886}, {"value": -1597}, {"value": 4973}, {"value": -1735}, {"value": 2699}, {"value": 2166}, {"value": 1657}, {"value": 3388}, {"value": 3360}]}
"""
