# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QidianHotItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()       #小说名称
    author = scrapy.Field()     #作者
    type = scrapy.Field()       #类型
    form = scrapy.Field()       #形式
