from lxml import etree
from jsonpath import jsonpath
from requests_html import HTMLSession

session = HTMLSession()

url = 'https://www.zhipin.com/job_detail/'
# url = 'https://www.zhipin.com/job_detail/?query=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&city=101010100&industry=&position='

headers = {
    # ':authority': 'www.zhipin.com',
    # ':method': 'GET',
    # ':path': '/job_detail/?query=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&city=101010100&industry=&position=',
    # ':scheme': 'https',
    # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'accept-encoding': 'gzip, deflate, br',
    # 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'cookie': 'lastCity=101010100; __zp_seo_uuid__=fed53952-9780-45b0-9025-858751b0b85d; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1646196653,1646197419; acw_tc=0bcb2f0616461986093455528ea33fe740a1b8a98ee1ba41721b0cc462fb29; __c=1646196653; __l=r=https%3A%2F%2Fcn.bing.com%2F&l=%2Fwww.zhipin.com%2Fjob_detail%2F%3Fquery%3D%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%26city%3D101010100%26industry%3D%26position%3D&s=3&g=&friend_source=0&s=3&friend_source=0; __a=43018174.1646196653..1646196653.17.1.17.17; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1646198610; __zp_stoken__=c139dZ289ZHs2bz9JTUVHOW8vcyxfMVN0LTpwNkY3H2oIaGlsUC52NEg7FjRrTVo9JiAPdEcmE2BSCmQYNG5XdAsmRkwCHVBnJGZDVwFfCy5oRxoTIktyZgl9GjoJKCAnZBk9ADUGZxhtOmE%3D',
    'cookie': 'lastCity=101010100; historyState=state; wd_guid=0e9912a9-1417-4a39-b285-01d79c0a27eb; _9755xjdesxxd_=32; gdxidpyhxdE=40Oje6oxGGv3XVZPd0OiSaMWs0f3AsOt7TnsREBqXNHinQ8Akm/hHjH1LB23q6xMyuQ5biv76ZpX3+ffMz343gVwmAqMLrxlz6mJ5Dhf4jHjTZnJafH7v5TsDZJfcBeJoYRTvjvR7xu9C\VJGQ+gUtisTimg5BYA8l/i1ath57JNt955:1646203558088; YD00951578218230:WM_NI=EghCUvTPrQaXYQnb9m2owMWHAyMsKupsJzSPKrOcaLPaUKAAm/ithkuVgbsatfDxmYQyeOrlcL6rR3l8Vt7EFAQdJlPiXkT4KQszeJi/wNaomH7rQb1vrf5MOcZxK9iLQU4=; YD00951578218230:WM_NIKE=9ca17ae2e6ffcda170e2e6ee93e549b09982a8f27081b08eb3d44b838f9ebaf47af2899daae6408a8fb693bb2af0fea7c3b92a87b9a8a4d87e9890beb2e4549b8fa283bc67f2b1b9aed64483a78394ca7fb4ad869bd25c89ae8184e44894bf9bacc44baff1a795eb61b78aa983f26bb8ba8c99f05393a7abb0f168a194fa93d139b0e89a95b64f869f9f85c96894b7988cd740898fbd9be842abf1b9afe465af98f993d46af3aabe87b8478dbd9699ca33ab949fb6b737e2a3; YD00951578218230:WM_TID=a9FM0GzVftVEREBFRQdr+2HWYg9JRmv9; _bl_uid=edld70v990g6IOke9ktp5Fz6LCU7; acw_tc=0bdd34f616502850223523713e019c0b1c1194a65798590134d7714b9f8474; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1648876013,1649729128,1650285022; __g=-; __c=1650285023; __l=l=/www.zhipin.com/job_detail/&s=3&friend_source=0; __a=43018174.1646196653.1649729129.1650285023.141.6.2.141; __zp_stoken__=d12bdfGxjIGouKSJ2WStjczZLTmV5MVN/L2UvD34Ybl44cTEpZTcybXopJFBNFDdiD381ZRFFRGVcVjosJ0E4TnI1GzxCBUU7BgQWYxReYi5iGHIMSj1xAUkdFhlALEkqTUYHG2BDNBhgZTQ=; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1650285065',
    # 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'sec-fetch-dest': 'document',
    # 'sec-fetch-mode': 'navigate',
    # 'sec-fetch-site': 'none',
    # 'sec-fetch-user': '?1',
    # 'upgrade-insecure-requests': '1',
    # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
}
page = 0

data = {
    'query': '数据分析',
    'city': '101010100',
    'page': page,
    'ka': 'page-next',
}
def zhiweixinxi():
    response = session.get(url, headers=headers, params=data)
    # response = session.get(url, headers=headers)
    # print(response.text)
    xml = etree.HTML(response.content.decode())

    zhiwei_list = xml.xpath('//*[@id="main"]/div/div[3]/ul/li/div/div[1]/div[1]/div/div[1]/span[1]/a/text()')
    zhiweilianjie_list = xml.xpath('//*[@id="main"]/div/div[3]/ul/li/div/div[1]/div[1]/div/div[1]/span[1]/a/@href')   # 加前缀'https://www.zhipin.com'
    gongzuodidian_list = xml.xpath('//*[@id="main"]/div/div[3]/ul/li/div/div[1]/div[1]/div/div[1]/span[2]/span/text()')
    xinzi_list = xml.xpath('//*[@id="main"]/div/div[3]/ul/li/div/div[1]/div[1]/div/div[2]/span/text()')
    gongzuonianxian_list1 = xml.xpath('//*[@id="main"]/div/div[3]/ul/li/div/div[1]/div[1]/div/div[2]/p/text()[1]')
    gongzuonianxian_list2 = xml.xpath('//*[@id="main"]/div/div[3]/ul/li/div/div[1]/div[1]/div/div[2]/p/text()[2]')
    jn_list1 = xml.xpath('//*[@id="main"]/div/div[3]/ul/li/div/div[2]/div[1]/span[1]/text()')
    jn_list2 = xml.xpath('//*[@id="main"]/div/div[3]/ul/li/div/div[2]/div[1]/span[2]/text()')
    jn_list3 = xml.xpath('//*[@id="main"]/div/div[3]/ul/li/div/div[2]/div[1]/span[3]/text()')
    jn_list4 = xml.xpath('//*[@id="main"]/div/div[3]/ul/li/div/div[2]/div[1]/span[4]/text()')
    jn_list5 = xml.xpath('//*[@id="main"]/div/div[3]/ul/li/div/div[2]/div[1]/span[5]/text()')
    danweimingcheng_list = xml.xpath('//*[@id="main"]/div/div[3]/ul/li/div/div[1]/div[2]/div/h3/a/text()')

    # t = xml.xpath('/text()')
    # t = xml.xpath('/text()')

    for zhiwei,gongzuodidian,xinzi,gongzuonianxian1,gongzuonianxian2,jn1,jn2,jn3,jn4,jn5,danweimingcheng,zhiweilianjie in zip(zhiwei_list,gongzuodidian_list,xinzi_list,gongzuonianxian_list1,gongzuonianxian_list2,jn_list1,jn_list2,jn_list3,jn_list4,jn_list5,danweimingcheng_list,zhiweilianjie_list):
        # linkinfo = session.get('https://www.zhipin.com'+zhiweilianjie, headers=headers)
        # xml2 = etree.HTML(linkinfo.content.decode())
        # yaoqiu = xml2.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div/div/text()')
        print(page,zhiwei,gongzuodidian,xinzi,gongzuonianxian1+'|'+gongzuonianxian2,jn1+'|'+jn2+'|'+jn3+'|'+jn4+'|'+jn5,danweimingcheng,'https://www.zhipin.com'+zhiweilianjie)

for i in range(1,10):
    page = i
    zhiweixinxi()










# xml = etree.HTML(response.content.decode())
# k = 0
# for i in range(3, 37):
#     shenghui = xml.xpath('//*[@id="showtext"]/div[{}]/div[1]/text()'.format(i))[0]
#     chengshi = xml.xpath('//*[@id="showtext"]/div[{}]/div[2]/a/text()'.format(i))
#
#     for j in chengshi:
#         url2 = 'https://www.toolnb.com/Tools/Index/gps.html'
#         data = {
#             'city': j,
#         }
#         response_data = session.post(url2, headers=headers, data=data)
#         lon = jsonpath(response_data.json(), '$..longitude')[0]
#         lat = jsonpath(response_data.json(), '$..latitude')[0]
#         print('[' + shenghui + '-' + j + '][lon]' + lon + '[/lon][lat]' + lat + '[/lat]')
#         k += 1
#     # break
# print(k)

# //*[@id="showtext"]/div[36]/div[1]

# info = response.xpath('//*/a/text()')
# info1 = response.xpath('//*/a/@href')
# print(info)


# for k in range(1,4):

# info = response.xpath('//*[@id="contents"]/p/text()')
# for i in info:
#     print(i)
