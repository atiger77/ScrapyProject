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


    rules = (
        Rule(LinkExtractor(allow=('http://jandan.net/ooxx/page-\d+#comments', )), callback='parse_item', follow=True),
    )


    def parse_item(self, response):
        for href in response.xpath('//a[@class="view_img_link"]/@href').extract():
            pic_url = "http:" + href
            item = JandanItem(image_urls=[pic_url])
            yield item



