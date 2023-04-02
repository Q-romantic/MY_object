# -*- coding: utf-8 -*-
import requests

"""  """
""" 提示： """
for i in range(1, 11):
# for i in range(1, 503):
#     url = 'https://app1.scrape.center/api/movie'
#     url = 'https://app2.scrape.center/api/movie'
    url = 'https://app3.scrape.center/api/movie'
    params = {
        'limit': 10,
        'offset': (i - 1) * 10,
    }
    resp = requests.get(url, params=params)
    print(resp.status_code, resp.url)
    # print(resp.text)
    data = resp.json()['results']
    for i in data:
        name = i['name']
        jpg_link = i['cover'].split('@')[0]
        types = i['categories']
        info = [i['regions'], str(i['minute']) + '分钟']
        release = i['published_at']
        details = 'https://spa1.scrape.center/detail/' + str(i['id'])
        score = i['score']
        print(name, jpg_link, types, info, release, details, score)
    break
