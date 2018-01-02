# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import DoubanTagItem, DoubanBookItem
import sys
import urllib
import re

reload(sys)
sys.setdefaultencoding("utf-8")


class DoubanSpider(scrapy.Spider):
    name = 'doubanTag'
    allowed_domains = ['book.douban']
    tags = []
    url_tags = []
    offset = 0
    start_urls = ['https://book.douban.com/tag/']

    # def parse_item(self, response):
    #     for each in response.xpath('//*[@class="subject-item"]'):
    #         item = DoubanBookItem()
    #         title_pub = ""
    #         star = ""
    #         introduction = ""
    #         name = each.xpath('./div[@class="info"]/h2/a/@title').extract()[0]
    #         image_url = each.xpath('./div[@class="pic"]/a/@href').extract()[0]
    #         if len(each.xpath('./div[@class="info"]/div[@class="pub"]/text()').extract()) > 0:
    #             title_pub = each.xpath('./div[@class="info"]/div[@class="pub"]/text()').extract()[0]
    #         if len(each.xpath('./div[@class="info"]/p/text()').extract()) > 0:
    #             introduction = each.xpath('./div[@class="info"]/p/text()').extract()[0]
    #         if len(each.xpath(
    #                 './div[@class="info"]/div[@class="star clearfix"]/span[@class="rating_nums"]/text()')) > 0:
    #             star = each.xpath(
    #                 './div[@class="info"]/div[@class="star clearfix"]/span[@class="rating_nums"]/text()').extract()[0]
    #
    #         # print name, detailLink, catalog, peopleNumber, workLocation,publishTime
    #
    #         item['name'] = name.encode('utf-8')
    #         item['image_url'] = image_url.encode('utf-8')
    #         item['title_pub'] = title_pub.encode('utf-8').replace(" ", "").replace("\n", "")
    #         item['introduction'] = introduction.encode('utf-8')
    #         item['star'] = star.encode('utf-8')
    #
    #         # curpageString = re.search('start=(\d+)', str(response.url)).group(1)
    #         # curpage = re.search('(\d+)', str(curpageString)).group(1)
    #         # page = int(curpage) + 20
    #         # url = re.sub('start=(\d+)', "start=" + str(page), response.url)
    #         # 发送新的url请求加入待爬队列，并调用回调函数 self.parse_item
    #         # yield scrapy.Request(url, callback=self.parse_item)
    #
    #         # 将获取的数据交给pipeline
    #         yield item

    def parse(self, response):
        tags_result = response.xpath('//*[@class="tagCol"]/tbody/tr/td/a/text()').extract()
        for each in tags_result:
            item = DoubanTagItem()
            item['name'] = str(each)
            item['tag_url'] = str(self.start_urls[0]) + (urllib.quote(str(each)))
            self.url_tags.append(item['tag_url'])
            self.tags.append(item)
            yield item

            # yield scrapy.Request(url=self.tags[self.offset], callback=self.parse_item)
