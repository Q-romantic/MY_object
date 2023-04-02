# -*- coding: utf-8 -*-
import requests

""" 对接 User-Agent 反爬，检测到常见爬虫 User-Agent 就会拒绝响应，适合用作 User-Agent 反爬练习。 """
""" 提示：无UA信息报错403 """
for i in range(1, 11):
    url = f'https://antispider2.scrape.center/page/{i}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53',
    }
    resp = requests.get(url, headers=headers)
    print(resp.status_code, resp.url)
    # print(resp.text)
    # break
