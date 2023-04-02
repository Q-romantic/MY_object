# -*- coding: utf-8 -*-
"""
@Time    : 2023/2/7  007 下午 18:26
@Author  : Jan
@File    : 机票信息查询.py
"""
import pprint
import execjs
import requests

""" {https://www.airasia.cn/select/en/gb/HKT/BKK/2024-02-04/N/1/0/0/O/N/CNY/ST} """


def get_authorization(t):
    index = open('2.js', 'r', encoding='utf-8')
    js = execjs.compile(index.read())
    a = js.call('get_authorization', t)
    return a


def get_data(authorization):
    headers = {"authorization": authorization}
    url = 'https://k.airasia.cn/shopprice-n/api/v4/pricesearch/0/1/HKT/BKK/2024-02-04/1/0/0'
    response = requests.get(url, headers=headers)
    data = response.json()
    pprint.pprint(data)


headers = {"channel_hash": "98ba1fad5baab2959fd06259acc292c6ebf46e210735882afc32a084"}
url = 'https://k.airasia.cn/ssr/v2/getssrdata'
response = requests.post(url, headers=headers)
data_t = response.json()
authorization = get_authorization(data_t)
print(authorization)
get_data(authorization['search'])
