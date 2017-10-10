#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import jieba
import logging
import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

txt_file = open("freebuf_vuls_titles.txt", "r")
jieba.load_userdict("THUOCL_it.txt")

hive = {}
blacklist = [u'漏洞', u'的', u'）', u'（', u'分析', u'_', u'-', u'：', u'，', u'可', u'被', u'“', u'”', u'利用', u'曝', u'影响', u'攻击', u'2016',
             u'、', u'？', u'2015', u'如何', u'修复', u'和', u'中']

with open("freebuf_vuls_titles.txt", "r") as txt_file:
    for line in txt_file:
        for word in jieba.cut(line):
            if word in blacklist:
                continue
            hive[word] = hive.get(word, 0) + 1

hive_sorted = sorted(hive.iteritems(), key=lambda d: d[1], reverse=True)

for i in range(0, 10):
    print hive_sorted[i][0]