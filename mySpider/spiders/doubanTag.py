# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import DoubanTagItem
import sys
import urllib

reload(sys)
sys.setdefaultencoding("utf-8")


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['book.douban']
    start_urls = ['https://book.douban.com/tag/']

    def parse(self, response):
        tags = []
        tags_result = response.xpath('//*[@class="tagCol"]/tbody/tr/td/a/text()').extract()
        for each in tags_result:
            item = DoubanTagItem()
            item['name'] = str(each)
            item['tag_url'] = str(self.start_urls[0]) + (urllib.quote(str(each)))
            tags.append(item)
        return tags
