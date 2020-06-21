# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaHomeItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field() #名称
    type = scrapy.Field() #户型
    area = scrapy.Field() #面积
    direction = scrapy.Field() #朝向
    price = scrapy.Field() #价格
    floor = scrapy.Field() #楼层
    elevator = scrapy.Field() #电梯
    status = scrapy.Field() #状态
    pass
