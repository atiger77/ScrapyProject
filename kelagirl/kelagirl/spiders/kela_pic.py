# -*- coding: utf-8 -*-

import scrapy
class KeLaGirlSpider(scrapy.Spider):
    name="kelagirl"
    start_urls = [
        "http://www.kelagirl.com/",
    ]

    def parse(self,response):
        print response.xpath('//div[@class="content"]').extract()
