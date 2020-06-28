# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.spiders import Spider#导入Spider类
from lianjia_home.items import LianjiaHomeItem  # 导入Item类
class HomeSpider(Spider):
    name = 'home'
    current_page = 1#记录当前的页数，默认为第1页
    total_page = 0#总页数
    def start_requests(self):#获取初始请求
        url = "https://su.lianjia.com/ershoufang/"
        #生成请求对象
        yield Request(url)

    def parse(self, response):#主页面解析函数
        # 1.提取主页中房屋信息
        #使用xpath定位到二手房信息的div元素，保存到列表中
        list_selecotr = response.xpath("//li/div[@class='info clear']")
        #依次遍历每个选择器，获取二手房的名称、户型、面积、朝向等数据
        for one_selecotr in list_selecotr:
            try:
                #获取房屋名称
                name = one_selecotr.xpath("div[@class='address']/"
                                          "div[@class='houseInfo']"
                                          "/a/text()").extract_first()
                #获取其他信息
                other =  one_selecotr.xpath("div[@class='address']/"
                                            "div[@class='houseInfo']"
                                            "/text()").extract_first()
                #以|作为间隔,转换为列表
                other_list = other.split("|")
                type = other_list[1].strip(" ")#户型
                area = other_list[2].strip(" ")#面积
                direction = other_list[3].strip(" ")#朝向
                fitment = other_list[4].strip(" ")#是否装修
                #有无电梯（由于网站结构经常变换，此处无法获取到该项的内容,可以到详细页中获取）。
                #elevator = other_list[5].strip(" ")

                #获取总价和单价，存入列表中
                price_list = one_selecotr.xpath("div[@class='priceInfo']//span/text()")
                # 总价
                total_price = price_list[0].extract()
                # 单价
                unit_price = price_list[1].extract()
                item = LianjiaHomeItem()#生成LianjiaHomeItem对象
                #将已经获取的字段保存于item对象中
                item["name"] = name.strip(" ")     #名称
                item["type"] = type                #户型
                item["area"] = area                #面积
                item["direction"] = direction     #朝向
                item["fitment"] = fitment         #是否装修
                #item["elevator"] = elevator       #有无电梯
                item["total_price"] = total_price#总价
                item["unit_price"] = unit_price  #单价
                # 2.获取详细页URL
                url = one_selecotr.xpath("div[@class='title']/a/@href").extract_first()
                #3.生成详细页的请求对象
                yield Request(url,
                              meta={"item":item},
                              callback=self.property_parse)
            except:
                print("error")
                pass
        #4.获取下一页URL，并生成Request请求
        #（1）获取下一页URL。仅在解析第一页时获取总页数的值
        if self.current_page == 1:
            #属性page-data的值中包含总页数和当前页。
            self.total_page = response.xpath("//div[@class='page-box house-lst-page-box']"
                                             "//@page-data").re("\d+")
            #获取总页数
            self.total_page = int(self.total_page[0])
        self.current_page+=1#下一页的值
        if self.current_page<=100: #self.total_page:#判断页数是否已越界
            next_url = "https://su.lianjia.com/ershoufang/pg%d"%(self.current_page)
            #（2）根据URL生成Request，使用yield提交给引擎
            yield Request(next_url)

    #详细页解析函数
    def property_parse(self,response):
        #1.提取房屋产权信息
        property = response.xpath("//div[@class='base']/div[@class='content']/ul/li[last()]/text()").extract_first()
        #2.获取主页面中的房屋信息
        item = response.meta["item"]
        #3.将产权信息添加到item中，返回给引擎
        item["property"] = property
        #配备电梯
        elevator= response.xpath("//div[@class='base']/div[@class='content']/ul/li[last()-1]/text()").extract_first()
        item["elevator"]=elevator
        yield item