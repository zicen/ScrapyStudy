# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from mySpider.items import DoubanBookItem
import json


# 使用另一种方式crawlSpider的方式去爬取豆瓣小说的book信息,filename = douban2.json
class Douban2Spider(CrawlSpider):
    name = 'douban2'
    allowed_domains = ['douban.com']
    offset = 0
    # from tag file read a list
    url_list = []
    f = open("doubantag.json", 'r')
    alljson = json.load(f)
    for each in alljson:
        url = each['tag_url']
        url_list.append(url)
    start_urls = url_list
    page_lx = LinkExtractor(allow=('start=\d+'))
    rules = (
        Rule(page_lx, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        for each in response.xpath('//*[@class="subject-item"]'):
            title_pub = ""
            star = ""
            introduction = ""
            name = each.xpath('./div[@class="info"]/h2/a/@title').extract()[0]
            image_url = each.xpath('./div[@class="pic"]/a/@href').extract()[0]
            if len(each.xpath('./div[@class="info"]/div[@class="pub"]/text()').extract()) > 0:
                title_pub = each.xpath('./div[@class="info"]/div[@class="pub"]/text()').extract()[0]
            if len(each.xpath('./div[@class="info"]/p/text()').extract()) > 0:
                introduction = each.xpath('./div[@class="info"]/p/text()').extract()[0]
            if len(each.xpath(
                    './div[@class="info"]/div[@class="star clearfix"]/span[@class="rating_nums"]/text()')) > 0:
                star = each.xpath(
                    './div[@class="info"]/div[@class="star clearfix"]/span[@class="rating_nums"]/text()').extract()[0]
            # print name, detailLink, catalog, peopleNumber, workLocation,publishTime
            item = DoubanBookItem()
            item['name'] = name.encode('utf-8')
            item['image_url'] = image_url.encode('utf-8')
            item['title_pub'] = title_pub.encode('utf-8').replace(" ", "").replace("\n", "")
            item['introduction'] = introduction.encode('utf-8')
            item['star'] = star.encode('utf-8')
            yield item
