#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-17 09:29
# @Author  : ysl
# @Site    : 
# @File    : spider.py
# @Software: PyCharm
import requests
import json
import re


class Spider(object):

    def __init__(self):
        self.name = 'Spider 腾讯微视 '

    def __str__(self):
        return self.name
    url = "http://h5.weishi.qq.com/webapp/json/weishi/WSH5GetPlayPage?"
    headers = {
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) "
                      "Version/11.0 Mobile/15A372 Safari/604.1",
    }
    data = {
        "feedid": "{}",
        "recommendtype": 0,
        "datalvl": "all",
        "_weishi_mapExt": {}}

    @staticmethod
    def get_feed():
        """
        获取feed id
        :return:
        """
        with open('./data.txt', 'r') as f:
            content = f.readlines()
        return content

    def parse_detail(self, feed_id):
        data = {
            "feedid": feed_id,
            "recommendtype": 0,
            "datalvl": "all",
            "_weishi_mapExt": {}}
        resp = requests.post(self.url, data=data).json()
        if resp:
            data = resp.get('data').get('feeds')
            for dt in data:
                item = dict()
                item['content'] = dt.get('feed_desc_withat')
                item['feed_id'] = dt.get('id')
                item['material_desc'] = dt.get('material_desc')
                item['playNum'] = dt.get('playNum')
                item['like'] = dt.get('ding_count')
                item['video_url'] = dt.get('video_url')
                print(item)

    def main(self):
        cont = self.get_feed()
        for con in cont:
            msg = re.findall(r'>>https://h5.weishi.qq.com/weishi/feed/(.*?)/wsfeed', con, re.S)
            msg = msg[0] if msg else None
            if msg:
                self.parse_detail(msg)


if __name__ == '__main__':
    s = Spider()
    print(s)
    s.main()
