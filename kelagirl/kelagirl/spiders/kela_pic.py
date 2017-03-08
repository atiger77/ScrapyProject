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
        uid_list = response.xpath('//div[@class="zhuanjimorewrap"]/div/@pid').extract()
        urls = ["http://www.kelagirls.com/zhuanji!findForDetail.action?pid=",]
        for i in uid_list:
            url = urls[0] + i 
            yield scrapy.Request(url,callback=self.parse_item))

    def parse_item(self,response):
        item = KelagirlItem()
        #继续爬取图片路径
