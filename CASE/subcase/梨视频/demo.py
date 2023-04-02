# -*- coding: utf-8 -*-
"""
@Time    : 2022/6/30  030 下午 20:52
@Author  : Jan
@File    : demo.py
"""
import random
import requests
from lxml import etree
from working.all_tools.tools import getip
from working.all_tools.tools import getua

""" {} """

proxies = {
    'http': 'http://' + getip(),
    # 'https': 'https://' + getip(),
}

headers = {
    "User-Agent": getua(),

}


def get_mp4_url(url):
    contId = url[-7:]
    headers = {
        "User-Agent": getua(),
        "Referer": url,
    }
    params = {
        'contId': contId,
        'mrd': random.random(),
    }
    mid_url = 'https://www.pearvideo.com/videoStatus.jsp'
    response = requests.get(mid_url, headers=headers, params=params, data={}, proxies=proxies)
    data = response.json()
    s = data["videoInfo"]["videos"]["srcUrl"]
    # pprint.pprint(data)
    # print(response)
    ss = s.split('-', 1)
    mp4_url = ss[0][:-13] + f'cont-{contId}-' + ss[1]
    print(mp4_url)
    return mp4_url


def get_urls():
    url = 'https://www.pearvideo.com/category_loading.jsp'
    for page in range(1, 4):
        headers = {
            "User-Agent": getua(),
            "Referer": "https://www.pearvideo.com/category_8",
        }
        params = {
            "reqType": "5",
            "categoryId": "8",
            "start": 12 * page,
            "mrd": random.random(),
            # "filterIds": "1766537,1766459,1766177,1764511,1764305,1758399,1758401,1758411,1763979,1763973,1763902,1763069,1762664,1757471,1757482"
        }
        response = requests.get(url, headers=headers, params=params, data={}, proxies=proxies)
        response.encoding = 'utf-8'
        data = response.text
        selector = etree.HTML(data)
        list = selector.xpath('//*[@class="categoryem"]')
        for i in list:
            href = 'https://www.pearvideo.com/' + i.xpath('.//div[@class="vervideo-bd"]/a/@href')[0]
            title = i.xpath('.//div[@class="vervideo-title"]/text()')[0]
            print(title, href)
            # mp4_url = get_mp4_url(href)
            # save_mp4(title, mp4_url)
        # break


def save_mp4(name, url):
    data = requests.get(url, headers={"User-Agent": getua()}).content
    with open(str(name) + ".mp4", 'wb+') as f:
        f.write(data)


if __name__ == '__main__':
    url = 'https://www.pearvideo.com/video_1766459'
    # get_mp4_url(url)
    get_urls()

    # mp4_url = 'https://video.pearvideo.com/mp4/third/20220614/cont-1765364-10097838-222509-hd.mp4'
    # save_mp4(1, mp4_url)
