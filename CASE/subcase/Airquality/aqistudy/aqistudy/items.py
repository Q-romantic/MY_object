# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AqistudyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    time_point = scrapy.Field()
    aqi = scrapy.Field()
    quality = scrapy.Field()
    pm2_5 = scrapy.Field()
    pm10 = scrapy.Field()
    co = scrapy.Field()
    so2 = scrapy.Field()
    no2 = scrapy.Field()
    o3 = scrapy.Field()
    city = scrapy.Field()
    rank = scrapy.Field()

    pass