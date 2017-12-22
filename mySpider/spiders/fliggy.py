# -*- coding: utf-8 -*-
import scrapy


class FliggySpider(scrapy.Spider):
    name = 'fliggy'
    allowed_domains = ['sjipiao.fliggy.com']

    def __init__(self, acity=None, dcity=None, date=None):
        super(FliggySpider, self).__init__()
        start_urls = [
            'https://sjipiao.fliggy.com/flight_search_result.htm?depCity=%s&arrCity=%s&depDate=%s' % (dcity, acity, date)
        ]

    def parse(self, response):
        print response.body()
