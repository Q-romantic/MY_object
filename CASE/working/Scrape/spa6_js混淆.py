# -*- coding: utf-8 -*-
import time
import requests
import hashlib
import base64

""" 电影数据网站，数据通过 Ajax 加载，数据接口参数加密且有时间限制，源码经过混淆，适合 JavaScript 逆向分析。 """
""" 提示：js 混淆，连蒙带猜逐一分析，通过测试得出token有效时间为当前时间往后180s，即有效期3分钟 """
for i in range(1, 11):
    url = 'https://spa6.scrape.center/api/movie'
    t = int(time.time()) - 170  # 通过调节时间可控制token有效期限
    s = f"/api/movie,{t}"
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
    s = time.time()
    while 1:
        resp = requests.get(resp.url)
        if resp.status_code != 200:
            break
        print(resp.status_code)
        time.sleep(5)
    print(time.time() - s, resp.status_code, resp.url)
    # print(resp.text)
    break
