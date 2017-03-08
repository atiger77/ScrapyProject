# -*- coding: utf-8 -*-

import scrapy
from kelagirl.items import KelagirlItem

class KeLaGirlSpider(scrapy.Spider):
    name="kelagirl"
    start_urls = [
        "http://www.kelagirls.com/zhuanji!findForIndexMoreTag.action?tagId=0&page=1",
        "http://www.kelagirls.com/zhuanji!findForIndexMoreTag.action?tagId=0&page=2",
        "http://www.kelagirls.com/zhuanji!findForIndexMoreTag.action?tagId=0&page=3",
    ]

    def parse(self,response):
        print response.xpath('//div[@class="zhuanjimorewrap"]/div/@pid').extract()
