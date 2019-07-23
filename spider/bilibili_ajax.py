'''
    获取B站动态的视频:
    爬取地址: http://vc.bilibili.com/p/eden/rank#/tag=全部

    Ajax地址： http://api.vc.bilibili.com/board/v1/ranking/top?page_size=10&next_offset=&tag=%E4%BB%8A%E6%97%A5%E7%83%AD%E9%97%A8&platform=pc
'''

import requests
import os

class BiLiVideo():
    def __init__(self):
        self.url = 'http://api.vc.bilibili.com/board/v1/ranking/top?page_size={}&next_offset=&tag=%E4%BB%8A%E6%97%A5%E7%83%AD%E9%97%A8&platform=pc'
        self.headers = {
            "Accept": 'application/json, text/plain, */*',
            "Origin": 'http://vc.bilibili.com',
            "Referer": 'http://vc.bilibili.com/p/eden/rank',
            "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
        }

    def _get_json(self,url):
        return requests.get(url=url,
                            headers=self.headers).json()

    def _get_video_links(self,jsonStr):

        for items in jsonStr['data']['items']:
            vlink = items['item']['video_playurl']
            self._save_video(vlink)

    def _save_video(self,link):

        res = requests.get(url=link,headers=self.headers).content
        filename = link[-8:]+'.mp4'
        directory = '/home/tarena/project/Fourth/1_Spider/spider_day04_note/videos/'
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(directory+filename,'wb') as f:
            f.write(res)
            print('已经保存视频{}'.format(filename))

    def main(self):
        page_size = input('请输入要爬取B站小视频数量:')
        url = self.url.format(page_size)
        jsonStr = self._get_json(url)
        self._get_video_links(jsonStr)

if __name__ == '__main__':
    BiLiVideo().main()