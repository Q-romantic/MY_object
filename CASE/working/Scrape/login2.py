# -*- coding: utf-8 -*-
from lxml import etree
import requests

""" 对接 Session + Cookies 模拟登录，适合用作 Session + Cookies 模拟登录练习。 """
""" 提示： """

url = 'https://login2.scrape.center/login'

session = requests.session()
data = {
    'username': 'admin',
    'password': 'admin',
}
session.post(url, data=data)
print(session.cookies)

for i in range(1, 11):
    url = f'https://login2.scrape.center/page/{i}'
    resp = session.get(url)
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
        print(resp.status_code, resp.url)
        print(name, jpg_link, types, info, release, details, score)
        break
    break


