# -*- coding: utf-8 -*-
"""
@Time    : 2022/11/14  014 下午 12:36
@Author  : Jan
@File    : main.py
"""

import json
import requests
import pprint
from login import login_headers

""" {采用JsRpc，省去抠代码补环境，只需先开启win64-localhost.exe，然后将index_20.js代码注入控制台} """

data_list = []


def get_params(page):
    url = "http://localhost:12080/go"
    params = {
        'group': 'group',  # 可不需要需要修改，但要和控制台注入js代码保持一致
        'name': 'name',  # 可不需要需要修改，但要和控制台注入js代码保持一致
        'action': 'func_1',
        "param": page
        # "param": json.dumps({"param1": "1", "param2": "2"})  # 多个参数传入参考
    }
    resp = requests.get(url, params=params).json()
    data = json.loads(resp['data'])
    page = data['page']
    sign = data['sign']
    t = data['t']
    url = f'https://match.yuanrenxue.com/api/match/20?page={page}&sign={sign}&t={t}'
    resp = requests.get(url, headers=login_headers).json()
    data = resp["data"]
    print(data)
    for d in data:
        data_list.append(d["value"])


for i in range(1, 6):
    get_params(i)
# print(data_list)
answer = sum(data_list)
print(answer)
url = 'https://match.yuanrenxue.com/api/answer'
params = {'answer': answer, 'id': 20}
resq = requests.get(url, headers=login_headers, params=params)
data = resq.json()
print(data)
