# -*- coding: utf-8 -*-
import requests
from login import login_headers

""" 模拟器安装HttpCanary，手机抓包大师，最强Android抓包工具 """

total = []


def get_data():
    url = 'https://match.yuanrenxue.com/api/match/11/query'
    # for i in range(0, 100):
    for i in range(0, 100):
        headers = {
            # 'User-Agent': 'okhttp/3.7.0',
            # 'Host': 'match.yuanrenxue.com'
        }
        params = {
            'id': i,
            # 'sign': 'hI#PG4mfdwX2koPJkJPl54Cu7imf7b#P60yIkOZyk2NJk+P65JFn4lyahoEJolN26wZFQ+XSDeylo+uJ6OyA6OyJy7yrkw3yoWYZQwZIieN55oXJ',   # 虽然每次请求都有变化，但可以固定
            'sign': 'jICB7ECfdwX2koPJkJPl54Cu7imf7iCupoP2k+YRk6WaQwyn42wIh0NlkHNTjwYukWNZ5rET4JNrkw3PiwN2k0W2kwy652uR46WP66yV5+y9kJ2JoYv=',
        }
        response = requests.post(url, params=params)
        print(f'query={i}', response.text)
        data = response.json()["data"]
        total.append(data)
        # break


# get_data()    # 查询内容多，跳过，直接提交答案
# print(total)
# answer = sum(total)
answer = 483974
print(answer)
url = 'https://match.yuanrenxue.com/api/answer'
params = {'answer': answer, 'id': 11}
resq = requests.get(url, headers=login_headers, params=params)
data = resq.json()
print(data)

""" 答案固定：483974
"""
