# -*- coding: utf-8 -*-
#
import scrapy

class dydlItem(scrapy.Item): 
    title = scrapy.Field()
    content = scrapy.Field()


class dydlSpider(scrapy.Spider):
    name = "dyly"
    
    start_urls = [
        "https://news.dyly.com/",
    ]
   
    
    def start_requests(self):
        return [scrapy.http.FormRequest('https://news.dyly.com/getAppNewsList.do',method="POST",formdata={'ajax':'ajax','type':'news_primary','loginMethod':'wap','pageNo':'2'})]
   

    def parse(self,response):
        #print response.body
        for url in response.xpath('//article//a/@href').extract():
            urls = ["https://news.dyly.com",]
            url = urls[0] + url
            yield scrapy.Request(url,callback=self.parse_item)
            #yield scrapy.Request(url="https://news.dyly.com/getAppNewsList.do",meta={'ajax':'ajax','type':'news_primary','loginMethod':'wap','pageNo':'2'},callback=self.parse_item)


    def parse_item(self,response):
        item = dydlItem()
        item['title'] = response.xpath('//article//section//header/text()').extract()
        content = response.xpath('//div//p//span/text()').extract()
        if content:
            item['content'] = content   
        else:
            item['content'] = response.xpath('//div//p/text()').extract()

        
        print "===============================================" *3
        print "title:",item['title']
        print "content:",item['content']
        print "===============================================" *3
        
        yield item
