# -*- coding: utf-8 -*-
import requests
import urllib3
from login import login_headers

urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'

print(urllib3.util.ssl_.DEFAULT_CIPHERS)

""" 据说是刚出来没多久的ja3指纹验证 """

url = 'https://match.yuanrenxue.com/api/match/19'

total = 0
for i in range(1, 6):
    params = {'page': i}
    response = requests.get(url, headers=login_headers, params=params)
    print(response.text)
    data = response.json()["data"]
    for d in data:
        total += d["value"]

answer = total
print(answer)
url = 'https://match.yuanrenxue.com/api/answers'
params = {'answer': answer, 'id': 19}
resq = requests.get(url, headers=login_headers, params=params)
data = resq.json()
print(data)

""" 答案：28073
{"status": "1", "state": "success", "data": [{"value": 3290}, {"value": 912}, {"value": 5440}, {"value": 370}, {"value": 1191}, {"value": -3226}, {"value": 538}, {"value": 1812}, {"value": -253}, {"value": -2534}]}
{"status": "1", "state": "success", "data": [{"value": -3508}, {"value": 3803}, {"value": -952}, {"value": 1659}, {"value": 5705}, {"value": -2745}, {"value": -1933}, {"value": -1684}, {"value": 5757}, {"value": 3725}]}
{"status": "1", "state": "success", "data": [{"value": -874}, {"value": -1648}, {"value": -509}, {"value": -3725}, {"value": 4963}, {"value": -2556}, {"value": -1052}, {"value": 1019}, {"value": 1414}, {"value": 4276}]}
{"status": "1", "state": "success", "data": [{"value": 4303}, {"value": -175}, {"value": 4743}, {"value": -2854}, {"value": -91}, {"value": -3142}, {"value": -644}, {"value": -3536}, {"value": 542}, {"value": -2269}]}
{"status": "1", "state": "success", "data": [{"value": 575}, {"value": -2229}, {"value": -2661}, {"value": 5531}, {"value": -573}, {"value": 3883}, {"value": 5693}, {"value": -1170}, {"value": 2539}, {"value": 933}]}
"""
