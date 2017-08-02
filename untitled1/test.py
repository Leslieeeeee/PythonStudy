# -*- coding: utf-8 -*-
# !/usr/bin/python
"""
Spyder Editor

This is a temporary script file.
"""

# 抓取用户名，用户背景，用户粉丝数，用户使用龄
import requests
import re
import bs4
import json
import os

headers = {
    'Host': "xueqiu.com",
    'Accept-Language': "en,zh-CN;q=0.8,zh;q=0.6",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/json;charset=UTF-8",
    'Connection': "keep-alive",
    'Cookie': "s=eu117etaa8; device_id=3610b97cf70102885b289bf37db37b9f; bid=e9a323e481ca9d25fbb151d80071ff7d_j4js6s57; Hm_lvt_63c1867417313f92f41e54d6ef61187d=1498822597; aliyungf_tc=AQAAANnkrU+IEAQApJNgtnM3aaXtZzFX; snbim_minify=true; xq_a_token=0a52c567442f1fdd8b09c27e0abb26438e274a7e; xq_a_token.sig=dR_XY4cJjuYM6ujKxH735NKcOpw; xq_r_token=43c6fed2d6b5cc8bc38cc9694c6c1cf121d38471; xq_r_token.sig=8d4jOYdZXEWqSBXOB9N5KuMMZq8; u=371499308556711; __utmt=1; Hm_lvt_1db88642e346389874251b5a1eded6e3=1498549773,1498549780,1498812257,1499307901; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1499309150; __utma=1.99999208.1498822017.1499060218.1499307901.3; __utmb=1.8.10.1499307901; __utmc=1; __utmz=1.1498822017.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
    'Referer': "https://xueqiu.com/5964068708",
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}


def GetHTML(url):
    if url is None:
        return None

    try:
        i = 1
        while i < 22368:
            url = "https://xueqiu.com/friendships/followers.json?pageNo=" + str(i) + "&uid=5964068708"
            r = requests.get(url, timeout=30, headers=headers)
            r.status_code
            r.encoding = r.apparent_encoding
            i = i + 1
            # print(r.text)
            return r.text
    except:
        return print("爬取失败")


def GetFollowers(html):
    try:
        for fans in json.loads(html)["followers"]:
            if fans["followers_count"] > 20000 and fans["profile"] not in name_list:
                name_list.append(fans["id"])
                print(name_list)

                file = open('leslieeeeee/Downloads/xueqiu_user.rtf', 'w', encoding='gbk')
                file.write(str(fans["screen_name"]) + "," + str(fans["followers_count"]) + "," + str(fans["id"]) + "\n")
                file.close()

                if fans["followers_count"] < 20000:
                    num = 20000
                else:

                    num = fans["followers_count"]

                for page_id in range(1, num):
                    url = "https://xueqiu.com/friendships/followers.json?pageNo=" + str(page_id) + "&uid=" + str(
                        fans["id"])[1:]
                yield Request(url, callback=self.GetFollowers, headers=headers)
    except:
        print("解析失败！，请重试或检查！")


def main():
    name_list = []
    html = GetHTML(url)


main()