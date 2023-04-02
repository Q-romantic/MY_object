# -*- coding: utf-8 -*-
import pprint
import re
import httpx
import parsel
from tqdm import tqdm
import requests

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
def get_comment(oid):
    url = f'https://comment.bilibili.com/{oid}.xml'  # 知乎推荐
    # url = f'https://api.bilibili.com/x/v1/dm/list.so?oid={oid}'  # bilibili前添加i后获取的评论接口链接
    resp = requests.get(url, headers=headers)
    resp.encoding = resp.apparent_encoding
    data = re.findall('<d p=".*?">(.*?)</d>', resp.text)
    total = len(data)
    data = "\n".join(data)
    print(data)
    print(f"total评论: {total}条")
    return total



def get_oid(url):  # 传入 detail_url 亦可
    resp = requests.get(url, headers=headers)
    resp.encoding = resp.apparent_encoding
    # resp.encoding = 'utf-8'
    # resp.encoding = 'utf-8-sig'
    # resp.encoding = 'unicode_escape'
    # print(resp.text)
    try:  # 直接找 cid 即可
        # 方法一
        data = re.findall('<script>window.__playinfo__=(.*?)</script>', resp.text)[0]
        pprint.pprint(eval(data))




        # data = re.findall('window\.__INITIAL_STATE__=(.*?);', resp.text)[0]
        # data = data.replace(':null', ':None').replace(':false', ':False').replace(':true', ':True')
        # data = eval(data)
        # aid = data['aid']
        # bvid = data['bvid']
        # cids = data['cidMap'][str(aid)]['cids']
        # cid = data['cidMap'][str(aid)]['cids']['1']
        # print(aid, bvid, cids)

        # 方法二
        cid = re.findall('"pages":\[\{"cid":(.*?),"page":1,', resp.text)[0]
        return cid
    except:
        cid = re.findall('"bvid":".*?","cid":(.*?),"cover":', resp.text)[0]
        return cid

# url = 'https://www.bilibili.com/'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33'}
# resp = requests.get(url, headers=headers)
# # resp.encoding = resp.apparent_encoding
# # resp.encoding = 'utf-8'
# resp.encoding = 'unicode_escape'
# # print(resp.text)

# data = re.findall('"url":"(.*?)",', resp.text)
# # data = re.findall('window\.__INITIAL_DATA__=(.*?)</script>', resp.text)[0]
# # data = data.encode("utf-8").decode("unicode-escape")
# # data = re.findall('"url":"(.*?)",', data)
#
# print(data, len(data))
# for url in tqdm(data):
#     # li = ['http://www.bilibili.com/bangumi/play/ep515328']  # 这个特殊
#     # for url in li:
#     li = ['video', 'play']
#     if any(name in url for name in li):
#         print(url)
#         oid = get_oid(url)
#         print('----' * 10)
#         print('----' * 10)
#         print(f'https://comment.bilibili.com/{oid}.xml')
#         total = get_comment(oid)
#         if total == 0:
#             with open('url.txt', 'a+', encoding='utf-8') as f:
#                 f.write(url)
#                 f.write('\n')
#         # break


def get_big_type_comment(type_id):
    url = 'https://api.bilibili.com/x/web-interface/dynamic/region'
    params = {
        'ps': 1,  # 单页数量
        'pn': 1,  # 页码
        'rid': type_id,  # 首页分类
    }
    with httpx.Client(http2=True) as client:
        resp = client.get(url, params=params, headers=headers)
        data = resp.json()['data']['archives']
        # pprint.pprint(resp.json())
        for archives in data:
            big_type = archives['tname']
            aid = archives['aid']
            bvid = archives['bvid']
            cid = archives['cid']
            detail_url = archives['short_link']
            print(detail_url)

            oid = cid
            comment_url = f'https://comment.bilibili.com/{oid}.xml'
            print(comment_url)
            get_comment(oid)  # 获取弹幕信息


if __name__ == '__main__':
    # rids = [1,13,168,3,129,4,36,188,234,223,160,211,217,119,155,5,23,11,181,177]
    rids = {
        1: "综合·MAD·AMV·MMD·3D·短片·手书·配音",
        13: "官方延伸·连载动画·完结动画",
        168: "国产原创相关",
        3: "翻唱·音乐现场·音乐综合·音乐教学",
        129: "明星舞蹈·中国舞·舞蹈综合",
        4: "单机游戏·电子竞技·网络游戏·手机游戏",
        36: "人文历史·社科·法律·心理·校园学习·财经商业",
        188: "数码·极客DIY·科工机械",
        234: "篮球·运动综合·足球·健身",
        223: "摩托车·购车攻略·汽车生活·赛车",
        160: "搞笑·日常·绘画",
        211: "美食制作·美食测评·美食侦探",
        217: "动物综合·野生动物·喵星人·汪星人",
        119: "人力VOCALOID·鬼畜剧场·鬼畜调教",
        155: "美妆护肤·穿搭·时尚潮流",
        5: "明星综合·粉丝创作·娱乐杂谈",
        23: "欧美电影",
        11: "海外剧·国产剧",
        181: "影视剪辑·短片·影视杂谈",
        177: "社会·美食·旅行·科学·探索·自然·人文·历史",
    }
    # for type_id in rids:
    #     get_big_type_comment(type_id)
    #     break
    url = 'https://www.bilibili.com/video/BV1qS4y1w7tP'
    oid = get_oid(url)
    get_comment(oid)
