# -*- coding: utf-8 -*-
import scrapy


class TouytiaoSpider(scrapy.Spider):
    name = 'touytiao'
    allowed_domains = ['toutiao.com']
    start_urls = ['http://toutiao.com/']

    def parse(self, response):
        pass
