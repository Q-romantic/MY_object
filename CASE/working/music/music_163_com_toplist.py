# -*- coding: utf-8 -*-
import requests
import parsel
import music_163_com as w

url = 'https://music.163.com/discover/toplist'  # 排行榜

resp = requests.get(url)
sel = parsel.Selector(resp.text)

url_class_list = sel.xpath('//p[@class="name"]/a/@href').getall()
name_class_list = sel.xpath('//p[@class="name"]/a/text()').getall()
for url, name in zip(url_class_list, name_class_list):
    url = 'https://music.163.com/#' + url
    print(url, name)
    resp = requests.get(url.replace('#/', ''))
    sel = parsel.Selector(resp.text)
    url_list = sel.xpath('//ul[@class="f-hide"]/li/a/@href').getall()
    name_list = sel.xpath('//ul[@class="f-hide"]/li/a/text()').getall()
    for url, name in zip(url_list, name_list):
        url = 'https://music.163.com/#' + url
        print(url, name)
        w.download_song(url)
        w.download_lyric(url)
        w.get_comments_data(url)
        # break
    print('===' * 30)
    break
