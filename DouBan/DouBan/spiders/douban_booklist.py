# -*- coding: utf-8 -*-
import scrapy

class QiuBaiItem(scrapy.Item):
    author = scrapy.Field()
    content = scrapy.Field()
    

class QiuBaiSpider(scrapy.Spider):
    name="qiubai"
    url = "https://www.douban.com/doulist/1264675/"    

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

