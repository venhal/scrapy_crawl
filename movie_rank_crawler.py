'''对电影网站http://dianying.2345.com/top/ 中的电影名字、主演、简介、标题图进行爬取'''
import requests
import bs4

def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status
        r.encoding = 'gbk'
        return r.text
    except:
        return "something wrong!"

def get_content(url):
    html = get_html(url)
    soup = bs4.BeautifulSoup(html, 'html.parser')

    #找到电影排行的对应列表
    movies_list = soup.find('ul', class_ = 'picList clearfix')
    movies = movies_list.find_all('li')

    for top in movies:
        #找到图片链接
        img_url=top.find('img')['src']
        name = top.find('span', class_ = 'sTit').a.text
        #防止无上映时间出现时的异常捕获
        try:
            time = top.find('span', class_= 'sIntro').text
        except:
            time = '暂无上映时间'
        
        #找出“pACtor”中的所有子孙节点，解决名字分割问题
        actors = top.find('p', class_= 'pActor')
        actor=''
        for act in actors.contents:
            actor = actor + act.string+''
        #找出影片介绍
        intro = top.find('p', class_='pTxt pIntroShow').text

        print("片名：{}\t{}\n{}\n{} \n \n ".format(name, time, actor, intro))

        #下载图片
        with open('C:\\Users\\lwh95\\OneDrive\\Python\\web_crawler\\movie_img\\'+name+'.png', 'wb+') as f:
            f.write(requests.get("http:"+img_url.split("jpg")[-2]+"jpg").content)

def main():
    url = 'http://dianying.2345.com/top/'
    get_content(url)

if __name__ == "__main__":
    main()