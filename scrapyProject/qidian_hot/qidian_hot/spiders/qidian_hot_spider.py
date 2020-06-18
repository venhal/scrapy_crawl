#-*-coding:utf-8-*-
from scrapy import Request
from scrapy.spiders import Spider
class HotSalesSpider(Spider):
    #定义爬虫名称
    name = 'hot'
    #起始的URL列表
    start_urls = ["https://www.qidian.com/rank/hotsales?style=1"]
    #解析函数
    def parse(self, response):
        #使用xpath定位到小说内容的div元素
        list_selector = response.xpath("//div[@class='book-mid-info']")
        #依次读取每部小说的元素，从中获取名称、作者、类型和形式
        for one_selector in list_selector:
            #获取小说名称
            name = one_selector.xpath("h4/a/text()").extract()[0]
            #获取作者
            author = one_selector.xpath("p[1]/a[1]/text()").extract()[0]
            #获取类型
            type = one_selector.xpath("p[1]/a[2]/text()").extract()[0]
            #获取形式（连载/完本）
            form = one_selector.xpath("p[1]/span/text()").extract()[0]
            #将爬取到的一部小说保存到字典中
            hot_dict = {"name":name,   #小说名称
                     "author":author,  #作者
                     "type":type,      #类型
                     "form":form}      #形式
            #使用yield返回字典
            yield hot_dict