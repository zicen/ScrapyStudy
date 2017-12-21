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


class DoubanTagItem(scrapy.Item):
    name = scrapy.Field()
    tag_url = scrapy.Field()


class DoubanBookItem(scrapy.Item):
    name = scrapy.Field()
    image_url = scrapy.Field()
    title_pub = scrapy.Field()
    introduction = scrapy.Field()
    star = scrapy.Field()


class ZhihuItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    answer = scrapy.Field()
    name = scrapy.Field()


class DouyuspiderItem(scrapy.Item):
    name = scrapy.Field()
    imageUrls = scrapy.Field()
    imagesPath = scrapy.Field()

