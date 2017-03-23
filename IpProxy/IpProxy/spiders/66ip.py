# -*- coding: utf-8 -*-

import scrapy
from IpProxy.items import IpProxyItem
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


class sixsixip(scrapy.Spider):
    name="66ip"
    start_urls = [
        "http://www.66ip.cn/areaindex_1/1.html",
    ]

    def parse(self,response):
        item = IpProxyItem()
        item['proxy_ipaddr'] =  response.xpath('//*[@id="footer"]/div/table//tr/td[1]/text()').extract()
        item['proxy_port'] = response.xpath('//*[@id="footer"]/div/table//tr/td[2]/text()').extract()
        '''
        print "=" * 15
        print "ipaddr:",item['proxy_ipaddr']," port:",item['proxy_port']
        '''
        yield item
