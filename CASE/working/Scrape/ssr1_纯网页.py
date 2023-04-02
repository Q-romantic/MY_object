# -*- coding: utf-8 -*-
import requests
import csv
from lxml import etree
import prettytable as pt
tb = pt.PrettyTable()
tb.field_names = ['电影名称', 'Img', '类型', '拼多多', '上映时间', 'detail', '评分']


""" 猫眼电影数据网站，数据通过服务端渲染，适合基本爬虫练习 """
""" 提示：模拟翻页、xpath练习、字符串处理，区别绝对和相对路径，取文本属性和链接属性，如：@href、@src """

for i in range(1, 11):
    url = f'https://ssr1.scrape.center/page/{i}'
    resp = requests.get(url)

    # print(resp.text)
    # xml = etree.HTML(resp.text)
    # divs = xml.xpath('//*[@id="index"]/div[1]/div[1]/div')
    # for div in divs:
    #     name = div.xpath('./div/div/div[2]/a/h2/text()')[0].split(' - ')[0]
    #     jpg_link = div.xpath('./div/div/div[1]/a/img/@src')[0].split('@')[0]
    #     types = div.xpath('./div/div/div[2]/div[1]/button/span/text()')
    #     info = ''.join(div.xpath('./div/div/div[2]/div[2]/span/text()'))
    #     release = div.xpath('./div/div/div[2]/div[3]/span/text()')
    #     details = 'https://ssr1.scrape.center' + \
    #               div.xpath('//*[@id="index"]/div[1]/div[1]/div[1]/div/div/div[2]/a/@href')[0]
    #     score = div.xpath('./div/div/div[3]/p[1]/text()')[0].strip()
    #     li = [name, jpg_link, types, info, release, details, score]
    #     # print(li)
    #     # tb.add_row(li)
    #
    #
    #     def writer_csv(data_list):
    #         '''将爬取的数据存储到 data.csv 文件'''
    #         with open('./data.csv', 'a+', newline='', encoding='utf-8-sig') as f:
    #             writer = csv.writer(f)
    #             writer.writerow(data_list)

        # writer_csv(li)
        # break
    break
print(tb)