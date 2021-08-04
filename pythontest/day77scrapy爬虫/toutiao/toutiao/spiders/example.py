
"""
scrapy爬虫框架使用入门
"""
from datetime import date,timedelta

import scrapy

today=date.today()

class ToutiaoItem(scrapy.Item):
    title=scrapy.Field()
    link=scrapy.Field()

class ToutiaoSpider(scrapy.Spider):
    name='Toutiao'
    start_urls=[f'https://toutiao.io/prev/{today-timedelta(days=i)}' for i in range(100)]

    def parse(self,response):
        for post in response.xpath('//h3[@class="title"]/a'):
            item=ToutiaoItem()
            item['title']=post.xpath('@title').extract_first()
            item['link']=post.xpath('@href').extract_first()
            yield item