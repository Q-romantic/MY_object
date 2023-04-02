# -*- coding: utf-8 -*-
"""
1、处理获取网页中文字符编码乱码，输出后面 + resp.encoding = 'utf-8'
2、使用 xpath 语法需要根据网页实际获取到内容解析
3、考虑带不带 headers 获取网页是否一致
4、如下提供两种使用 xpath 语法方法
5、xpath 语法标签带多个属性可只写一个或全写用 and 连接
"""
import parsel
import requests
from lxml import etree
from lxml.html import fromstring

url = 'https://www.baidu.com'

resp = requests.get(url)  # 不带headers中user-agent，获取内容不全面
print(resp.encoding)  # ISO-8859-1
print(resp.apparent_encoding)  # GB2312
# resp.encoding = 'utf-8'
resp.encoding = resp.apparent_encoding
# print(resp.text)
sel = parsel.Selector(resp.text)
a = sel.xpath('//div[@id="u1"]/a/text()').getall()
print(a)

xml = etree.HTML(resp.text)
a = xml.xpath('//div[@id="u1"]/a/text()')
print(a)

sel = fromstring(resp.text)
a = sel.xpath('//div[@id="u1"]/a/text()')
print(a)


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29',
}
resp = requests.get(url, headers=headers)
resp.encoding = 'utf-8'
# print(resp.text)
sel = parsel.Selector(resp.text)
a = sel.xpath('//div[@id="s-top-left"]/a/text()').getall()
print(a)
a = sel.xpath('//div[@id="s-top-left"]/a/@href').getall()
print(a)
a = sel.xpath('//div[@id="s-top-left"]/a/@target').getall()
print(a)
a = sel.xpath('//div[@id="s-top-left"]/a/@class').getall()
print(a)


xml = etree.HTML(resp.text)
a = xml.xpath('//div[@id="s-top-left"]/a/@class')
print(a)
b = xml.xpath('//div[@id="s-top-left" and @class="s-top-left-new s-isindex-wrap"]/a/text()')
print(b)
c = sel.xpath('//ul[@class="s-hotsearch-content"]/li/a/span[2]/text()').getall()
print(c)
