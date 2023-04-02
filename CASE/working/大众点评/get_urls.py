import requests
from lxml import etree

url = 'https://www.dianping.com/citylist'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44',
}

resp = requests.get(url, headers=headers)
xml = etree.HTML(resp.text)
onecity_link = xml.xpath('//*[@id="main"]/div[4]/ul/li/div[2]/div/a/@href')
onecity_name = xml.xpath('//*[@id="main"]/div[4]/ul/li/div[2]/div/a/text()')
# print(ls)
for i, j in zip(onecity_name, onecity_link):
    j = 'http:' + j
    # print(i, j)
    resp = requests.get(j, headers=headers)
    xml = etree.HTML(resp.text)
    click_names = xml.xpath('//*[@id="nav"]/div/ul/li/div[1]/span/a//text()')
    click_links = xml.xpath('//*[@id="nav"]/div/ul/li/div[1]/span/a//@href')
    for click_name, click_link in zip(click_names, click_links):
        click_link = 'http:' + click_link
        # print(i, click_name, click_link)
        resp = requests.get(click_link, headers=headers)
        # print(resp.text)
        xml = etree.HTML(resp.text)
        click_ns = xml.xpath('//ul/li/div[2]/div[1]/a/h4/text()')
        click_ls = xml.xpath('//ul/li/div[2]/div[1]/a/@href')
        for click_n, click_l in zip(click_ns, click_ls):
            print(i, click_name, click_n, click_l)
        break

    break













