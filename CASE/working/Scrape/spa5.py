# -*- coding: utf-8 -*-
import requests

""" 豆瓣图书网站，数据通过 Ajax 加载，有翻页，无反爬，适合大批量动态页面渲染抓取。 """
""" 提示：简单模拟翻页 """
for i in range(1, 11):
# for i in range(1, 503):
    url = 'https://spa5.scrape.center/api/book'
    params = {
        'limit': 18,
        'offset': (i - 1) * 10,
    }
    resp = requests.get(url, params=params)
    print(resp.status_code, resp.url)
    data = resp.json()['results']
    for i in data:
        name = i['name']
        sub_url = 'https://spa5.scrape.center/detail/'+str(i['id'])
        authors = str(i['authors']).replace('\\n', '').replace(' ', '')
        img_url = i['cover']
        score = i['score']
        print(name, sub_url, authors, img_url, score)
    break
