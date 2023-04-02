# -*- coding: utf-8 -*-
import base64
import requests
import os
import re

""" https://y.qq.com """


def get_data(url):
    def get_song_name(url):
        resp = requests.get(url)
        obj = re.compile('<title>(?P<name>.*?) - QQ音乐-千万正版音乐海量无损曲库新歌热歌天天畅听的高品质音乐平台！</title>', re.S)
        title = obj.search(resp.text).group('name')
        strinfo = re.compile(r'[/:*?"<>|\\]')
        name = strinfo.sub('-', title)
        print(name)
        return name
        pass

    def download_song(url):
        songmid = url.split('/')[-1]
        url_song = 'https://u.y.qq.com/cgi-bin/musicu.fcg'
        params = {
            'data': '{"comm":{"uin":"","g_tk":""},'
                    '"req_5":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey",'
                    '"param":{"guid":"9110509931","songmid":["%s"],"platform":""}}}' % (songmid)
        }
        resp = requests.get(url_song, params=params)
        purl = resp.json()['req_5']['data']['midurlinfo'][0]['purl']
        url_mp3 = 'https://dl.stream.qqmusic.qq.com/' + purl
        print(url_mp3)

        def save():
            data = requests.get(url_mp3).content
            filename = get_song_name(url) + '.mp3'
            os_mkdir_path = os.getcwd() + '/歌曲/'
            if not os.path.exists(os_mkdir_path):
                os.mkdir(os_mkdir_path)
            with open(os_mkdir_path + filename, 'wb') as ff:
                ff.write(data)

        save()
        pass

    def download_lyric(url):
        url_lyric = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_new.fcg'
        headers = {'referer': 'https://y.qq.com/'}
        params = {'songmid': url.split('/')[-1]}
        resp = requests.get(url_lyric, headers=headers, params=params)
        s = eval(resp.text[18:-1])['lyric']
        lyric = base64.b64decode(s).decode()
        strinfo = re.compile('\[.*?\]')
        lyric = strinfo.sub('', lyric).strip()
        print(lyric)

        def save(lyric):
            filename = get_song_name(url) + '.lrc'
            os_mkdir_path = os.getcwd() + '\\歌曲\\'
            if not os.path.exists(os_mkdir_path):
                os.mkdir(os_mkdir_path)
            with open(os_mkdir_path + filename, 'w', encoding='utf-8') as ff:
                ff.write(lyric)
                # print(i)  # 输出显示歌词

        save(lyric)
        pass

    def get_comments_data(url):
        url_c = 'https://u.y.qq.com/cgi-bin/musics.fcg'
        params = {
            'sign': 'zzba7860a23ttcivhuw9hyamfspki3onge5afa21e',
            'data': '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":0,"g_tk_new_20200303":5381,"g_tk":5381},'
                    '"req_1":{"method":"GetCommentCount","module":"music.globalComment.GlobalCommentRead","param":{"request_list":[{"biz_type":1,"biz_id":"351816508","biz_sub_type":0}]}},'
                    '"req_2":{"module":"music.globalComment.CommentRead","method":"GetNewCommentList","param":{"BizType":1,"BizId":"351816508","LastCommentSeqNo":"","PageSize":25,"PageNum":0,"FromCommentId":"","WithHot":1,"PicEnable":1}},'
                    '"req_3":{"module":"music.globalComment.CommentRead","method":"GetHotCommentList","param":{"BizType":1,"BizId":"351816508","LastCommentSeqNo":"","PageSize":15,"PageNum":0,"HotType":2,"WithAirborne":1,"PicEnable":1}}}'
        }
        resp = requests.get(url_c, params=params)
        # print(resp.text)
        comments_list = resp.json()['req_2']['data']['CommentList']['Comments']
        for i in comments_list:  # SubComments 未统计
            u_id = i['EncryptUin']
            u_name = i['Nick']
            u_comment = i['Content']
            u_link = 'https://y.qq.com/n/ryqq/profile?uin=' + u_id
            print(u_name, u_link, u_comment)
        print(len(comments_list))
        pass

    download_lyric(url)
    download_song(url)
    get_comments_data(url)
    # get_song_name(url)


if __name__ == '__main__':
    url = 'https://y.qq.com/n/ryqq/songDetail/00219Qw032Qldd'
    get_data(url)
    pass
