# -*- coding: utf-8 -*-
import requests
from login import login_headers

""" ? """

a = {"status": "1", "state": "success",
     "data": [{"value": 304}, {"value": 2207}, {"value": 6182}, {"value": 1548}, {"value": 22}, {"value": 1115},
              {"value": 5666}, {"value": 2970}, {"value": 7077}, {"value": 2068}], "k": {"k": "CABe|1006"}}

b = {"status": "1", "state": "success",
     "data": [{"value": 5928}, {"value": 6210}, {"value": 1670}, {"value": 8328}, {"value": 3227}, {"value": 5868},
              {"value": 5019}, {"value": 9421}, {"value": 469}, {"value": 1153}], "k": {"k": "CABe|1324"}}

c = {"status": "1", "state": "success",
     "data": [{"value": 6184}, {"value": 9462}, {"value": 7467}, {"value": 9555}, {"value": 6369}, {"value": 6293},
              {"value": 562}, {"value": 1905}, {"value": 5833}, {"value": 1164}], "k": {"k": "CABe|207"}}

li = [1770, 2055, 6957, 9495, 369, 6264, 2114, 4148, 3133, 7612, 3929, 3628, 4423, 9256, 675, 451, 8930, 6445, 5705,
      3314]
for i in a["data"]:
    li.append(i['value'])
for i in b["data"]:
    li.append(i['value'])
for i in c["data"]:
    li.append(i['value'])

answer = sum(li)
print(answer)
url = 'https://match.yuanrenxue.com/api/answer'
params = {'answer': answer, 'id': 10}
resq = requests.get(url, headers=login_headers, params=params)
data = resq.json()
print(data)

url = 'https://match.yuanrenxue.com/api/match/10'

# total = 0
# for i in range(1, 6):
#     params = {
#         'page': i,
#     }
#     response = requests.get(url, headers=headers, params=params)
#     print(response.text)
#     data = response.json()["data"]
#     for d in data:
#         total += d["value"]
#
# print(total)
