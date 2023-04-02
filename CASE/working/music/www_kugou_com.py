# -*- coding: utf-8 -*-
import requests
import parsel
import re
import os
import time

""" https://www.kugou.com """

# url = 'https://www.kugou.com/mixsong/5rcb3re6.html'
url = 'https://www.kugou.com/mixsong/25x2ed44.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36',
    "referer": "https://www.kugou.com",
    'cookie': 'kg_mid=914d8a90cf050c2d7652300b12833188; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1670934816; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22gzlogin-user.kugou.com%22%5D%5D%7D; kg_dfid=1Jd6g51EeBus2WMc351n5fuP; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; KuGooRandom=66691670934843756; kg_mid_temp=914d8a90cf050c2d7652300b12833188; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1670936040',

}

def get_data(url):
    resp = requests.get(url, headers=headers)
    # 方法一：
    # sel = parsel.Selector(resp.text)
    # audio_name = sel.xpath('//div[@class="songDetail clearfix"]/p/a/text()').getall()[0]
    # lyirc = sel.xpath('//div[@class="displayNone"]/text()').getall()[0]

    obj = re.search('var dataFromSmarty = \[{"hash":"(?P<hash>.*?)",.*?'
                    '"album_id":(?P<album_id>.*?),"mixsongid":(?P<mixsongid>.*?)}],', resp.text)
    # print(resp.text)
    hash_num = obj.group('hash')
    album_id = obj.group('album_id')
    mixsongid = obj.group('mixsongid')

    url_song = 'https://wwwapi.kugou.com/yy/index.php'
    # params = {
    #     'r': 'play/getdata',
    #     'hash': hash_num,
    #     'album_id': album_id,
    #     # 'mixsongid': mixsongid,
    #     # '_': int(time.time()*1000),
    # }
    params = {
        "r": "play/getdata",
        "encode_album_audio_id": url.split('/')[-1][:-5],
    }
    resp = requests.get(url_song, headers=headers, params=params)
    # print(resp.text)
    data = resp.json()['data']
    audio_name = data['audio_name']
    lyrics = data['lyrics']
    play_url = data['play_url']
    play_backup_url = data['play_backup_url']
    print(play_url)
    # print(play_backup_url)

    obj = re.sub('\[.*?\]', '', lyrics).split('\r\n')
    obj = [i for i in obj if i][1:-1]
    lyric = '\n'.join(obj)

    def download_song(url, name):
        resp = requests.get(url)
        data = resp.content
        filename = name + '.mp3'
        os_mkdir_path = os.getcwd() + '\\歌曲\\'
        if not os.path.exists(os_mkdir_path):
            os.mkdir(os_mkdir_path)
        with open(os_mkdir_path + filename, 'wb') as ff:
            ff.write(data)

    def download_lrc(lyric, name):
        filename = name + '.lrc'
        os_mkdir_path = os.getcwd() + '\\歌曲\\'
        if not os.path.exists(os_mkdir_path):
            os.mkdir(os_mkdir_path)
        with open(os_mkdir_path + filename, 'w', encoding='utf-8') as ff:
            ff.write(lyric)

    print(url, audio_name)
    # print(lyric)
    print('===' * 20)
    download_song(play_url, audio_name)
    download_lrc(lyric, audio_name)


if __name__ == '__main__':
    get_data(url)
