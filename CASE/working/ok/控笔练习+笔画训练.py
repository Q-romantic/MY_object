import requests
from lxml import etree

filename_no_str = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']
url = 'https://www.sohu.com/a/488253621_121124330'

response = requests.get(url)
# print(response.text)
xml = etree.HTML(response.text)
png_list = xml.xpath('//*[@id="mp-editor"]/p/img')
for i in png_list:
    filename_url = i.attrib['src']
    if '.png' in filename_url:
        png = requests.get(filename_url, stream=True)
        path = './数据/' + filename_url[-8:]
        # with open(path, 'wb') as f:
        #     f.write(png.content)
        print(path, filename_url)
        print()
    # break
