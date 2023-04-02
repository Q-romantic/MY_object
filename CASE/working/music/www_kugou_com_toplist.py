# -*- coding: utf-8 -*-
import requests
import parsel
import re
import www_kugou_com as kg

url_rank = 'https://www.kugou.com/yy/rank/home/1-6666.html?from=rank'


def get_rank_url():
    resp = requests.get(url_rank)
    sel = parsel.Selector(resp.text)
    n_list = sel.xpath('//div[@class="pc_temp_side"]/div/ul/li/a/text()[2]').getall()
    u_list = sel.xpath('//div[@class="pc_temp_side"]/div/ul/li/a/@href').getall()
    for name, u in zip(n_list, u_list):
        name = name.strip()
        print(u, name)
        get_homepage_url(u, name)
        print('===' * 30)
        # break


def get_homepage_url(_url, _name):
    # url = url.replace('from=rank', 'from=homepage')
    resp = requests.get(_url)
    sel = parsel.Selector(resp.text)
    obj = re.compile('<li class=" " title="(?P<name>.*?)" data-index=', re.S)
    n_list = obj.findall(resp.text)
    # n_list = sel.xpath('//div[@class="pc_temp_songlist "]/ul/li').attrib.get('title')
    u_list = sel.xpath('//div[@id="rankWrap"]/div[2]/ul/li/a/@href').getall()
    for name, u in zip(n_list, u_list):
        print(_name, u, name)
        # kg.get_data(u)  # 下载歌曲歌词到文件


if __name__ == '__main__':
    get_rank_url()
