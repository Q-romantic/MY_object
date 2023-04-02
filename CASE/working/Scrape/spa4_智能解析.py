# -*- coding: utf-8 -*-
import requests

""" 新闻网站索引，数据通过 Ajax 加载，无页码翻页，适合 Ajax 分析和动态页面渲染抓取以及智能页面提取分析。 """
""" 提示：简单模拟翻页 """
# for i in range(1, 16):
#     url = 'https://spa4.scrape.center/api/news'
#     params = {
#         'limit': 10,
#         'offset': (i - 1) * 10,
#     }
#     resp = requests.get(url, params=params)
#     print(resp.status_code, resp.url)
#     # print(resp.text)
#     # break


# 方法二：智能解析中使用的是newspaper库
import pandas as pd
import requests
from newspaper import Article  # python39 -m pip install newspaper3k

title, url, authors, published = [], [], [], []
the_url = 'https://spa4.scrape.center/api/news/?limit=10&offset=0'
response = requests.get(the_url)
data = response.json()
for i in range(0, 10):
    url.append(data['results'][i]['url'])
    news = Article(url[i], language='zh')
    news.download()  # 加载网页
    news.parse()  # 解析网页
    title.append(news.title)
    authors.append(news.authors)
    published.append(news.publish_date)

bt = {
    "链接": url,
    "标题": title,
    "作者": authors,
    "发布时间": published
}
print(bt)
# work = pd.DataFrame(bt)
# work.to_csv('work.csv')
