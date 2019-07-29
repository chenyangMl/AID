"""
爬取民政部数据中最新的行者区化码

url = http://www.mca.gov.cn/article/sj/xzqh/2019/
该站点使用的反爬措施为： 通过JS实现爬取地址的重定向。
"""

import pymysql
from lxml import etree
import re
import requests

class Goverment():
    def __init__(self):
        self.one_url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
        self.headers = {'User-Agent':'Mozilla/5.0'}
        self.db = pymysql.connect(host='localhost',port=3306,database='goverment',user='root',password='123456')
        self.cursor = self.db.cursor()

    # 获取二级页面连接(假链接),需要是最新更新的
    def get_false_link(self):
        html = requests.get(url=self.one_url,headers=self.headers).text
        xpath = '//a[@class="artitlelist"]'
        parser_html = etree.HTML(html)
        r_list = parser_html.xpath(xpath)
        for a in r_list:
            # title = a.xpath('./@title')[0]
            title = a.get('title')
            # print(title)
            if re.findall(r'\d+年\d+月中华人民共和国县以上行政区划代码',title):
                two_false_link = 'http://www.mca.gov.cn'+a.get('href')
                return two_false_link


    # 提取真实二级页面链接
    def get_true_link(self, link):

        html = requests.get(url=link, headers=self.headers).text
        link = re.findall('window.location.href="(.*?)"',html,re.S)[0]
        sql = "select * from version where link='%s' "%link
        self.cursor.execute(sql)
        # 不为空元组
        if self.cursor.fetchall():
            print('数据已是最新')
        else:
            print('开始抓取数据')
            self.get_data(link)
            #把更新的link插入到version表中
            ins = 'insert into version values (%s)'
            self.cursor.execute(ins,[link])
            self.db.commit()



    #真正提取数据函数
    def get_data(self,link):
        html = requests.get(url=link,headers=self.headers).text
        #基准xpath
        parse_html = etree.HTML(html)
        r_lists= parse_html.xpath('//tr[@height="19"]')
        for info in r_lists:
            code = info.xpath('./td[2]/text()')[0]
            name = info.xpath('./td[3]/text()')[0]
            print(code,name)

    # 主函数
    def main(self):
        false_link = self.get_false_link()
        self.get_true_link(false_link)

if __name__ == '__main__':
    Goverment().main()




