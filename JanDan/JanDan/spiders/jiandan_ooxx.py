# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from JanDan.items import JandanItem

class JandanSpider(CrawlSpider):
    name = "JanDan"
    allowed_domains = ["jandan.net"]
    start_urls = [
        "http://jandan.net/ooxx",
    ]

'''
使用CrawlSpider方法scrapy自行深入爬区，page页数使用正则进行数字匹配
爬取的图片地址加上“http:”进行后续下载

'''
    rules = (
        Rule(LinkExtractor(allow=('http://jandan.net/ooxx/page-\d+#comments', )), callback='parse_item', follow=True),
    )


    def parse_item(self, response):
        for href in response.xpath('//a[@class="view_img_link"]/@href').extract():
            pic_url = "http:" + href
            item = JandanItem(image_urls=[pic_url])
            yield item
