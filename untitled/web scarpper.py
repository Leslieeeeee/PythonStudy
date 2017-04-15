# -*- coding:utf-8 -*-
import os
import re
import BeautifulSoup
import Requests
'''arr = [ ]
i = 0
while ( i < 3 ) :
    arr[i] = raw_input('输入你的需求：')
keyword =arr[0]'''

keyword =

r = Requests.get('https://s.taobao.com/search?q=keyword', timeout=1)
print r.request.headers['users-agent']
headers = {'users-agent':'Chrome/55.0.2883.95'}
r = Requests.get('https://s.taobao.com/search?q=keyword', timeout=1)
print (r.status_code)
print (r.text)
r.encoding = ('GBK')
print (r.text)

