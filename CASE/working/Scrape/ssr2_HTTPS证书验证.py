# -*- coding: utf-8 -*-
import requests
from lxml import etree
from requests.packages import urllib3
urllib3.disable_warnings()


""" 电影数据网站，无反爬，无 HTTPS 证书，适合用作 HTTPS 证书验证。 """
""" 提示： """
for i in range(1, 11):
    url = f'https://ssr2.scrape.center/page/{i}'
    resp = requests.get(url, verify=False)
    # print(resp.text)
    xml = etree.HTML(resp.text)
    divs = xml.xpath('//*[@id="index"]/div[1]/div[1]/div')
    for div in divs:
        name = div.xpath('./div/div/div[2]/a/h2/text()')[0].split(' - ')[0]
        jpg_link = div.xpath('./div/div/div[1]/a/img/@src')[0].split('@')[0]
        types = div.xpath('./div/div/div[2]/div[1]/button/span/text()')
        info = ''.join(div.xpath('./div/div/div[2]/div[2]/span/text()'))
        release = div.xpath('./div/div/div[2]/div[3]/span/text()')
        details = 'https://ssr1.scrape.center' + \
                  div.xpath('//*[@id="index"]/div[1]/div[1]/div[1]/div/div/div[2]/a/@href')[0]
        score = div.xpath('./div/div/div[3]/p[1]/text()')[0].strip()
        print(name, jpg_link, types, info, release, details, score)
        # break
    break
