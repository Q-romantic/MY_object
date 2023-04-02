# -*- coding: utf-8 -*-

import requests
import execjs
from login import login_headers

""" ?下回再分析，累了 """

li = [9877, 9806, 9625, 9368, 8637]
answer = sum(li)
print(answer)
url = 'https://match.yuanrenxue.com/api/answer'
params = {'answer': answer, 'id': 5}
resq = requests.get(url, headers=login_headers, params=params)
data = resq.json()
print(data)

"""答案固定：47313
排前五：
[9877, 9806, 9625, 9368, 8637]
"""

# import time
#
# print('m', str(int(time.time() * 1000 + 1000)))
# print('m', str(int(time.time() * 1000 + 1000))[:-1])
# print('f', str(int(time.time())) + '000')
#
#
# def result():
#     index = open('index_05.js', 'r', encoding='utf-8')
#     js = execjs.compile(index.read())
#     a = js.call('result')
#     return a
#
#
# print(result())
#
#
# # print(result(165172938700))
# # print(result(165172938829))
# # print(result(160394288630))
#
# def result2(a):
#     index = open('index_00.猿人学', 'r', encoding='utf-8')
#     js = execjs.compile(index.read())
#     a = js.call('b', a)
#     return a
#
#
# print(result2(165172938700))
# print(result2(165172938829))
# print(result2(160394288630))
# # aa6b3eb2cfbe980b1e1f5bd2c5555008
# # print(result('1651729387000'))
# # print(result('1651729388297'))
# # print(result('1603942886303'))
#
# url = 'https://match.yuanrenxue.com/api/match/5'
#
# # total = 0
# # for i in range(1, 6):
# #     params = {
# #         'page': i,
# #         'm': m,
# #         'f': result()[0],
# #     }
# #     response = requests.get(url, headers=headers, params=params)
# #     print(response.text)
# #     # data = response.json()["data"]
# #     # for d in data:
# #     #     total += d["value"]
# #
# # print(total)
