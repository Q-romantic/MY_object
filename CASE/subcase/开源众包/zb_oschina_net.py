# -*- coding: utf-8 -*-
import csv
import requests

""" https://zb.oschina.net/projects/list.html """

f = open('data.csv', mode='wt', encoding='utf-8', newline='')
# 方式一（字典索引写入）
head = [
    '名称',
    '悬赏标签',
    '预估价',
    '预估工时',
    '参与人数',
    '发布日期',
    'detail_url',
    '技能要求',
]
dit_writer = csv.DictWriter(f, fieldnames=head)
dit_writer.writeheader()  # 写入表头

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44'}
url = 'https://zb.oschina.net/project/contractor-browse-project-and-reward'
for page in range(1, 16):
    params = {
        "keyword": "",
        "applicationAreas": "",
        "type": "2",
        "sortBy": "30",
        "currentTime": "2022-06-19 09:32:30",
        "pageSize": "20",
        "currentPage": page
    }
    response = requests.get(url, headers=headers, params=params)
    # pprint.pprint(response.json())
    datas = response.json()['data']['data']
    for data in datas:
        # pprint.pprint(data)
        name = data['name']
        application = data['application']
        budgetMaxByYuan = data['budgetMaxByYuan']
        cycleName = data['cycleName']
        applyCount = data['applyCount']
        publishTime = data['publishTime']

        url_id = data['id']

        detail_url = f'https://zb.oschina.net/reward/detail?id={url_id}'
        params = {'id': url_id}
        response = requests.get(detail_url, headers=headers, params=params)
        # pprint.pprint(response.json())
        prd = response.json()['data']['prd']

        dit = {
            '名称': name,
            '悬赏标签': application,
            '预估价': budgetMaxByYuan,
            '预估工时': cycleName,
            '参与人数': applyCount,
            '发布日期': publishTime,
            'detail_url': detail_url,
            '技能要求': prd,
        }
        dit_writer.writerow(dit)  # 按表头字典写入
        print(name, application, budgetMaxByYuan, cycleName, applyCount, publishTime, detail_url, prd)

        # break
    # break
