# -*- coding: utf-8 -*-
#
import scrapy
import json

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
        response_html =  response.body
        result = json.loads(response_html)
        result_newsid = result['newsContent']
        urls = ["https://news.dyly.com/news/detail/",]
        for i in  result_newsid:
            url = urls[0] + i['objectId'] + ".html"
            yield scrapy.Request(url,callback=self.parse_item)

    def parse_item(self,response):
        item = dydlItem()
        item['title'] = response.xpath('//article//section//header/text()').extract()
        content = response.xpath('//div//p//span/text()').extract()
        if content:
            item['content'] = content   
        else:
            item['content'] = response.xpath('//div//p/text()').extract()

        '''
        print "===============================================" *3
        print "title:",item['title']
        print "content:",item['content']
        print "===============================================" *3
        '''
        yield item
