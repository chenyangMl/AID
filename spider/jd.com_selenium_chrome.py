"""
1、打开京东，到商品搜索页
2、匹配所有商品节点对象列表
3、把节点对象的文本内容取出来，查看规律，是否有更好的处理办法？
4、提取完1页后，判断如果不是最后1页，则点击下一页
   # 如何判断是否为最后1页？？？

查找节点的xpath
输入框; //*[@id="key"]
搜索按钮的xpath: //*[@id="search"]/div/div[2]/button
商品节点的xpath: //*[@id="J_goodsList"]/ul/li


"""
from selenium import webdriver
import time

class JdSpider():
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.url = 'http://www.jd.com'
        self.n = 0


    #获取商品页面
    def get_page(self):
        # 打开京东
        self.browser.get(self.url)
        #获取输入框节点,和搜索框按钮
        self.browser.find_element_by_xpath('//*[@id="key"]').send_keys('手机')
        self.browser.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
        # 流出时间给页面加载,这里指打开页面时的加载,不包括滚动滑轮动态加载.
        time.sleep(2)

    #解析页面
    def parse_page(self):
        # 1: 实现滑轮的滚动加载
        # 将滚动条从开始位置，滑动到页面底部.
        self.browser.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)'
        )
        time.sleep(2)


        # 2: 匹配所有商品节点对象列表
        li_lists = self.browser.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
        for li in li_lists:
            info = li.text.split('\n')
            if info[0].startswith('每满'):
                price = info[1]
                name = info[2]
                number = info[3]
                market = info[4]
            elif info[0].startswith('单价'):
                price = info[3]
                name = info[4]
                number = info[5]
                market = info[6]
            elif info[0].startswith('￥') and info[1].startswith('￥'):
                price = info[0]
                name = info[2]
                number = info[3]
                market = info[4]
            else:
                price = info[0]
                name = info[1]
                number = info[2]
                market = info[3]
            self.n +=1
            print('{}>>{}>>{}>>{}'.format(price,number,market,name))


    def main(self):
        self.get_page()
        while True:
            self.parse_page()
            # 如果有下一页点击下一页
            if self.browser.page_source.find('pn-next disabled') == -1:
                self.browser.find_element_by_class_name('pn-next').click()
                # 等待页面加载
                time.sleep(2)
            else:
                break

        self.browser.quit()
        print(self.n)

if __name__ == '__main__':
    JdSpider().main()
