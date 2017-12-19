# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import DoubanBookItem
import sys
import urllib
import urllib2
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['book.douban']
    start_urls = ['https://book.douban.com/tag/?view=type&icn=index-sorttags-all']

    def parse(self, response):
        tags = []
        tags_result = response.xpath('//*[@class="tagCol"]')
        for tag in tags_result:




