# -*- coding: utf-8 -*-
import requests
import time
import hashlib
import base64

""" 8、JavaScript 反爬，增加了接口处的无限 debugger 和定时循环 debugger。 """
""" 9、JavaScript 反爬，核心加密逻辑使用位置移动数组混淆，同时设置格式化保护，适合 AST 分析。 """
""" 提示：无 """
""" 参考：常见的无限debugger反调试策略以及应对方法 https://www.jianshu.com/p/838922415c70 """

for i in range(1, 11):
    # url = 'https://antispider8.scrape.center/api/movie/'
    url = 'https://antispider9.scrape.center/api/movie/'
    t = int(time.time())
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
    print(resp.text)
    # get_details_info(resp.json(), t)
    break
