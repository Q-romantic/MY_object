# -*- coding: utf-8 -*-
import requests

""" 对接文字偏移反爬，所见顺序并不一定和源码顺序一致，适合用作文字偏移反爬练习。 """
""" 提示：？？？ """

for i in range(1, 11):
    url = 'https://antispider3.scrape.center/api/book'
    params = {
        'limit': 18,
        'offset': (i - 1) * 18,
    }
    resp = requests.get(url, params=params)
    data = resp.json()['results']
    for i in data:
        name = i['name']
        sub_url = 'https://spa5.scrape.center/detail/'+str(i['id'])
        authors = str(i['authors']).replace('\\n', '').replace(' ', '')
        img_url = i['cover']
        score = i['score']
        print(name, sub_url, authors, img_url, score)
    print(resp.status_code, resp.url)
    break
