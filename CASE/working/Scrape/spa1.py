# -*- coding: utf-8 -*-
import pprint
import requests

""" 猫眼电影数据网站，数据通过 Ajax 加载，页面动态渲染，适合 Ajax 分析和动态页面渲染爬取。 """
""" 提示：考察参数规律 """
for i in range(1, 11):
    url = 'https://spa1.scrape.center/api/movie/'
    params = {
        'limit': 10,
        'offset': (i - 1) * 10,
    }
    resp = requests.get(url, params=params)
    print(resp.status_code, resp.url)
    # print(resp.text)
    # pprint.pprint(resp.json())
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

# import requests
# import pandas as pd
#
# ajax_url = "https://spa1.scrape.center/api/movie/?limit={}&offset={}"
# res = requests.get(ajax_url.format(100, 0))
# res = json.loads(res.json())
#
# my_df = pd.DataFrame(res["results"])
# my_df.to_excel("spa1.xlsx", index=False)
