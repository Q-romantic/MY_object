# -*- coding: utf-8 -*-
import re
import requests
from login import login_headers

""" 动态cookie，每刷新一次变，区别于02、03题 """
""" 第二次请求加上第一次请求获得的cookie """

session = requests.Session()

url = 'https://match.yuanrenxue.com/match/13'
url2 = 'https://match.yuanrenxue.com/api/match/13'

r = session.get(url, headers=login_headers)
obj = re.compile("'([a-zA-Z0-9=|_])'")
results = obj.findall(r.text)
print(r.text)
cookie = ''.join(results)
key, value = cookie.split('=')
session.cookies.set(key, value)
cookies = session.cookies.get_dict()
print(cookies)

total = 0
for i in range(1, 6):
    headers2 = {'User-Agent': 'yuanrenxue.project'}
    params = {'page': i}
    response = requests.get(url2, headers=headers2, cookies=cookies, params=params)
    # print(session.cookies.get_dict())
    print(response.text)
    data = response.json()["data"]
    for d in data:
        total += d["value"]

answer = total
print(answer)
url = 'https://match.yuanrenxue.com/api/answers'
params = {'answer': answer, 'id': 13}
resq = requests.get(url, headers=login_headers, params=params)
data = resq.json()
print(data)

""" 答案固定：7833
"""
