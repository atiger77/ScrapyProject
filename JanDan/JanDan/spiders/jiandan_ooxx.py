# -*- coding: utf-8 -*-
import scrapy
from rosioo.items import RosiooItem

class RosiokSpider(scrapy.Spider):
    name = "rosiok"
    allowed_domains = ["rosiok.com"]
    start_urls = (
        'http://jandan.net/ooxx/',
    )

