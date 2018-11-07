#coding=utf-8

import urllib2
import json


'''
req = urllib2.Request('http://api.map.baidu.com/place/v2/search?query=银行&bounds=39.915,116.404,39.975,116.414&output=json&ak=key')
response = urllib2.urlopen(req) #如果不需要修改Request，直接用urlopen就可以发送get请求
the_page = response.read()
print the_page
'''





def postfunc(url):
    data = {"data": {"name": "ml0tester", "password": "123456"}}
    headers = {'Content-Type': 'application/json'}
    request = urllib2.Request(url=url, headers=headers, data=json.dumps(data))
    response = urllib2.urlopen(request)
    print response.read()

postfunc('https://my.worktile.com/api/user/signin')


req = urllib2.Request('https://www.baidu.com')
response = urllib2.urlopen(req)
print response.read()
