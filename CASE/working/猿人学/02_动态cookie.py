# -*- coding: utf-8 -*-
import requests
import execjs
from login import login_headers

""" 从js代码加载获取动态cookie，不分页面，区别于03、13题 """

url = 'https://match.yuanrenxue.com/api/match/2'


# 如下获取js代码需要进一步分析，已混淆
# response = requests.get(url)
# print(response.text)
# with open('index_02.js', 'wb') as f:
#     f.write(response.content[8:-9])


def get_cookie():  # 方法一
    index = open('index_02.js', 'r', encoding='utf-8')
    a = execjs.eval(index.read())
    return a


# def get_cookie():  # 方法二
#     with open('index_02.js', 'r') as f:
#         data = f.read()
#     a = execjs.eval(data)
#     return a


cookie = get_cookie()
print(cookie)
headers = {'User-Agent': 'yuanrenxue.project', 'cookie': cookie}

total = 0
for i in range(1, 6):
    params = {'page': i}
    response = requests.get(url, headers=headers, params=params)
    print(response.text)
    data = response.json()["data"]
    for d in data:
        total += d["value"]

print(total)
url = 'https://match.yuanrenxue.com/api/answer'
params = {'answer': total, 'id': 2}
resq = requests.get(url, headers=login_headers, params=params)
data = resq.json()
print(data)

""" 答案固定：248974
{"status": "1", "state": "success", "data": [{"value": 3592}, {"value": 1829}, {"value": 3753}, {"value": 5054}, {"value": 9894}, {"value": 1037}, {"value": 7581}, {"value": 5257}, {"value": 8218}, {"value": 5244}]}
{"status": "1", "state": "success", "data": [{"value": 5993}, {"value": 9462}, {"value": 4820}, {"value": 7555}, {"value": 1805}, {"value": 445}, {"value": 3457}, {"value": 6417}, {"value": 6855}, {"value": 6841}]}
{"status": "1", "state": "success", "data": [{"value": 8814}, {"value": 4889}, {"value": 6821}, {"value": 3063}, {"value": 1475}, {"value": 8797}, {"value": 2370}, {"value": 1989}, {"value": 3685}, {"value": 7603}]}
{"status": "1", "state": "success", "data": [{"value": 801}, {"value": 9557}, {"value": 7947}, {"value": 3847}, {"value": 3336}, {"value": 4237}, {"value": 4589}, {"value": 2477}, {"value": 5316}, {"value": 787}]}
{"status": "1", "state": "success", "data": [{"value": 7642}, {"value": 5199}, {"value": 4247}, {"value": 4604}, {"value": 3344}, {"value": 9769}, {"value": 6655}, {"value": 1263}, {"value": 3209}, {"value": 5533}]}
"""
