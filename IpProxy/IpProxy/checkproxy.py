#coding=utf-8
 
import requests
'''
测试代理IP可用脚本，仅测试作用
'''

'''
proxies = [
   {"http":"183.78.183.156:82"},
   {"http":"180.76.154.5:8888"},
   {"http":"124.88.67.24:80"},
   {"http":"115.29.2.139:80"},
   {"http":"115.29.2.139:8011"},
   {"http":"121.204.165.80:8118"}
]
'''

proxies = [
   {'http':'183.78.183.156:82'},
   {'http':'180.76.154.5:8888'},
   {'http':'115.29.2.139:80'},
   {'http':'121.204.165.80:8118'}
]



proxypool = []

for index in range(len(proxies)):
    print proxies[index]
    try:
        result = requests.get('http://ip.cn/',proxies=proxies[index],timeout=3)
        proxypool.append(proxies[index])
    except Exception as e:
        continue

print proxypool
