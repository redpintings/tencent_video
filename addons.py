#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-13 14:36
# @Author  : ysl
# @Site    : 
# @File    : addons.py
# @Software: PyCharm

import mitmproxy.http
from mitmproxy import ctx


class Counter(object):
    def __init__(self):
        self.num = 0
        self.url_list = list()

    def request(self, flow: mitmproxy.http.HTTPFlow):
        if 'http://v.weishi.qq.com/shg' in flow.request.pretty_url:
            print('+'*20)
            u = flow.request.pretty_url
            print('+'*20)
            with open('u_list.txt', 'a') as f:
                f.write(str(u) + '\n')


addons = [
    Counter()
]