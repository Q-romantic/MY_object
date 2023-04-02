import scrapy

from ..items import ChinadailyItem


class EnglishSpider(scrapy.Spider):
    name = 'english'
    allowed_domains = ['chinadaily.com.cn']     # 限制域名爬取
    start_urls = [f'http://language.chinadaily.com.cn/thelatest/page_{page}.html' for page in range(1, 11)]

    def parse(self, response):
        divs = response.xpath('//div[@class="gy_box"]')
        for div in divs:
            title = div.xpath('./div/p[1]/a/text()').get()
            title_url = 'http:' + div.xpath('./div/p[1]/a/@href').get()
            info = div.xpath('./div/p[2]/a/text()').get()
            img_url = 'http:' + div.xpath('./a/img/@src').get()

            # print(title, title_url, info, img_url)
            item = ChinadailyItem(title=title, title_url=title_url, info=info, img_url=img_url)
            yield item
























        pass
