# -*- coding: utf-8 -*-
"""
@Time    : 2022/7/1  001 下午 14:06
@Author  : Jan
@File    : 弹幕.py
"""
import json
import re
import zlib
import requests
from xml.dom.minidom import parse
import xml.dom.minidom
from working.all_tools.tools import getip
from working.all_tools.tools import getua

""" {} """

headers = {
    "User-Agent": getua(),
    "cookie": "QC005=0cdeacebe253b1ad40190acf36ea6324; QC006=c427f7c430de6f8499b557345a035c6e; QP0030=1; QC173=0; P00004=.1625663848.c1b8b2ef98; user_type=web; QC170=1; SDKENTERTYPE=normal_login; GC_PCA=false; T00404=aed185152a4c04e518bcab8c1e8281f3; QIYUECK=qy_pc_71f21f31bc714f83a19df711fb53fa3f; TQC030=1; QP008=0; _ga=GA1.2.2116955020.1655029929; QC008=1632826003.1655029929.1656655373.11; QC175=%7B%22upd%22%3Atrue%2C%22ct%22%3A%22%22%7D; nu=0; QP0034=%7B%22v%22%3A1%2C%22m%22%3A%7B%22wm-vp9%22%3A1%7D%7D; QP0033=1; QP0035=2; QC007=DIRECT; QP007=360; Hm_lpvt_53b7374a63c37483e5dd97d78d9bb36e=1656659677; Hm_lvt_53b7374a63c37483e5dd97d78d9bb36e=1655029929,1656659677; __dfp=a1fc1f8bb5ba6b4f0fb19443be939cb8c2ccee677efaa53bd1f1523f48701c55b1@1657951374312@1656655375312; QC010=218278045; QP0027=15; T00700=EgcI9L-tIRABEgcI67-tIRAMEgcI58DtIRABEgcI8L-tIRABEgcIz7-tIRABEgcIkMDtIRABEgcIg8DtIRABEgcI0b-tIRABEgcI4b-tIRABEgcIhcDtIRABEgcIi8HtIRAJEgcI87-tIRABEgcI7L-tIRABEgcImMDtIRABEgcI57-tIRABEgcIisHtIRAB; QP0037=485; QC159=%7B%22color%22%3A%22FFFFFF%22%2C%22channelConfig%22%3A1%2C%22hadTip%22%3A1%2C%22isOpen%22%3A1%2C%22speed%22%3A10%2C%22density%22%3A40%2C%22opacity%22%3A86%2C%22isFilterColorFont%22%3A1%2C%22isOpenMask%22%3A0%2C%22proofShield%22%3A0%2C%22forcedFontSize%22%3A24%2C%22isFilterImage%22%3A1%2C%22defaultSwitch%22%3A0%2C%22isset%22%3A1%2C%22openRecord%22%3A%5B1656655495449%5D%7D; QP0036=202271%7C496.941; IMS=IggQAhj_s_yVBiozCiA0MTY0ZjcyZTgyYTgxNzRkYmNjMjhkODAwMzkwNzdhNxAAIggI0AUQAhiwCSjoAjAFciQKIDQxNjRmNzJlODJhODE3NGRiY2MyOGQ4MDAzOTA3N2E3EACCAQCKASQKIgogNDE2NGY3MmU4MmE4MTc0ZGJjYzI4ZDgwMDM5MDc3YTc",
}

proxies = {
    'http': 'http://' + getip(),
    # 'https': 'https://' + getip(),
}
url = 'https://www.iqiyi.com/v_1zo488bnv6s.html'
# url = 'https://www.iqiyi.com/v_jgqg7i8714.html'
response = requests.get(url, headers=headers, params={}, data={}, proxies=proxies)
response.encoding = response.apparent_encoding
data = response.text
playPageInfo = re.findall('window\..*?=(\{.*?\});', data)[0]
playPageInfo = json.loads(playPageInfo)
# pprint.pprint(playPageInfo)
title = playPageInfo['shortTitle']
tvid = str(playPageInfo['tvId'])
vid = playPageInfo['vid']
a = tvid[-4:-2]
b = tvid[-2:]
# print(playPageInfo)


# 'https://cmts.iqiyi.com/bullet/94/00/7223202647699400_60_1_97b3562c.br'
# 'https://cmts.iqiyi.com/bullet/94/00/7223202647699400_60_2_f6b75784.br'
# 'https://cmts.iqiyi.com/bullet/94/00/7223202647699400_60_3_5617a204.br'

url = f'https://cmts.iqiyi.com/bullet/{a}/{b}/{tvid}_300_1.z'
# url = 'https://cmts.iqiyi.com/bullet/94/00/7223202647699400_300_2.z'
# url = 'https://cmts.iqiyi.com/bullet/94/00/7223202647699400_300_3.z'
# print(url)
response = requests.get(url, headers=headers, params={}, data={}, proxies=proxies)
data = response.content


# print(data)
# print(response)

def zipdecode(data_z):
    """对zip压缩的二进制内容解码成文本"""
    decode = zlib.decompress(bytearray(data_z), 15 + 32).decode('utf-8')
    return decode


# 读取xml文件中的弹幕数据数据
def xml_parse(xml_data):
    DOMTree = xml.dom.minidom.parseString(xml_data)
    collection = DOMTree.documentElement
    # 在集合中获取所有entry数据
    entrys = collection.getElementsByTagName("entry")
    # print(entrys)
    for entry in entrys:
        uid = entry.getElementsByTagName('uid')[0].childNodes[0].data
        content = entry.getElementsByTagName('content')[0].childNodes[0].data
        likeCount = entry.getElementsByTagName('likeCount')[0].childNodes[0].data
        print(uid, content, likeCount)


xml_data = zipdecode(data)
# print(xml_data)
xml_parse(xml_data)
