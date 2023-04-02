# -*- coding: utf-8 -*-
import requests
import base64

""" HTTP Basic Authentication 网站，适合做 HTTP 认证案例，用户名密码均为 admin。 """
""" 参考：https://blog.csdn.net/u011430225/article/details/51860091 """
""" 提示：服务器发现配置了http auth，带Authorization header去访问 """
""" 这是一种简单的身份认证，它是通过http的authorization请求头中，携带经过base64加密的用户名和密码而实现的一种认证。 """
""" 巩固练习base64加密解密编码过程 """

# 方法二：
for i in range(1, 11):
    url = f'https://ssr3.scrape.center/page/{i}'
    resp = requests.get(url, auth=('admin', 'admin'))   # auth 参数上下两种写法
    # from requests.auth import HTTPBasicAuth
    # resp = requests.get(url, auth=HTTPBasicAuth('admin', 'admin'))
    print(resp.status_code, url)
    # print(resp.text)

# 方法一：
###############################################################################
s = 'admin:admin'  # user:password
d = base64.b64encode(s.encode('utf-8')).decode('utf-8')  # 默认'utf-8'可省略不写
print(d)  # s编码后结果d
dd = 'YWRtaW46YWRtaW4='
ss = base64.b64decode(dd).decode('utf-8')
print(ss)  # dd解码后结果ss

url = 'https://ssr3.scrape.center'
resp = requests.get(url)
print(resp.status_code, url)

for i in range(1, 11):
    url = f'https://ssr3.scrape.center/page/{i}'
    # headers = {'Authorization': 'Basic YWRtaW46YWRtaW4='}
    headers = {'Authorization': f'Basic {d}'}
    resp = requests.get(url, headers=headers)
    print(resp.status_code, url)
    # print(resp.text)
