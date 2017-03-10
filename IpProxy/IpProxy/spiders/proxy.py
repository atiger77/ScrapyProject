# -*- coding: utf-8 -*-

import scrapy
class IpProxySpider(scrapy.Spider):
    name="IpProxy"
    start_urls = [
        "http://www.xxx.com/",
    ]

    def parse(self,response):
        print response.xpath('//div[@class="content"]').extract()
