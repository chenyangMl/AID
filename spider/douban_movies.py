import requests

class DouBan():
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90&action=&start=0&limit={}'
        self.headers = {
            "Accept": '*/*',
            # 慎用，
            # "Accept-Encoding": 'gzip, deflate, br',
            "Accept-Language": 'zh-CN,zh;q=0.9',
            "Connection": 'keep-alive',
            "Cookie": 'viewed="25910559"; bid=x8ZG52Nac2Y; gr_user_id=bcaadbac-06ae-4825-bfbc-3154e624d0e0; __utmc=30149280; _vwo_uuid_v2=D4EC681D578309EA0F62C25AE1151A0F3|b3a2ce5c0dbdff55ef99a4d6a0604d54; ll="108288"; ap_v=0,6.0; __utma=30149280.2044314746.1563452941.1563452941.1563871909.2; __utmb=30149280.0.10.1563871909; __utmz=30149280.1563871909.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.494834535.1563871909.1563871909.1563871909.1; __utmb=223695111.0.10.1563871909; __utmc=223695111; __utmz=223695111.1563871909.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1563871909%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DcgCmAHnDQOvj_V3eHb-Oye4t_2TUnQBnn58fs_LGTzZ74D6jNIISi8C9VHkVnzBq%26wd%3D%26eqid%3Df3a1b55400047aec000000065d36c917%22%5D; _pk_ses.100001.4cf6=*; __yadk_uid=4ZNND2iRFdLshRtfB9N1OJ7SiLYCJyUo; _pk_id.100001.4cf6=920f1d9f8f138e54.1563871909.1.1563872954.1563871909.',
            "Host": 'movie.douban.com',
            "Referer": 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=',
            "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
            "X-Requested-With": 'XMLHttpRequest',
        }

    #请求+解析
    def get_film_info(self,url):
        # html_json: [{},{}]
        html_json = requests.get(url=url,
                                 headers = self.headers).json()
        #遍历获取每个电影信息
        n=0
        for film in html_json:
            name = film['title']
            score = film['score']
            n+=1

            print(name, score)
        print('爬取了{}个数据'.format(n))
    def main(self):
        while True:
            types = {'剧情':'11','喜剧':"24",'爱情':'13','动作':'5','科幻':'17','动画':'25',
                     '悬疑':'10','惊悚':'19','恐怖':'20','记录片':'1','短片':'23','情色':'6',
                     '同性':'26','音乐':'14','歌舞':'7','家庭':'28','儿童':'8','传记':'2','历史':'4','战争':'22',
                     '犯罪':'3','西部':'27','奇幻':'16','冒险':'15','灾难':'12','武侠':'29','古装':'30','运动':'18'}
            print('''
                ==============电影类型=================
                剧情| 喜剧| 动作| 爱情| 科幻| 动画| 悬疑|
                惊悚| 恐怖| 纪录片| 短片| 情色| 同性| 音乐|
                歌舞| 家庭| 儿童| 传记| 历史| 战争| 犯罪|
                西部| 奇幻| 冒险| 灾难| 武侠| 古装| 运动|
            ''')

            file_type = input('请输入电影类型名>>')
            if file_type not in types:
                print('!!!未知电影类型!!!\n')
                continue
            type_id = types[file_type]
            limit = input('获取电影数量>>')
            url = self.url.format(type_id,limit)
            self.get_film_info(url)


if __name__ == '__main__':
    DouBan().main()