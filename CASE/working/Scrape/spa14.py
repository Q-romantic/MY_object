# -*- coding: utf-8 -*-
import requests
import time

""" 电影数据网站，数据通过 Ajax 加载，数据接口参数加密且有时间限制，加密过程通过数值型 WASM 实现，适合 WASM 逆向分析。 """
""" 提示：js逆向，进入函数内部看运行过程 """

p_ip = requests.get('https://proxypool.scrape.center/random').text
proxies = {'http': f'http://{p_ip}', 'https': f'http://{p_ip}'}
print(proxies)
for i in range(1, 11):
    t = int(time.time())
    sign = (i - 1) * 10 + int(t / 3) + 16358  # 通过调试，sign有效期为当前时间上下60s[-60s,+60s]
    url = 'https://spa14.scrape.center/api/movie/'
    params = {
        'limit': 10,
        'offset': (i - 1) * 10,
        'sign': sign,
    }
    resp = requests.get(url, params=params)
    print(resp.status_code, url)
    # print(resp.text)
    data = resp.json()['results']
    for i in data:
        name = i['name']
        jpg_link = i['cover'].split('@')[0]
        types = i['categories']
        info = [i['regions'], str(i['minute']) + '分钟']
        release = i['published_at']
        details = 'https://spa1.scrape.center/detail/' + str(i['id'])
        score = i['score']
        print(name, jpg_link, types, info, release, details, score)
    break
