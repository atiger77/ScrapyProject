# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests

class IpproxyPipeline(object):
    def process_item(self, item, spider):

        proxy_ip = item['proxy_ipaddr']
        proxy_port = item['proxy_port']
        proxypool = []

        for i,j in zip(proxy_ip,proxy_port):
            proxies = [
                {"http":"%s:%s" %(i,j)}
            ]    
            
            for index in range(len(proxies)):
                print proxies[index]
            try:
                result = requests.get('http://ip.cn/',proxies=proxies[index],timeout=3)
                proxypool.append(proxies[index])
            except Exception as e:
                print e
        print "---" * 10
        print proxypool
            
        return item
