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


class xicidaili(scrapy.Spider):
    name="xici"
    url = "http://www.xicidaili.com/nn/"
    start_urls = [
        url + str(i) for i in range(1,5)
    ]


    def parse(self,response):
        item = IpProxyItem()
        item['proxy_ipaddr'] =  response.xpath('//*[@id="ip_list"]//tr/td[2]/text()').extract()
        item['proxy_port'] = response.xpath('//*[@id="ip_list"]//tr/td[3]/text()').extract()
        ''' 
        print "=" * 15
        print "xici ipaddr:"
        print "ipaddr:",item['proxy_ipaddr']," port:",item['proxy_port']
        print "=" * 15
        '''
        yield item
