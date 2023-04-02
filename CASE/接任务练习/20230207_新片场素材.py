# -*- coding: utf-8 -*-
"""
@Time    : 2023/2/7  007 下午 14:47
@Author  : Jan
@File    : 20230207_新片场素材.py
"""

""" {} """

import parsel
import requests

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
# keyword = '科技'
keyword = ''
page = 1
musicMoodTags = 0
url = f'https://stock.xinpianchang.com/music/list?from=seachtop&keyword={keyword}&page={page}&musicMoodTags={musicMoodTags}'
# url = f'https://stock.xinpianchang.com/music/list?keyword={keyword}&page={page}'
resp = requests.get(url, headers=headers)
resp.encoding = 'utf-8'
# print(resp.text)
sel = parsel.Selector(resp.text)
a = sel.xpath('//div[@class="music-box"]/div/@data-id').getall()  # 素材ID
print(a)
print('https://stock.xinpianchang.com/music/details/' + a[0])  # 详情链接
# a = sel.xpath('//div[@class="music-box"]/div/div/@data-music').getall()  # link
# print(a)
# a = sel.xpath('//div[@class="music-box"]/div/div/div[2]/div/a/text()').getall()  # title
# print(a)
# a = sel.xpath('//div[@class="music-box"]/div/div/div[2]/div/a/@href').getall()  # 详情链接
# print('https://stock.xinpianchang.com' + a[0])
