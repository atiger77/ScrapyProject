# -*- coding: utf-8 -*-

import scrapy

'''
相关网站整理
http://www.kuaidaili.com/free/
http://www.xicidaili.com/
http://www.proxy360.cn/default.aspx
http://ip.zdaye.com/ 端口号是图片需要OCR
http://www.cz88.net/proxy
http://cn-proxy.com
http://www.66ip.cn
'''


class kuaidaili(scrapy.Spider):
#class IpProxySpider(scrapy.Spider):
    #name="IpProxy"
    name="kuaidaili"
    start_urls = [
        "http://www.kuaidaili.com/proxylist/1/",
    ]

    def parse(self,response):
        print response.xpath('//*[@id="index_free_list"]/table/tbody/tr[1]/td[1]').extract()
