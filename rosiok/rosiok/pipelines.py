# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

class RosiooPipeline(ImagesPipeline):
    def get_media_requests(self, item, spider):
        for image_url in item['img_url']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, spider):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return results


