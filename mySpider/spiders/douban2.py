# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from mySpider.items import DoubanBookItem


class Douban2Spider(CrawlSpider):
    name = 'douban2'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4']

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
