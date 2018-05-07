# -*- coding: utf-8 -*-
import scrapy


class MerchantsSpider(scrapy.Spider):
    name = "merchants"
    allowed_domains = ["cn.made-in-china.com"]
    start_urls = ['http://cn.made-in-china.com/']

    def parse(self, response):
        pass
