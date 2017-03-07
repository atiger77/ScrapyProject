# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import Workbook

class DylyPipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['Titles','Contents'])
    

    def process_item(self, item, spider):
        line = item['title']
        line2 = item['content']

        for i,j in zip(line,line2):
            self.ws.append([i,j])
            self.wb.save('dyly.xlsx')
        return item
  
