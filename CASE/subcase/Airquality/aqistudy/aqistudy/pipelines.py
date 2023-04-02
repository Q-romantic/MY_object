# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
from itemadapter import ItemAdapter


class AqistudyPipeline:
    def __init__(self):
        self.f = open('data.csv', mode='a', encoding='utf-8', newline='')
        self.csv_write = csv.DictWriter(self.f, fieldnames=['日期', 'AQI', '质量等级', 'PM2.5', 'PM10', 'CO', 'SO2', 'NO2', 'O3_8h', 'city', 'rank'])
        self.csv_write.writeheader()
        self.csv_write = csv.DictWriter(self.f, fieldnames=['time_point', 'aqi', 'quality', 'pm2_5', 'pm10', 'co', 'so2', 'no2', 'o3', 'city', 'rank'])
        self.csv_write.writeheader()

    def process_item(self, item, spider):
        self.csv_write.writerow(dict(item))
        return item

    def close_file(self):
        self.f.close()
