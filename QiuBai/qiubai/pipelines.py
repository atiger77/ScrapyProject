# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import Workbook

class QiubaiPipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['Author','Contents'])
    

    def process_item(self, item, spider):
        line = item['author']
        line2 = item['content']

        for i,j in zip(line,line2):
            self.ws.append([i,j])
            self.wb.save('qiubai.xlsx')
        return item
