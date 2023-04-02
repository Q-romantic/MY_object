# -*- coding: utf-8 -*-
import requests
import httpx

""" 图书网站，无反爬，不同于其他，该网站协议采用 HTTP 2，适合用于 HTTP 2 协议分析和测试。 """
""" 提示：参考猿人学17题 """

for i in range(1, 3):
    url = 'https://spa16.scrape.center/api/book/'
    params = {
        'limit': 18,
        'offset': (i - 1) * 18,
    }
    resp = httpx.Client(http2=True).get(url, params=params)
    print(resp.status_code, url)
    # print(resp.text)
    data = resp.json()['results']
    for i in data:
        name = i['name']
        sub_url = 'https://spa5.scrape.center/detail/' + str(i['id'])
        authors = str(i['authors']).replace('\\n', '').replace(' ', '')
        img_url = i['cover']
        score = i['score']
        print(name, sub_url, authors, img_url, score)
    break
