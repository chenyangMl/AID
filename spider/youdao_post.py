'''
模拟有道的post请求向有道服务器进行请求
'''
import requests
import time
import random
import hashlib

#获取salt sign ts
def get_salt_sigin_ts(word):
    ts =  str(int(time.time()*1000))
    salt = ts + str(random.randint(0, 9))

    s = hashlib.md5()
    string = ("fanyideskweb" + word + salt + "n%A-rKaT5fb[Gy?;N5@Tj").encode()
    s.update(string)
    sign = s.hexdigest()
    return salt,ts,sign

#模拟有道翻译功能
def attack_yd(word):
    salt,ts,sign = get_salt_sigin_ts(word)
    # url地址为
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    headers = {
        "Content-Length": "236",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=-1979821903@10.108.160.17; JSESSIONID=aaa0bDIRmBxz_eQHrRIWw; OUTFOX_SEARCH_USER_ID_NCOO=1827880986.4182167; ___rl__test__cookies=1563949990154",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    #代理IP,
    proxies = {
        'http': 'http://475199896:2gadbghh@223.111.182.70:16818',
        'https': 'http://223.111.182.70:16818'
    }
    data = {
        "i": word,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign,
        "ts": ts,
        "bv": "65313ac0ff6808a532a1d4971304070e",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME",
    }
    html_json = requests.post(url=url,data=data,headers=headers,proxies=proxies).json()
    return html_json

if __name__ == '__main__':
    word = input('请输入要翻译的英文单词>> ')
    result = attack_yd(word)['translateResult'][0][0]['tgt']
    print(result)