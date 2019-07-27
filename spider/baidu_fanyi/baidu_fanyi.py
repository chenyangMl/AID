"""
POST地址: https://fanyi.baidu.com/v2transapi
Form Data
    from: en
    to: zh
    query: word
    transtype: realtime
    simple_means_flag: 3
    sign: 210056.513977
    token: 231e5788be2651ee5408f825643c0b0

主要技术点:
    sign的生成: js代码生成
    token的获取: 通过响应页面获取token值

"""

import requests
import re
import execjs

class BaiduTrans():
    def __init__(self):
        self.get_url = 'https://fanyi.baidu.com/?aldtype=16047'
        self.post_url = 'https://fanyi.baidu.com/v2transapi'
        self.headers = {
            # "authority": "fanyi.baidu.com",
            # "method": "GET",
            # "path": "/?aldtype=16047",
            # "scheme": "https",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "max-age=0",
            "cookie": "BAIDUID=B8F4A17856D9E9818B8EC520C35EBC0A:FG=1; BIDUPSID=B8F4A17856D9E9818B8EC520C35EBC0A; PSTM=1561686472; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; delPer=0; PSINO=1; H_PS_PSSID=1455_21118_29578_29518_28519_29098_29568_28832_29220_26350; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1563930183,1563954548,1563958803,1564019773; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1564026400; yjs_js_security_passport=0b76d735a294170c6a77b0e78b0502781b465702_1564026454_js",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.3",
        }
        self.post_headers = {
            "authority": "fanyi.baidu.com",
            "method": "POST",
            "path": "/v2transapi",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "content-length": "120",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "cookie": "BAIDUID=B8F4A17856D9E9818B8EC520C35EBC0A:FG=1; BIDUPSID=B8F4A17856D9E9818B8EC520C35EBC0A; PSTM=1561686472; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; delPer=0; PSINO=1; H_PS_PSSID=1455_21118_29578_29518_28519_29098_29568_28832_29220_26350; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1563954548,1563958803,1564019773,1564030427; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1564030427; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; yjs_js_security_passport=9041b97c809a0a65041ff0383e580ddac9894c34_1564030427_js",
            "origin": "https://fanyi.baidu.com",
            "referer": "https://fanyi.baidu.com/translate?aldtype=16047&query=as&keyfrom=baidu&smartresult=dict&lang=auto2zh",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
        }

    def get_sign(self,word):
        with open('baidu.js') as f:
            js_data = f.read()
        execjs_obj = execjs.compile(js_data)
        # 使用eval将字符串当着表达式执行
        sign = execjs_obj.eval('e("{}")'.format(word))
        return sign

    def get_token(self):
        html = requests.get(url=self.get_url,
                            headers= self.headers).text
        pattern = re.compile("token: '(.*?)'",re.S)
        return pattern.findall(html)[0]

    def create_form_data(self,word,fromLag,toLag):
        token = self.get_token()
        sign = self.get_sign(word)
        form_data = {
            "from":fromLag,
            "to":toLag,
            "query":word,
            "transtype":"realtime",
            "simple_means_flag":"3",
            "sign":str(sign),
            "token": str(token)
        }
        return form_data

    def main(self):
        print("""
        ==========选择翻译类型============
        > 1: 英文-中文
        > 2: 中文-英文
        ================================        
        """)
        while True:
            trans_type = input('请选择翻译类型(1或2)>>')
            trans_types = {'1': ['en', 'zh'],
                           '2': ['zh', 'en']}
            if trans_type not in trans_types:
                print('请重写输入类型:')
                continue
            else:
                fromLag = trans_types[trans_type][0]
                toLag = trans_types[trans_type][1]
                break

        while True:
            word = input('输入查询词:')
            form_data = self.create_form_data(word,fromLag,toLag)
            json = requests.post(url=self.post_url,
                                 data=form_data,
                                 headers=self.post_headers).json()

            print('结果>>',json['trans_result']['data'][0]['dst'])

if __name__ == '__main__':
    BaiduTrans().main()
