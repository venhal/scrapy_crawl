#导入包
import requests

#抓取index页面
r = requests.get("http://www.baidu.com")

#下载打印到的内容
print(r.text)