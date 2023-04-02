# -*- coding: utf-8 -*-
import requests
from login import login_headers

""" ? """

a = {"status": "1", "state": "success",
     "data": [{"value": 7175}, {"value": 6135}, {"value": 1244}, {"value": 4419}, {"value": 8053}, {"value": 3509},
              {"value": 1571}, {"value": 1744}, {"value": 6825}, {"value": 8924}]}
b = {"status": "1", "state": "success",
     "data": [{"value": 6580}, {"value": 4161}, {"value": 4642}, {"value": 8679}, {"value": 9897}, {"value": 9703},
              {"value": 2608}, {"value": 4306}, {"value": 3764}, {"value": 8781}]}
c = {"status": "1", "state": "success",
     "data": [{"value": 8616}, {"value": 9281}, {"value": 4560}, {"value": 8019}, {"value": 2863}, {"value": 8817},
              {"value": 4347}, {"value": 1654}, {"value": 4294}, {"value": 4708}]}
d = {"status": "1", "state": "success",
     "data": [{"value": 897}, {"value": 2104}, {"value": 6344}, {"value": 470}, {"value": 1795}, {"value": 9387},
              {"value": 929}, {"value": 3357}, {"value": 2335}, {"value": 5244}]}
e = {"status": "1", "state": "success",
     "data": [{"value": 4603}, {"value": 8619}, {"value": 2315}, {"value": 2331}, {"value": 11}, {"value": 9469},
              {"value": 3932}, {"value": 7862}, {"value": 570}, {"value": 2547}]}
li = []
for i in a["data"]:
    li.append(i['value'])
for i in b["data"]:
    li.append(i['value'])
for i in c["data"]:
    li.append(i['value'])
for i in d["data"]:
    li.append(i['value'])
for i in e["data"]:
    li.append(i['value'])

print(li)
answer = int(sum(li) / len(li))
print(answer)
url = 'https://match.yuanrenxue.com/api/answer'
params = {'answer': answer, 'id': 9}
resq = requests.get(url, headers=login_headers, params=params)
data = resq.json()
print(data)

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
