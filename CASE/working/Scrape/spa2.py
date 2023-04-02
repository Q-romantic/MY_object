# -*- coding: utf-8 -*-
import time
import requests
import hashlib
import base64

""" 猫眼电影数据网站，数据通过 Ajax 加载，数据接口参数加密且有时间限制，适合动态页面渲染爬取或 JavaScript 逆向分析。 """
""" 提示：通过逆向追踪加密方式及加密字符串来源走向规律 """


def get_details_info(data, t):
    for i in data['results']:
        movie_id = i['id']
        s0 = 'ef34#teuq0btua#(-57w1q5o5--j@98xygimlyfxs*-!i-0-mb' + str(movie_id)
        token1 = base64.b64encode(s0.encode()).decode()
        url = f'https://spa2.scrape.center/api/movie/{token1}'
        s1 = f'/api/movie/{token1},0,{t}'
        s2 = hashlib.sha1(s1.encode()).hexdigest() + f',{t}'
        token2 = base64.b64encode(s2.encode()).decode()
        resp = requests.get(url, params={'token': token2})
        print(resp.status_code, resp.url)
        # print(resp.text)
        # li = []
        # for j in resp.json()['actors']:
        #     li.append(j['name'])
        # print('actors：', li)
        # break


for i in range(1, 11):
    url = 'https://spa2.scrape.center/api/movie/'
    t = int(time.time())
    s = f"/api/movie,{(i - 1) * 10},{t}"
    sha1 = hashlib.sha1(s.encode('utf-8'))
    result = sha1.hexdigest()
    s = result + f",{t}"
    token = base64.b64encode(s.encode()).decode()
    params = {
        'limit': 10,
        'offset': (i - 1) * 10,
        'token': token,
    }
    resp = requests.get(url, params=params)
    print(resp.status_code, resp.url)
    # print(resp.text)
    get_details_info(resp.json(), t)
    break
