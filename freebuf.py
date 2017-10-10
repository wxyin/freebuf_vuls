#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import jieba
import logging
import requests
import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
page_count = 100
base_url = 'http://www.freebuf.com/vuls/'
headers = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
news_title = []
txt_file = open("freebuf_vuls_titles.txt", "w+")

def page_news_title(page_number):
    page_url = base_url + "page/" + str(page_number)
    print page_url
    webpage = requests.get(page_url, headers = headers).text
    soup = BeautifulSoup(webpage, "html5lib")
    news_list = soup.find_all('div', {'class': 'news-info'})
    news_title_list = []
    for news in news_list:
        news_title = news.a.get('title')
        print news_title
        news_title_list.append(news_title)
    return news_title_list

for page_number in range(0, page_count):
    page_number = page_number + 1
    print "This is page " + str(page_number)
    page_news_title_list = page_news_title(page_number)
    news_title = news_title + page_news_title_list
    for title in page_news_title_list:
        title = title +"\n"
        txt_file.write(title.encode('utf8'))

txt_file.close()