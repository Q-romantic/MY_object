from lxml import etree
from jsonpath import jsonpath
from requests_html import HTMLSession

session = HTMLSession()

url1 = 'https://www.toolnb.com/tools/gps.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62',
    'X-Requested-With': 'XMLHttpRequest',
}
response = session.get(url1, headers=headers)
xml = etree.HTML(response.content.decode())
k = 0

for tmp in [0.2,0.3,0.4,0.5,0.6,0.7]:
    for i in range(3, 37):
        shenghui = xml.xpath('//*[@id="showtext"]/div[{}]/div[1]/text()'.format(i))[0]
        chengshi = xml.xpath('//*[@id="showtext"]/div[{}]/div[2]/a/text()'.format(i))

        for j in chengshi:
            url2 = 'https://www.toolnb.com/Tools/Index/gps.html'
            data = {
                'city': j,
            }
            response_data = session.post(url2, headers=headers, data=data)
            # lon = jsonpath(response_data.json(), '$..longitude')[0]
            # lat = jsonpath(response_data.json(), '$..latitude')[0]
            lon = str(float(jsonpath(response_data.json(), '$..longitude')[0])+tmp)
            lat = str(float(jsonpath(response_data.json(), '$..latitude')[0])+tmp)
            print('[' + shenghui + '-' + j + '][lon]' + lon + '[/lon][lat]' + lat + '[/lat]')
            k += 1
    # break
print(k)
