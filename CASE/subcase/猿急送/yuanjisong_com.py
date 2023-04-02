# -*- coding: utf-8 -*-
import requests
import parsel
import csv

""" https://www.yuanjisong.com/job """

f = open('data.csv', mode='wt', encoding='utf-8', newline='')
# 方式一（字典索引写入）
head = [
    '名称',
    '合作方式',
    '预估总价',
    '预估工时',
    '所在区域',
    '投递人数',
    '发布项目',
    'detail_url',
    '需求描述',
]
dit_writer = csv.DictWriter(f, fieldnames=head)
dit_writer.writeheader()  # 写入表头

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44'}

for page in range(1, 2):
    url = f'https://www.yuanjisong.com/job/allcity/page{page}'
    response = requests.get(url, headers=headers)
    selector = parsel.Selector(response.text)
    detail_url_list = selector.xpath('/html/body/div[2]/div[1]/div/div/a[1]/@href').getall()
    # print(detail_url_list)

    for detail_url in detail_url_list[1:]:
        response = requests.get(detail_url)
        selector = parsel.Selector(response.text)
        title = selector.xpath('/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/h2/text()').get().strip()
        item_title = selector.xpath('/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/div/ul/li[2]/text()').get().strip()
        price = selector.xpath('/html/body/div[2]/div[1]/div[2]/div[2]/div[4]/div/ul/li[2]/text()').get().strip()
        job_time = selector.xpath('/html/body/div[2]/div[1]/div[2]/div[2]/div[5]/div/ul/li[2]/text()').get().strip()
        area = selector.xpath('/html/body/div[2]/div[1]/div[2]/div[2]/div[6]/div/ul/li[2]/text()').get().strip()
        job_info = selector.xpath('/html/body/div[2]/div[1]/div[3]/div[1]/div/p/text()').getall()
        people = selector.xpath('//*[@id="i_post_num_151162"]/text()').get()
        total = selector.xpath('/html/body/div[2]/div[2]/div[1]/ul/li[1]/span[2]/a/text()').get().strip()

        dit = {
            '名称': title,
            '合作方式': item_title,
            '预估总价': price,
            '预估工时': job_time,
            '所在区域': area,
            '投递人数': people,
            '发布项目': total,
            'detail_url': detail_url,
            '需求描述': job_info,
        }
        dit_writer.writerow(dit)  # 按表头字典写入
        print(title, item_title, price, job_time, area, job_info, people, total)

f.close()
