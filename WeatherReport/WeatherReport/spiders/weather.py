# -*- coding: utf-8 -*-

import scrapy
import smtplib
from email.mime.text import MIMEText

class WeatherSpider(scrapy.Spider):
    name="weather"
    start_urls = [
        "http://www.weather.com.cn/weather1d/101020100.shtml",
    ]


    def parse(self,response):
        Tod_Weather_Date = response.xpath('//*[@id="today"]/div[1]/ul/li[1]/h1/text()').extract()
        Tod_Weather_Wea = response.xpath('//*[@id="today"]/div[1]/ul/li[1]/p[1]/text()').extract()
        Tod_Weather_Tem = response.xpath('//*[@id="today"]/div[1]/ul/li[1]/p[2]/span/text()').extract()
    
        Tom_Weather_Date = response.xpath('//*[@id="today"]/div[1]/ul/li[2]/h1/text()').extract()
        Tom_Weather_Wea = response.xpath('//*[@id="today"]/div[1]/ul/li[2]/p[1]/text()').extract()
        Tom_Weather_Tem = response.xpath('//*[@id="today"]/div[1]/ul/li[2]/p[2]/span/text()').extract()

        lst = ['今天日期:' + Tod_Weather_Date[0].encode('utf-8'),"\n",'今天天气情况:'+ Tod_Weather_Wea[0].encode('utf-8'),"\n",'今天温度:' + Tod_Weather_Tem[0].encode('utf-8') + '℃',"\n","\n",'明天日期:' + Tom_Weather_Date[0].encode('utf-8'),"\n",'明天天气情况:'+ Tom_Weather_Wea[0].encode('utf-8'),"\n",'明天温度:' + Tom_Weather_Tem[0].encode('utf-8') + '℃']
        
        mailto_list="liudehua@wenba100.com"
        mail_host="smtp.exmail.qq.com"
        mail_user="ldy@wenba100.com"
        mail_pass="XXXXXXXXXXXX"

        content = ''.join(lst)
	msg = MIMEText(content,_subtype='plain',_charset='utf-8')
        msg['Subject'] = "Two day's weather"
        msg['From'] = mail_user
        msg['To'] = mailto_list

        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(mail_user,mailto_list,msg.as_string())
        s.close()
