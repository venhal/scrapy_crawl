#导入模块
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')
#输出结果
print(soup.prettify())
