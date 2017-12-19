# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ItcastItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()


class TencentItem(scrapy.Item):
    name = scrapy.Field()
    detailLink = scrapy.Field()
    positionInfo = scrapy.Field()
    peopleNumber = scrapy.Field()
    workLocation = scrapy.Field()
    publishTime = scrapy.Field()


class DoubanBookItem(scrapy.Item):
    name = scrapy.Field()
    book_name = scrapy.Field()
    image_url = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    press = scrapy.Field()
    press_time = scrapy.Field()
    price = scrapy.Field()
    translater = scrapy.Field()
    introduction = scrapy.Field()
    star = scrapy.Field()
