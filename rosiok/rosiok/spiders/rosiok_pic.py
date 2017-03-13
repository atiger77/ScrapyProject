# -*- coding: utf-8 -*-
import scrapy
from rosioo.items import RosiooItem

class RosiokSpider(scrapy.Spider):
    name = "rosiok"
    allowed_domains = ["rosiok.com"]
    start_urls = (
        'http://www.rosiok.com/x/list_1_1.html',
    )

    def parse2(self,response):
        for i in response.xpath('//div[@class="photo"]'):
            item = RosiooItem()
            item['img_url'] = i.xpath('img/@src').extract()
            yield item

    def parse(self, response):

        urls = response.xpath('//*[@id="imgBox"]/li/a/@href').extract()
        if urls:
            for url in urls:
                yield scrapy.Request(url=r"http://www.rosiok.com"+url, callback=self.parse2)

        next_page = response.xpath('//*[@class="cPage"]/li[last()]/a/@href') # next page
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)

