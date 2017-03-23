# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IpProxyItem(scrapy.Item):
    proxy_ipaddr = scrapy.Field()
    proxy_port = scrapy.Field()
