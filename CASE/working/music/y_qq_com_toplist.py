# -*- coding: utf-8 -*-
import requests
from lxml import etree
import y_qq_com as qq

""" https://y.qq.com """

if __name__ == '__main__':
    url = 'https://u.y.qq.com/cgi-bin/musics.fcg'
    params = {
        'sign': 'zzb257ebf58dkmofrktpegwawhtqo8hg174cbc7a',
        'data': '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":0,"g_tk_new_20200303":5381,"g_tk":5381},'
                '"req_1":{"module":"musicToplist.ToplistInfoServer","method":"GetAll","param":{}}}',
    }

    resp = requests.get(url, params=params)
    # print(resp.text)
    data = resp.json()['req_1']['data']['group']
    for i in data:
        groupName = i['groupName']
        toplist = i['toplist']
        for j in toplist:
            topId = j['topId']
            title = j['title']
            url_top = 'https://y.qq.com/n/ryqq/toplist/' + str(topId)
            print(groupName, title, url_top)
            resp = requests.get(url_top)
            xml = etree.HTML(resp.text)
            n = xml.xpath('//ul[@class="songlist__list"]/li/div/div[3]/span/a[2]/text()')
            u = xml.xpath('//ul[@class="songlist__list"]/li/div/div[3]/span/a[2]/@href')
            for x, y in zip(n, u):
                y = 'https://y.qq.com' + y
                print(x, y)
                # qq.get_data(y)  # 下载等后续操作
            break
        break
