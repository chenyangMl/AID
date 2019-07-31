Python-Spider
==========

© ANTCODE

注: 案例用于技术分享,转载请注明。 

# 爬虫案例
```text
> 网站网页大体可分为静态网页和动态网页两大类，静态页面指浏览器请求地址(URL)时服务端会将带有数据的页面(html)直接返回给浏览器渲染显示。
动态页面指浏览器请求地址(URL)时服务端返回带有JS的页面(html),页面中的数据通过JS异步请求获取或者通过JS重定向。

> 怎么判断一个网站页面是否为静态页面？
     通过页面右键查看源代码，再在源代码中搜索需要获取数据关键词，能够获取到即为静态页面。
```

### 1. 爬取静态网站
#### 1.1 爬取猫眼电影榜单信息
- 简介: 
> 地址: https://maoyan.com/board/4?offset={}

> 该地址为猫眼电影的榜单信息地址,通过下一页观察地址,可以发现offset会有规律的变化.通过总结规律便可
使用程序模拟人为点击爬取这些榜单信息。主要演示通过请求一级页面获取结构化数据。
- 主要技术:
> 示例代码中使用python的标准库模块
>> 请求: urllib.request
>> 解析: 使用正则re
- 示例代码: [maoyan.py]()


#### 1.2 电影天堂电影信息
- 简介；
> 地址: https://www.dytt8.net/html/gndy/dyzz/list_23_1.html

>> 该示例主要演示抓取一级页面信息 和 二级页面信息并保存到mysql数据中。
- 主要技术:
>> urllib.request, re, pymysql
- 示例代码: [dytt.py]()

#### 1.3  链家二手房信息
- 简介:
> 地址: https://bj.lianjia.com/ershoufang/pg2/
- 主要技术：
>> urllib.request, re, pymysql
- 示例代码: [lianjia.py]()

#### 1.4 爬取指定百度贴吧名中的图片和视频
- 简介：
> 地址: http://tieba.baidu.com/f?kw={}&pn={}
> 该示例主要演示通过requests模块来实现模拟请求获取响应，并通过Xpath来匹配需要的元素信息，Xpath其实是使用于XML的一种标记语言，但同时也适用于
HTML文档中元素的匹配。
- 主要技术：
>> 请求: 第三方requests
>> 解析: 基于Xpath的 lxml
- 示例代码: [baidutieba.py]()


### 2.爬取动态网页
- 获取动态网页的真实地址.
> 打开F12--> network -->抓取实际数据的XHR请求.
####2.0 爬取民政部每月最新行政区分码
- 示例代码 [xinzhen.py]()

#### 2.1 爬取腾讯招聘信息
- 简介: 
> 腾讯招聘网站做了动态页面的反爬措施，当浏览器访问网站地址时响应回来的html中并没有需要信息，
通过抓包发现其实是使用了AJAX做了异步数据请求。真实的数据在AJAX请求响应回来的json串中。
该示例演示爬取动态页面的json数据相关操作.

- 示例代码: [tencent-career.py]()

#### 2.2 爬取豆瓣电影榜单信息
- 简介:

- 示例代码:[douban.py]()

#### 2.3 爬取B站短视频
- 简介:
> B站的的短视频是用户滚动滑轮时动态加载的，所有在抓取时需要获取其动态链接.
- 主要技术点
> 1. 非结构化数据视频的获取: requests.get(url,headers).content
 
- 示例代码: [bilibili.py]()

#### 2.4 基于多线程的小米应用商店爬取
- 示例代码 [xiaomi.py]()

#### 2.5 基于selenimum+Chrome的京东商城

- 示例代码[jd.py]()

#### 2.5 模拟有道翻译
- 简介: 
有道翻译在翻译单词时，通过Ajax向服务端发送了POST请求,后端服务器对请求头中几项内容做了一些加密的反爬措施。
在模拟这类请求时，不仅需要获取动态API接口，还应在程序中做一样的加密处理，再进行post请求才可能通过后台验证实现响应。
- 有道的主要反爬策略
> 1. Ajax的局部post请求
> 2. 对请求头中的refer, User-Agent,Cookie,
> 3. IP请求次数限制，（IP很容易被封，建议使用代理IP测试）
> 4. Form Data 中的部分数据进行了加密
- 主要技术
> 1. 重点： 分析Form data中那些内容做了加密，解析JS代码中对该内容的具体加密手段，在程序中同步实现该过程即可。
> 2. post请求:  requests.post(url,data,headers) 

- 示例代码: [youdao.py]()

#### 2.5 模拟百度翻译
- 简介:baidu_fanyi.py
- 主要技术
```text
Form Data
    from: en
    to: zh
    query: word
    transtype: realtime
    simple_means_flag: 3
    sign: 210056.513977
    token: 231e5788be2651ee5408f825643c0b0
```
> 1. sign加密
>> 重点: 分析Form Data数据加密过程， 使用pyexecjs模拟的源代码的中的sign加密过程.
> 2. token生成.
>> 通过解析JS代码发现token是获取的暂存
> 3. Cookies

### Cookie,Session模拟登录案例
- 人人网