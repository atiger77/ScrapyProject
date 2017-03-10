# -*- coding: utf-8 -*-

import scrapy

'''
相关网站整理
http://www.kuaidaili.com/free/
http://www.xicidaili.com/
http://www.proxy360.cn/default.aspx
http://ip.zdaye.com/ 端口号是图片需要OCR
'''


class IpProxySpider(scrapy.Spider):
    name="IpProxy"
    start_urls = [
        "http://www.xxx.com/",
    ]

    def parse(self,response):
        print response.xpath('').extract()
