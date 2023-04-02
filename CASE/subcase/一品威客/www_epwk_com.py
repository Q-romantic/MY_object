# -*- coding: utf-8 -*-
import csv
import parsel
import requests

""" https://task.epwk.com/ """

f = open('data.csv', mode='wt', encoding='utf-8', newline='')
# 方式一（字典索引写入）
head = [
    '名称',
    '交易模式',
    '预估总价',
    '投递人数',
    'detail_url',
    '任务需求',
]
dit_writer = csv.DictWriter(f, fieldnames=head)
dit_writer.writeheader()  # 写入表头

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44'}
url = 'https://task.epwk.com/page1.html'
response = requests.get(url, headers=headers)
selector = parsel.Selector(response.text)
# divs = selector.xpath('//div[@class="itemblock"]')
divs = selector.xpath('//div[@class="content-lists"]/div')
for div in divs[:-1]:
    title = div.xpath('.//a/text()').get()
    detail_url = div.xpath('.//a/@href').get()
    trade_mode = div.xpath('.//div[@class="modelName"]/text()').get().strip()
    abort_time = div.xpath('.//div[@class="prcDesc"]/span/text()').get()  # 疑似动态加载
    people = div.xpath('.//div[@class="browser"]/div[3]/span/text()').get()
    price = div.xpath('.//div[@class="right"]/span/text()').get()

    response_2 = requests.get(detail_url, headers=headers)
    selector = parsel.Selector(response_2.text)
    task_info = '\n'.join(selector.xpath('//div[@class="task-info-content"]//text()').getall()).strip()

    dit = {
        '名称': title,
        '交易模式': trade_mode,
        '预估总价': price,
        '投递人数': people,
        'detail_url': detail_url,
        '任务需求': task_info,
    }
    dit_writer.writerow(dit)  # 按表头字典写入

    print(title, detail_url, trade_mode, abort_time, people, price, task_info)
    # break
f.close()
