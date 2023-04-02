# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/15  015 下午 14:38
@Author  : Jan
@File    : 猿人学_05_v2.py
"""
import requests
import execjs
from login import login_headers_no_cookies
from login import login_headers

""" {} """


def encrypt_yrx5():
    room_heat_all = []
    with open('index_05_v2.js', 'r', encoding='utf-8') as f:
        encrypt = f.read()
    for page_num in range(1, 6):
        encrypt_params = execjs.compile(encrypt).call('getParamers')
        cookies = {
            "m": encrypt_params['cookie_m'],
            "RM4hZBv0dDon443M": encrypt_params['cookie_rm4']
        }
        params = {
            "m": encrypt_params['m'],
            "f": encrypt_params['f']
        }
        url = "https://match.yuanrenxue.com/api/match/5?page=%s" % page_num
        response = requests.get(url, headers=login_headers_no_cookies, cookies=cookies, params=params)
        for data in response.json()['data']:
            value = data['value']
            room_heat_all.append(value)
    room_heat_all.sort(reverse=True)
    return room_heat_all


li = encrypt_yrx5()
print(li)
answer = sum(li[:5])
print(answer)
url = 'https://match.yuanrenxue.com/api/answer'
params = {'answer': answer, 'id': 5}
resq = requests.get(url, headers=login_headers, params=params)
data = resq.json()
print(data)
