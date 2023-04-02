# -*- coding: utf-8 -*-
import json
import requests

""" 对接图文点选验证码，适合图文点选验证码分析处理。 """
""" 提示：对于字典嵌套字典传参方式用json.dumps()函数处理 """

url = 'https://captcha6.scrape.center/api/login'
data1 = {
    "username": "admin",
    "password": "admin",
    "captcha": {
        "geetest_challenge": "6334bc0ad720bc197d66cbcc443435446z",
        "geetest_validate": "630559a530279fbea624a95e20724d09",
        "geetest_seccode": "630559a530279fbea624a95e20724d09|jordan",
        "status": 1,
        "type": "geetest",
    }

}

data2 = {
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

data3 = {
    "username": "admin",
    "password": "admin",
    "captcha": {
        "geetest_challenge": "9bb47edf2890baff9241896bedc6fbd9",
        "geetest_validate": "1fd828ccba8651d790b1b037db4429e6",
        "geetest_seccode": "1fd828ccba8651d790b1b037db4429e6|jordan",
        "status": 1,
        "type": "geetest"
    }
}
data4 = {
    "username": "admin",
    "password": "admin",
    "captcha": {
        "geetest_challenge": "2f786ad6240e1ae89afecc2f8f5e0f8d",
        "geetest_validate": "cb4688edb29f3e175754723b376197ec",
        "geetest_seccode": "cb4688edb29f3e175754723b376197ec|jordan",
        "status": 1,
        "type": "geetest"
    }
}

data5 = {
    "username": "admin",
    "password": "admin",
    "captcha": {
        "geetest_challenge": "536fb16afcf0c1a34c7b2e36a5e94ac3",
        "geetest_validate": "986d696310f149f23e2fb1f39e6d6113",
        "geetest_seccode": "986d696310f149f23e2fb1f39e6d6113|jordan",
        "status": 1,
        "type": "geetest"
    }
}
data = {
    "username": "admin",
    "password": "admin",
    "captcha": {
        "geetest_challenge": "654a8976d3292eb9aebb31c9be805c6f",
        "geetest_validate": "8a3f6fa49f46c1df1695213e949dd39d",
        "geetest_seccode": "8a3f6fa49f46c1df1695213e949dd39d|jordan",
        "status": 1,
        "type": "geetest"
    }
}

resp = requests.post(url, data=json.dumps(data))
print(resp.status_code)
print(resp.text)
