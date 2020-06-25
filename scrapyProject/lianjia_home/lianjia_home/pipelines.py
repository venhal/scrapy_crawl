# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import re #正则表达式模块
from scrapy.exceptions import DropItem
class FilterPipeline(object):
    def process_item(self, item, spider):
        #总面积，提取数字
        item["area"]=re.findall(r"\d+\.?\d*",item["area"])[0]
        #单价，提取数字
        item["unit_price"]=re.findall(r"\d+\.?\d*",item["unit_price"])[0]
        #产权，提取数字
        item["property"]=re.findall(r"\d+\.?\d*",item["property"])[0]
        #如果字段房屋朝向缺少数据，则抛弃该条数据
        item["direction"]=="暂无数据":
            #抛弃缺少数据的Item项
            rasie DropItem("房屋朝向无数据，抛弃此项目：%s"%item)
        return item
