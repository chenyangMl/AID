'''
演示多线程和单线程之间效率差别.
'''

import requests
import time
from threading import Thread
from queue import Queue
import json

class XiaomiSpider():
    def __init__(self):
        self.url  = 'http://app.mi.com/categotyAllListApi?page={}&categoryId=2&pageSize=30'
        self.headers = {"User-Agent":'Mozilla/5.0'}
        #url队列
        self.url_queue = Queue()
        self.n = 0
        self.fd = open('xiaomi.json','a')

    # URL入队列
    def url_in(self):
        for i in range(67):
            url = self.url.format(i)
            #入队
            self.url_queue.put(url)

    # 线程事件函数,用于抓取数据
    def get_data(self):
        # get地址,请求+解析+保存
        while not self.url_queue.empty():
            url = self.url_queue.get()

            html = requests.get(url=url,
                                headers=self.headers).content.decode('utf-8')
            #解析JSON
            html = json.loads(html)
            app_dic = {}
            # html['data']-->[{},{},{}]
            for app in html['data']:
                app_dic['app_name'] = app['displayName']
                app_dic['app_link'] = 'http://app.mi.com/details?id=' + app['packageName']
                self.n +=1
                json.dump(app_dic,self.fd,ensure_ascii=False)

    # 主函数入口
    def main(self):
        # url入队列
        self.url_in()
        # 创建多线程来进行数据抓取
        jobs = []
        for i in range(5):
            t = Thread(target=self.get_data)
            t.start()
            jobs.append(t)

        for i in jobs:
            i.join()

        self.fd.close()
        print('应用数量:{}'.format(self.n))

if __name__ == '__main__':
    start = time.time()
    XiaomiSpider().main()
    end = time.time()
    print('执行时间:%.2f'%(end-start))