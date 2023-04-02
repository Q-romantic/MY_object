# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/16  016 下午 18:22
@Author  : Jan
@File    : 百度翻译_v1.py
"""
import requests
import re
import execjs

""" {} """

session = requests.session()
index_url = 'https://fanyi.baidu.com/'
lang_url = 'https://fanyi.baidu.com/langdetect'
translate_api = 'https://fanyi.baidu.com/v2transapi'

ctx = execjs.compile(open('百度翻译_v1.js', encoding='utf-8').read())

headers = {
    # 'Host': 'fanyi.baidu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
}


def get_token_and_gtk(query):
    # 获取 token 和 gtk 和 lang
    session.get(url=index_url, headers=headers)
    # print(session.cookies.get_dict())
    response_index = session.get(url=index_url, headers=headers)
    token = re.findall(r"token: '([0-9a-z]+)'", response_index.text)[0]
    gtk = re.findall(r'gtk = "(.*?)"', response_index.text)[0]
    # 自动检测语言
    response_lang = session.post(url=lang_url, headers=headers, data={'query': query})
    lang = response_lang.json()['lan']
    return token, gtk, lang


def get_acstoken(query, params, key):
    url = f"https://fanyi.baidu.com/#{params['from']}/{params['to']}/" + query
    ua = headers.get('User-Agent')
    acstoken = ctx.call("AcsToken", url, ua, key)
    return acstoken


def get_data(query, token, gtk, lang):
    sign = ctx.call("sign", query, gtk)
    params = {
        "from": lang,
        "to": "zh" if lang == "en" else "en"
    }
    data = {
        "from": lang,
        "to": "zh" if lang == "en" else "en",
        "query": query,
        "transtype": "realtime",
        "simple_means_flag": "3",
        "sign": sign,
        "token": token,
        "domain": "common"
    }
    while True:
        # 折腾一圈既然可有可无，让人哭笑不得
        global key
        key = 'aiyyeswmsceomsaa'
        # key = 'meaaauoegemaaaqs'
        # session.headers['Acs-Token'] = get_acstoken(query, params, key)
        resp = session.post(translate_api, params=params, data=data)
        res = resp.json()
        if 'errmsg' in res:
            # print(key, res)
            if key == 'aiyyeswmsceomsaa':
                key = 'meaaauoegemaaaqs'
            else:
                key = 'aiyyeswmsceomsaa'
        else:
            result = {
                query: f"{res['trans_result']['data'][0]['dst']}"
            }
            # print(acstoken)
            print(result)
            break


if __name__ == '__main__':
    querys = ['英文', '中文']
    for query in querys:
        token, gtk, lang = get_token_and_gtk(query)
        get_data(query, token, gtk, lang)
