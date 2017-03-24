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
        "http://www.66ip.cn/areaindex_1/2.html", 
        "http://www.66ip.cn/areaindex_1/3.html", 
        "http://www.66ip.cn/areaindex_1/4.html"
    ]
 

    def parse(self,response):
        item = IpProxyItem()
        item['proxy_ipaddr'] =  response.xpath('//*[@id="footer"]/div/table//tr/td[1]/text()').extract()[1:-1]
        item['proxy_port'] = response.xpath('//*[@id="footer"]/div/table//tr/td[2]/text()').extract()[1:-1]
        '''
        print "=" * 15
        print "66ip ipaddr:"
        print "ipaddr:",item['proxy_ipaddr']," port:",item['proxy_port']
        print "=" * 15
        '''
        yield item
