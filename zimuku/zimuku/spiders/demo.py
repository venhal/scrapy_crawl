# -*- coding: utf-8 -*-
import scrapy

from zimuku.items import ZimukuItem

class DemoSpider(scrapy.Spider):

    #爬虫的名字
    name = 'demo'

    #爬虫爬取的网页域名
    allowed_domains = ['zimuku.net']

    #爬取的url链接
    start_urls = ['http://zimuku.net/']

    def parse(self, response):

        name = response.xpath('//b/text()').extract()[1]

        items = {}
        items['第一个'] = name

        return items
