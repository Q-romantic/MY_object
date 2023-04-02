from lxml import etree
from jsonpath import jsonpath
from requests_html import HTMLSession

session = HTMLSession()

url = 'https://restapi.amap.com/v3/place/text?' \
      's=rsv3' \
      '&key=6e79f6d236e295632f21b385e363b6e8'
headers = {
    # 'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'Connection': 'keep-alive',
    # 'Cookie': 'UM_distinctid=17d804f1ea517-0b42febd9a17bb-59191459-1fa400-17d804f1ea6d88; cna=SSFsGblGMhgCAXU9Eseustw5; xlly_s=1; tfstk=cwqlBNVf3zu7iqu05gi73kN2xYfAaIxEskrb0lURASkrreEqUsbpuF70jtcl1_8C.; l=eBak6OrRgn-6rKlXBO5BFurza779gIRbzrVzaNbMiInca66lTFw6INCnd_le7dtjgtfU0U-rAS_2aReDStUdgFEXKZsqhySdYxJw-; isg=BOXl03Tc6_nIBQySR1JVlZk_9KEfIpm0s7rcvefKMpwr_gdwpHGFhAXYiGKIeLFs',
    # 'Host': 'restapi.amap.com',
    'Referer': 'https://lbs.amap.com/',
    # 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'Sec-Fetch-Dest': 'script',
    # 'Sec-Fetch-Mode': 'no-cors',
    # 'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
}

data = {
    # 's': 'rsv3',
    # 'children': '',
    # 'key': '6e79f6d236e295632f21b385e363b6e8',
    # 'offset': 1,
    # 'page': 1,
    # 'extensions': 'all',
    # 'city': 110000,
    # 'language': 'zh_cn',
    # 'callback': 'jsonp_529204_',
    # 'platform': 'JS',
    # 'logversion': 2.0,
    # 'appname': 'https://lbs.amap.com/tools/picker',
    # 'csid': '637EEF57-92FF-4776-A429-5DFC4748BBDD',
    # 'sdkversion': '1.4.18',
    'keywords': '海南省',
}
response = session.get(url, headers=headers, data=data)
# print(response.text)
name_list = jsonpath(response.json(), '$..name')
location_list = jsonpath(response.json(), '$..location')
for name, location in zip(name_list, location_list):
    # print('[' + name + '][lon]' + location + '[/lat]')  # replace(',', '[/lon][lat]')
    print(name + ': [' + location + ']')
