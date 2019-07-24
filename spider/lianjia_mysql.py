'''
爬取链家二手房房源信息
    URL: https://bj.lianjia.com/ershoufang/pg2/
    爬取数据：
数据库
    db: lianjiadb
    table: lianjia_info
date: 2019-07-20
© ANTCODE
'''
import time
import random
import re
import requests
import pymysql


class DyttSpider():
    def __init__(self):
        self.url = 'https://m.lianjia.com/bj/ershoufang/pg{}/'
        self.ua_list = [{"User-Agent": 'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) ' + \
                                       'Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10'},
                        {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) " + \
                                       "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"},
                        {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) " + \
                                       "Version/5.1.7 Safari/534.57.2"}]
        self.db = pymysql.connect(host='localhost',port=3306,user='root',
                                  password='123456',charset='utf8',database='lianjiadb')
        self.cursor = self.db.cursor()

    # 获取响应内容
    def _get_page(self,url):
        html = requests.get(url=url, headers=random.choice(self.ua_list)).text
        return html

    # 解析数据
    def _parse_page(self,html):
        regx = r'class="item_other.*?>(.*?)</div>.*?<em>(.*?)</em>.*?class="unit_price">(.*?)</span>'
        pattern = re.compile(regx,re.S)
        data = pattern.findall(html)
        # [('2室1厅/58.5m²/南 北/进步巷', '605', '103419元/平'), ('3室2厅/114.66m²/南 北/运乔嘉园', '500', '43608元/平')]
        # 插入数据库格式：  [[名字，户型,方位,大小，单价,总价],[...]]
        result = []
        for i in data:
            temp = i[0].split('/')
            # name,rtype,location,size = temp[3],temp[0],temp[2],temp[1]
            result.append([ temp[3],temp[0],temp[2],temp[1],i[2],i[1]+'万'])
        return result

    # 保存数据
    def _save_data(self,data):

        sql = 'insert into lianjia_info values (%s,%s,%s,%s,%s,%s)'
        try:
            self.cursor.executemany(sql,data)
            self.db.commit()
        except Exception:
            self.db.rollback()

    # 主程序入口
    def main(self):
        for i in range(2,101):
            url = self.url.format(i)
            html = self._get_page(url)
            data = self._parse_page(html)
            self._save_data(data)
            print('第{}页爬取完成'.format(i))
        print('爬取完所有数据')


if __name__ == '__main__':
    spider = DyttSpider()
    spider.main()

