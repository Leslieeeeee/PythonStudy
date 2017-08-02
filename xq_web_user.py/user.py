# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#!/usr/bin/python
#抓取用户名，用户背景，用户粉丝数，用户使用龄
import requests
import re
import bs4
import json
import os

start_urls = []

headers = {
    'Host': "xueqiu.com",
    'Accept-Language': "en,zh-CN;q=0.8,zh;q=0.6",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/json;charset=UTF-8",
    'Connection': "keep-alive",
    'Cookie': "s=ff11jjcikk; webp=1; remember=1; remember.sig=K4F3faYzmVuqC0iXIERCQf55g2Y; xq_is_login.sig=J3LxgPVPUzbBg3Kee_PquUfih7Q; u.sig=0PtlEgOiOEI4j8B9JhoFXLVCZn8; bid=e9a323e481ca9d25fbb151d80071ff7d_j3b6luq5; aliyungf_tc=AQAAACqJ6EQ1yAEAX4Fyyj0HVh2ahOMp; snbim_minify=true; xq_a_token=876f2519b10cea9dc131b87db2e5318e5d4ea64f; xq_a_token.sig=dfyKV8R29cG1dbHpcWXqSX6_5BE; xq_r_token=709abdc1ccb40ac956166989385ffd603ad6ab6f; xq_r_token.sig=dBkYRMW0CNWbgJ3X2wIkqMbKy1M; u=131496281493790; __utmt=1; __utma=1.1126502126.1496125809.1496125809.1496323845.2; __utmb=1.2.10.1496323845; __utmc=1; __utmz=1.1496125809.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_1db88642e346389874251b5a1eded6e3=1495775140,1495776268,1496121018,1496281457; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1496323915",
    'Referer': 'https://xueqiu.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
url =
def GetHTML(url):
    try:
        r = requests.get(url, timeout=30, headers = headers)
        r.status_code
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return print("爬取失败")