# -*- coding: utf-8 -*-
import requests
import parsel
import re
import www_kuwo_cn as kw

""" https://www.kuwo.cn """

url_menu = 'https://www.kuwo.cn/api/www/bang/bang/bangMenu'


def get_bangMenu_url():
    headers = {
        'csrf': '3VR35BUI04P',
        'Cookie': 'kw_token=3VR35BUI04P',
    }
    resp = requests.get(url_menu, headers=headers)
    # print(resp.text)
    data = resp.json()['data']
    for i in data:
        for j in i['list']:
            name = j['name']
            bangId = j['sourceid']
            url_musicList = 'https://www.kuwo.cn/api/www/bang/bang/musicList'
            params = {
                'bangId': bangId,
                'pn': '1',
                'rn': '1',  # 可适当调节单页数量
            }
            resp = requests.get(url_musicList, headers=headers, params=params)
            num = resp.json()['data']['num']
            params['rn'] = num
            resp = requests.get(url_musicList, headers=headers, params=params)
            # print(resp.text)
            data = resp.json()['data']['musicList']
            for li in data:
                name_song = li['name']
                rid = li['rid']
                url = 'https://www.kuwo.cn/play_detail/' + str(rid)
                # print(li)
                print(name, bangId, name_song, url)
                # kw.get_data(url)
                # break
            break
        break


if __name__ == '__main__':
    get_bangMenu_url()
