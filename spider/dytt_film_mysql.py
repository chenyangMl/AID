'''
爬取电影天堂数据,
    爬取地址： https://www.dytt8.net/html/gndy/dyzz/list_23_1.html
爬取数据保存在mysql中：
    mysql> create database dyttdb charset utf8
    mysql> create table dytt (name varchar(100), link varchar(100))

'''
from urllib import request
import re
import time,random
import pymysql

class FilmSky():
    def __init__(self):
        self.url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
        self.ua_list = [{"User-Agent": 'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) ' + \
                                       'Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10'},
                        {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) " + \
                                       "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"},
                        {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) " + \
                                       "Version/5.1.7 Safari/534.57.2"}]
        self.db = pymysql.connect(host='localhost',
                                  port=3306,
                                  user='root',
                                  passwd='123456',
                                  database='dyttdb',
                                  charset='utf8')
        self.cursor = self.db.cursor()

    #获取html函数
    def _get_page(self,url):
        req = request.Request(url=url,headers=random.choice(self.ua_list))
        response = request.urlopen(req)
        return response.read().decode('gbk','ignore')

    # 解析数据,获取名称和下载链接
    def _parse_page(self,html,flag):
        # 先解析一级页面,提取电影名称和详情链接
        # 解析二级页面，提取下载地址
        if flag == '1':
            pattern = re.compile(r'<table width="100%".*?<td height="26".*?<a href="(.*?)".*?class="ulink">(.*?)</a>',re.S)
            # film_list:[(详情连接),(电影名称)]
            film_list = pattern.findall(html)
            return film_list

        if flag == "2":
            #解析二级页面
            pattern = re.compile('<td style="WORD-WRAP.*?">.*?>(.*?)</a>')

            return pattern.findall(html)


    #保存到数据库
    def _save_data(self,data):
        sql = 'insert into dytt values (%s,%s)'
        self.cursor.executemany(sql,data)
        self.db.commit()

    # 主函数入口
    def main(self):
        start = int(input('输入起始页(1~197):'))
        end = int(input('输入起始页(1~197):'))
        print('开始爬取数据')
        for i in range(start,end):
            url = self.url.format(i)
            html = self._get_page(url)
            film_list = self._parse_page(html,flag="1")
            #
            film_info = []
            for film in film_list:

                html = self._get_page('https://www.dytt8.net'+film[0])

                film_down_link = self._parse_page(html,flag="2")
                if film_down_link and film[1]:
                    film_info.append((film[1].strip(), film_down_link[0]))

            self._save_data(film_info)
            time.sleep(random.randint(1,3))
            print('第{}页完成'.format(i))


        self.db.close()
        self.cursor.close()
        print('爬取完成')

if __name__ == '__main__':
    start = time.time()
    tt_spider = FilmSky()
    tt_spider.main()
    end = time.time()
    print('执行时间: %.2f'%(end-start))
