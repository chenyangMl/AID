'''
简介：
    爬取猫眼电影toop100榜单电影名，主演，上映时间，写入到CSV中

    爬取路由： url = https://maoyan.com/board/4?offset=0

        路由规律 offst = 0,10,20,30,40....
date: 2019-07-18
author: ANTCODE
'''
from urllib import request
import time,random
import re
import csv

class MaoyanSpider():
    def __init__(self,url):
        self.url = url
        self.ua_list = [{"User-Agent":'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) '+\
                                      'Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10'},
                        {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) " + \
                                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"},
                        {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) "+\
                                      "Version/5.1.7 Safari/534.57.2"}]


    # 获取响应
    def _get_page(self,url):
        req = request.Request(url=url,headers=random.choice(self.ua_list))
        response = request.urlopen(req)
        return response.read().decode('utf-8')

    # 解析数据
    def _parse_page(self,html):
         regx =r'.*?title="(.*?)".*?主演(.*?)\n.*?class="releasetime">上映时间：(\d+-*\d*-*\d*).*?</p>'
         pattern = re.compile(regx,re.S)
         return re.findall(pattern,html)

    # 保存数据
    def _write_page(self,filename, data):
        f = open(filename,'a+',newline='')
        writer = csv.writer(f)
        movies = []
        for m in data:

            movies.append((m[0],m[1][1:],m[2]))
        writer.writerows(movies)
        f.close()


    def main(self):
        start = 1
        end = 10
        filename = '猫眼toop100榜单信息.csv'
        for i in range(start,end+1):
            offset = (i-1)*10
            url = self.url.format(offset)
            html = self._get_page(url)
            data = self._parse_page(html)
            self._write_page(filename,data)
            print('第{}页已经爬取完成'.format(i))
            time.sleep(random.randint(1,3))


if __name__ == '__main__':
    url = 'https://maoyan.com/board/4?offset={}'
    start = time.time()
    spider = MaoyanSpider(url)
    spider.main()
    end = time.time()
    print('执行时间: %.2f'%(end-start))