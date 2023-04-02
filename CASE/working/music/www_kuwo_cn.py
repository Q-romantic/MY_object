# -*- coding: utf-8 -*-
import requests
import os
import re
from lxml import etree

""" https://www.kuwo.cn """
""" 参考：https://www.cnblogs.com/zhiyiYo/p/16122664.html"""


def get_data(url):
    def get_song_name(url):
        response = requests.get(url)
        obj = re.compile('<title>(?P<name>.*?)_单曲在线试听_酷我音乐</title>')
        title = obj.search(response.text).group('name')
        strinfo = re.compile(r'[/:*?"<>|\\]')
        name = strinfo.sub('-', title)
        return name

    def download_song(url):
        url_play = 'https://www.kuwo.cn/api/v1/www/music/playUrl'
        params = {
            'mid': url.split('/')[-1],
            'type': 'convert_url3',
            # 'br': ['128kmp3', '192kmp3', '320kmp3'][2],  # 可选，据说指音质
        }

        resp = requests.get(url_play, params=params)
        mp3_url = resp.json()['data']['url']
        print(mp3_url)

        def save():
            data = requests.get(mp3_url).content
            filename = get_song_name(url) + '.mp3'
            os_mkdir_path = os.getcwd() + '/歌曲/'
            if not os.path.exists(os_mkdir_path):
                os.mkdir(os_mkdir_path)
            with open(os_mkdir_path + filename, 'wb') as ff:
                ff.write(data)
        # save()

    def download_lyric(url):
        url_lyric = url
        resp = requests.get(url_lyric)
        # xml = etree.HTML(resp.text)
        # text = xml.xpath('//div[@id="lyric"]/div/p/text()')[:-1]
        obj = re.compile('<p data-v-34783d0c>(.*?)</p>', re.S)
        lyric = obj.findall(resp.text)[1:]
        print(url_lyric)

        def save(lyric):
            filename = get_song_name(url) + '.lrc'
            os_mkdir_path = os.getcwd() + '\\歌曲\\'
            if not os.path.exists(os_mkdir_path):
                os.mkdir(os_mkdir_path)
            for i in lyric:
                with open(os_mkdir_path + filename, 'a+', encoding='utf-8') as ff:
                    ff.write(i + '\n')
                # print(i)  # 输出显示歌词

        # save(lyric)
        pass

    def get_comments_data(url):
        url_comments = 'https://www.kuwo.cn/comment'
        params = {
            'type': 'get_comment',
            'f': 'web',
            'page': '1',
            'rows': 20,  # 可手动指定评论量
            'digest': '15',
            'sid': url.split('/')[-1],
            'uid': '0',
            # 'prod': 'newWeb',
            # 'httpsStatus': '1',
            # 'reqId': '79b730e0-d18f-11ec-a4b5-e57470ba06bc',
        }
        resp = requests.get(url_comments, params=params)  # 评论全拿容易报错
        total = resp.json()['total']
        params['rows'] = total
        resp = requests.get(url_comments, params=params)
        data = resp.json()['rows']
        # print(resp.text)
        for i in data:
            u_time = i['time']
            u_id = i['u_id']
            u_name = i['u_name']
            msg = i['msg']
            # print(u_time + '_' + u_name + '_' + u_id + '：' + msg)  # 显示评论
        print(f'共 {len(data)} 条评论')
        pass

    try:
        download_lyric(url)
        download_song(url)
        get_comments_data(url)
    except:
        print('error：未能获取到数据')


if __name__ == '__main__':
    url = 'https://www.kuwo.cn/play_detail/216929788'
    get_data(url)
