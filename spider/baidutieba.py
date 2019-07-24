'''
爬取百度贴吧指定吧名的内容:
    1:用户通过输入 吧名 实现指定贴吧内容的抓取
    2: 抓取内容主要包括: 吧内的图片和视频。

    地址； http://tieba.baidu.com/f?kw={}&pn={}
'''

import requests
from urllib import parse
from lxml import etree
import random
import time
import os

class BaiduImageSpider():
    def __init__(self):

        self.ua_list = [{"User-Agent":'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)'},
                        ]

    # requests请求
    def _get_page(self,url):

        html = requests.get(url=url,
                            headers=random.choice(self.ua_list)
                            ).content.decode('utf-8')
        return html



    # lxml解析html
    def _get_parse_page(self,html,xpath):
        parse_html = etree.HTML(html)
        result = parse_html.xpath(xpath)
        return result



    # 获取吧内所有帖子链接
    def get_tlink(self,url):
        html = self._get_page(url=url)
        # print(html)
        # 提取帖子链接
        xpath = '//*[@id="thread_list"]/li[@class=" j_thread_list clearfix"]/div/div[2]/div[1]/div[1]/a/@href'
        #t_list: ['/p/23232', '/p/232323']
        t_list = self._get_parse_page(html,xpath)
        for t in t_list:
            t_link = 'http://tieba.baidu.com'+t
            # 把这个帖子中所有图片保存到本地
            self._write_image(t_link)


    def _write_image(self,url):
        #保存每个帖子中的图片到本地
        html = requests.get(url=url,
                            headers=random.choice(self.ua_list)).content.decode('utf-8')
        # parse_html = etree.HTML(html)

        # img_list: ['https://xxx.jpg']
        img_xpath = '//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src'
        video_xpath = '//div[@class="video_src_wrapper"]/embed/@data-video'
        # img_list = parse_html.xpath(img_xpath+'|'+video_xpath)
        img_video_list = self._get_parse_page(html,img_xpath+'|'+video_xpath)

        for img_link in img_video_list:
            html = requests.get(url=img_link,
                                headers=random.choice(self.ua_list)).content
            filename = img_link[-10:]
            if not os.path.exists('./images/'):
                os.mkdir('./images/')
            with open('./images/'+filename,'wb') as f:
                f.write(html)
                print('{}下载成功'.format(filename))
            time.sleep(random.randint(1,3))

    def main(self):
        # 1获取用户输入的吧名
        name = input('请输入需要抓取的百度贴吧名: ')
        try:
            start = int(input('输入起始页:'))

        except ValueError:
            print('请重新输入起始页!!!!')
            start = int(input('输入起始页:'))
        try:
            end = int(input('输入终止页: '))
        except ValueError:
            print('请重新输入终止页')
            end = int(input('输入终止页: '))

        # 进入指定贴吧
        for i in range(start, end+1):
            pn = (i-1)*50
            url = 'http://tieba.baidu.com/f?kw={}&pn={}'.format(parse.quote(name),pn)
            self.get_tlink(url)
            print('第{}页抓取成功'.format(i))


if __name__ == '__main__':

    BaiduImageSpider().main()