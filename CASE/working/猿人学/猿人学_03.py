# -*- coding: utf-8 -*-
import re
import requests
from login import login_headers

""" 每页重新请求另外一个网页获取加密cookie，区别于02、13题 """

url = 'https://match.yuanrenxue.com/match/3'
url_jssm = "https://match.yuanrenxue.com/jssm"
url2 = 'https://match.yuanrenxue.com/api/match/3'

resp = requests.get(url)
resp.encoding = 'utf-8'
obj = re.compile('let name=(?P<name>.*?);data=', re.S)
names = obj.search(resp.text).group('name').replace('];let com_name=[', ',')
li = eval(names)
# print(li)

for i in range(1, 6):
    l = []
    for j in range(1, 11):
        (i == 1) and l.append(li[j * 1])
        (i == 2) and l.append(li[j * 2])
        (i == 3) and l.append(li[j * 3])
        (i == 4) and l.append(li[j * 4])
        (i == 5) and l.append(li[j * 5])
    print(l)
print('---' * 30)

data_list = []
for i in range(1, 6):
    headers = {
        'Content-Length': '0',
        'Accept': '*/*',
        'Referer': 'http://match.yuanrenxue.com/match/3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    cookies = {'Cookie': 'sessionid='}
    session = requests.session()
    session.headers = headers
    resp = session.post(url_jssm, cookies=cookies)
    # print(resp.cookies.get_dict())
    params = {'page': i}
    response = session.get(url2, headers={'User-Agent': 'yuanrenxue.project'}, params=params)
    print(response.text)
    data = response.json()["data"]
    for d in data:
        data_list.append(d["value"])
print(data_list)
answer = max(data_list, key=data_list.count)
print(answer)
url = 'https://match.yuanrenxue.com/api/answer'
params = {'answer': answer, 'id': 3}
resq = requests.get(url, headers=login_headers, params=params)
data = resq.json()
print(data)

"""答案固定：8717
[2838, 7609, 8717, 6923, 5325, 4118, 8884, 8717, 2680, 3721, 
8490, 3148, 6025, 8526, 8529, 6481, 9489, 6599, 5500, 8717, 
185, 8498, 6102, 9222, 8717, 2008, 9827, 8717, 8224, 2929, 
3762, 567, 672, 8717, 9524, 7159, 986, 505, 6535, 9491, 
3612, 9095, 7357, 9307, 5650, 2109, 23, 8717, 2110, 2792]
"""