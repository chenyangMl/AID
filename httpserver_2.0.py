"""
httpserver 1.0: C_IO网络编程/0508/httpserver_1.0/http_server.py
        多进程　os.fork()

Httpserver 2.0
    升级点: ＊　IO并发处理
           ＊　基本的request解析
           ＊　使用类封装

技术点：
    1 使用tcp通信
    2 select io多路复用

结构:
    1. 采用类封装

类的接口设计：
    1.在用户使用角度进行工作流程设计
    2.尽可能提供全面的功能，能为用户决定的在类中实现
    3.不能替用户决定的变量可以通过实例话对象传入类中
    4. 不能替用户决定的复杂功能，可以通过重写让用户自己决定
"""
from socket import *
from select import select

# 将具体的http server 功能封装
class HTTPServer:
    def __init__(self,server_addr,static_dir):
        self.server_addr, self.static_dir = server_addr,static_dir
        self.rlist = self.wlist = self.xlist = []
        self._create_socket()
        self._bind()

    def _create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)

    def _bind(self):
        self.sockfd.bind(self.server_addr)
        self.port = self.server_addr[1]

    #处理客户端请求
    def _handle(self,connfd):
        #接收请求
        request = connfd.recv(4096)
        #防止浏览器断开
        if not request:
            #当浏览器关闭时，移除对该IO发生的监听
            self.rlist.remove(connfd)
            connfd.close()
            return
        #请求解析
        #对http请求进行按行切割，按空格切割
        #获取请求行　Get / http/1.1
        request_line = request.splitlines()[0]
        # 获取请求内容
        info = request_line.decode().split(" ")[1]
        # print(coonfd.getpeername(),":",info)
        # 将请求内容info分为访问网页和其他
        if info == "/" or info[-5:] ==".html":
            self._get_html(connfd,info)
        else:
            self._get_data(connfd,info)

        self.rlist.remove(connfd)
        connfd.close()

    #根据请求内容info,返回具体网页
    def _get_html(self,connfd,info):
        if info == "/":
            #将主页打开发送给客户端
            filename = self.static_dir+"/index.html"
        else:
            filename = self.static_dir + info
        try:
            fd  = open(filename)
        except Exception:
            #如果无法打开网页，发送404
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type: text/html\r\n"
            response += "\r\n"
            response += "<h1>Not Found...</h1>"
        else:
            #如果正常打开，发送200,及内容
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type: text/html\r\n"
            response += "\r\n"
            response += fd.read()
        finally:
            connfd.send(response.encode())

    # 处理其他情况
    def _get_data(self,connfd,info):
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: text/html\r\n"
        response += "\r\n"
        response += "<h1>Waiting httpserver 3.0...</h1>"
        connfd.send(response.encode())

    #启动服务
    def server_forever(self):
        self.sockfd.listen(5)
        print("Listen thr port %s"%self.port)
        self.rlist.append(self.sockfd)
        #循环监控IO发生
        while True:
            rs,ws,xs = select(self.rlist,self.wlist,self.xlist)
            for r in rs:
                if r == self.sockfd:
                    c,addr = r.accept()
                    print("Connect for ",addr)
                    self.rlist.append(c)
                else:
                    self._handle(r)

#如何使用HTTPServer类
if __name__ == '__main__':
    # 用户自己决定：服务端绑定地址，展示内容
    SERVER_ADDR = ("0.0.0.0",8888)
    static_dir = "./static" #网页存放目录

    httpd = HTTPServer(SERVER_ADDR,static_dir) #生成实例对象
    httpd.server_forever() #启动服务
