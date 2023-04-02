# -*- coding: utf-8 -*-
import requests
import re  # 正则表达式
import pprint
import json
import time
from working.IP_Headers_Proxies import headers
from working.IP_Headers_Proxies import proxies
proxies = {}

for timestamp in range(15, 75, 30):  # timestamp 最大值等于片长+15s，js代码timestamp = 30 * parseInt((t + 1) / 30) + 15
    url = 'https://mfm.video.qq.com/danmu'
    t = int(time.time() * 1000)
    params = {
        'otype': 'json',
        'callback': 'jQuery19108412063141030974_1654684198697',
        'target_id': '7861406841&vid=g0042gpd5ax',
        'session_key': '0,524,1654684199',
        'timestamp': timestamp,
        '_': t,
    }
    resp = requests.get(url, params=params, headers=headers, proxies=proxies)
    data = json.loads(resp.text[41:-1])
    # pprint.pprint(data)
    for contents in data['comments']:
        content = contents['content']
        opername = contents['opername']
        print('--->', content)


# url = 'https://upos-sz-mirrorhwo1.bilivideo.com/upgcxcode/21/51/724105121/724105121-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1654619907&gen=playurlv2&os=hwo1bv&oi=1026609166&trid=63d6c148d00f4a0b81c1d46c040f89f4u&mid=0&platform=pc&upsig=ba4e2b211455b60c5375e2485aed3160&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&agrr=1&bw=39958&logo=40000000'
#
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
#
# resp =requests.get(url, headers=headers)
# with open('1.mp3', 'wb') as f:
#     f.write(resp.content)