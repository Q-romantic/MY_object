# -*- coding: utf-8 -*-
import base64
import json
import requests

""" 登录时用户名和密码经过加密处理，适合 JavaScript 逆向分析。 """
""" 提示：
BTOA Binary-to-ASCII
javascript函数（适用于mozilla），
btoa： 将普通字符串转为Base64字符串
atob： 将Base64字符串转为普通字符串
"""

data = {
    'username': 'admin',
    'password': 'admin',
}
url = 'https://login1.scrape.center/'
token = base64.b64encode(json.dumps(data).encode()).decode()
# 注意这里是 get 请求，如果是 post 请求的话会报 405 错误代码。
r = requests.get(url=url, data={'token': token})
print(token)
print(r.status_code)
print(r.url, r.text)
