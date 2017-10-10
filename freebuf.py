#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import jieba
import logging
import urllib

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

url = 'http://www.freebuf.com/vuls/'
webpage = urllib.urlopen('http://www.freebuf.com/vuls/').read()
soup = BeautifulSoup(webpage, "html5lib")
news_list = soup.find_all('div', {'class': 'news-info'})
news_title_list = []
for news in news_list:
    news_title = news.a.get('title')
    print news_title
    news_title_list.append(news_title)


