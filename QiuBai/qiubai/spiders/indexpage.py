# -*- coding: utf-8 -*-
import scrapy

class QiuBaiItem(scrapy.Item):
    author = scrapy.Field()
    content = scrapy.Field()
    

class QiuBaiSpider(scrapy.Spider):
    name="qiubai"
    url = "http://www.qiushibaike.com/8hr/page/"    
    start_urls = [ url+str(i) for i in range(1,5)]

    def parse(self,response):
        item = QiuBaiItem()
        item['author'] = response.xpath('//div[@class="author clearfix"]//h2/text()').extract()
        item['content'] = response.xpath('//div[@class="content"]/span/text()').extract()
        '''
        print "===============================================" *3
        print "author:",item['author']
        print "content:",item['content']
        print "===============================================" *3
        '''
        yield item

