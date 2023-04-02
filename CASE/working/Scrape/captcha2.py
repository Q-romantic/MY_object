# -*- coding: utf-8 -*-
import json
import requests

""" 对接图标点选验证码，适合图标点选验证码分析处理。 """
""" 提示：对于字典嵌套字典传参方式用json.dumps()函数处理 """

url = 'https://captcha2.scrape.center/api/login'
# data1 = {
#     "username": "admin",
#     "password": "admin",
#     "captcha": {
#         "geetest_challenge": "6334bc0ad720bc197d66cbcc443435446z",
#         "geetest_validate": "630559a530279fbea624a95e20724d09",
#         "geetest_seccode": "630559a530279fbea624a95e20724d09|jordan",
#         "status": 1,
#         "type": "geetest",
#     }
#
# }

data = {
    "username": "admin",
    "password": "admin",
    "captcha": {
        "geetest_challenge": "1ffbadee6ff0abf2b78eee17cda99689",
        "geetest_validate": "fa9a7ae8b09dc3b94920b20382b1e551",
        "geetest_seccode": "fa9a7ae8b09dc3b94920b20382b1e551|jordan",
        "status": 1,
        "type": "geetest"
    }
}

resp = requests.post(url, data=json.dumps(data))
print(resp.status_code)
print(resp.text)
