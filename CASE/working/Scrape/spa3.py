# -*- coding: utf-8 -*-
import requests
import pprint

""" 猫眼电影数据网站，数据通过 Ajax 加载，无页码翻页，适合 Ajax 分析和动态页面渲染抓取。 """
""" 提示：简单模拟翻页 """
for i in range(1, 11):
    url = 'https://spa3.scrape.center/api/movie'
    params = {
        'limit': 10,
        'offset': (i - 1) * 10,
    }
    resp = requests.get(url, params=params)
    print(resp.status_code, resp.url)
    # print(resp.text)
    # break
