'''
爬取Tencent招聘信息
'''

import requests
import time
import json
import random
import csv

class TencentSpider():
    def __init__(self):
        self.headers = {'User-Agent':'Mozila/5.0'}
        self.one_url='https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1563912271089&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
        self.two_url='https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1563912374645&postId={}&language=zh-cn'

    #请求函数
    def _get_page(self,url):
        res = requests.get(url=url,headers=self.headers)
        res.encoding = 'utf-8'
        # json.loads()将响应内容转为Python数据类型
        return json.loads(res.text)

    #json数据解析,(名称,职责,要求)
    def _get_data(self,html):
        #先解析一级页面html
        job_info = {}
        jobs = []
        #在解析二级页面.
        for job in html['Data']['Posts']:
            # 职位名称
            job_info['job_name'] = job['RecruitPostName']
            #postId,拼接二级页面地址
            post_id = job['PostId']
            second_url = self.two_url.format(post_id)
            # 发请求,解析出职责和要求
            job_info['job_duty'],job_info['require']= self.parser_two_page(second_url)

            jobs.append([ job_info['job_name'],job_info['job_duty'],job_info['require']])

        self.save_csv('tencent.csv',jobs)

    def parser_two_page(self,url):
        two_html = self._get_page(url)
        duty = two_html['Data']['Responsibility']
        require = two_html['Data']['Requirement']
        return duty,require

    def save_csv(self,filename,data):
        f = open(filename,'w')
        writer = csv.writer(f)
        writer.writerows(data)
        f.close()

    #主函数入口
    def main(self):
        for index in range(1,453):
            url = self.one_url.format(index)

            html = self._get_page(url)
            self._get_data(html)
            print('===第{}页爬取完成==='.format(index))
            time.sleep(random.randint(1,2))
        print('==========所有数据爬取完成=========')

if __name__ == '__main__':
    TencentSpider().main()

