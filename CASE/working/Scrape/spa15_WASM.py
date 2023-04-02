# -*- coding: utf-8 -*-
import requests
import time

""" 电影数据网站，数据通过 Ajax 加载，数据接口参数加密且有时间限制，加密过程通过字符串型 WASM 实现，适合 WASM 逆向分析。 """
""" 提示：js逆向，???? """

for i in range(1, 11):
    t = int(time.time())
    s = "/api/movie"
    token = '??'
    url = 'https://spa15.scrape.center/api/movie/'
    params = {
        'limit': 10,
        'offset': (i - 1) * 10,
        'token': token,
    }
    resp = requests.get(url, params=params)
    print(resp.status_code, url)
    print(resp.text)
    # data = resp.json()['results']
    # for i in data:
    #     name = i['name']
    #     jpg_link = i['cover'].split('@')[0]
    #     types = i['categories']
    #     info = [i['regions'], str(i['minute']) + '分钟']
    #     release = i['published_at']
    #     details = 'https://spa1.scrape.center/detail/' + str(i['id'])
    #     score = i['score']
    #     print(name, jpg_link, types, info, release, details, score)
    # break
