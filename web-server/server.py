#-*- coding:utf-8 -*-
import os
import sys
import BaseHTTPServer
import subprocess

#服务内部错误
class ServerException(Exception):
    pass

class base_case(object):

    def handle_file(self, handler, full_path):
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
            self.send_content(content)
        except IOError as msg:
            msg = "'{0} connot be read: {1}".format(self.path, msg)
            handler.handle_error(msg)
        def index_path(self, handler):
            return os.path.join(handler.full_path, "index.html")

        def test(self, handler):
            assert False, 'Not implemented.'

        def tact(self, handler):
            assert False, 'Not implemented.'


class case_cgi_file(base_case):
    def test(self, handler):

        return os.path.isfile(handler.full_path), handler.full_path.endswith('.py')

    def act(self, handler):
        handler.run_cgi(handler)

        def run_cgi(self,full_path):
            data = subprocess.check_output(["python", handler.full_path])



class case_directory_index_file(base_case):
    #返回根路径下的主页文件
    def index_path(self,handler):
        return os.path.join(handler.full_path, 'index.html')

    def test(self, handler):
        return os.path.isdir(handler.full_path) and \
            os.path.isfile(self.index_path(handler))

    def act(self, handler):
        handler.handle_file(self.index_path(handler))

class case_no_file(base_case):

    #文件或目录不存在
    def test(self, handler):
        return not os.path.exists(handler.full_path)

    def act(self, handler):
        raise ServerException("'{0}' not found".format(handler.full_path))



class case_existing_file(base_case):
    #文件存在的情况
    def test(self, handler):
        return os.path.isfile(handler.full_path)

    def act(self, handler):
        handler.handle_file(handler, handler.full_path)



class case_always_fail(base_case):
    #一直请求失败
    def test(self, handler):
        return True

    def act(self, handler):
        raise ServerException("Unknown object '{0}'".format(handler.path))


class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    Cases = [case_no_file(),
             case_always_fail(),
             case_directory_index_file(),
             case_existing_file(),
             case_cgi_file()]
    #错误页面
    Error_Page = '''\
    <html?
    <body>
    <h1>Error accessing {path}</h1>
    <p>{msg}</P>
    </body>
    </html>
    '''

    #重新定义do_GET函数
    def do_GET(self):
        try:
            #完整请求路径
            self.full_path = os.getcwd() + self.path

            #根据请求情况找到合适处理方法
            for case in self.Cases:
                if case.test(self):
                    case.act(self)
                    break
        #请求不到路径的异常处理方法
        except Exception as msg:
            self.handle_error(msg)

    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content, 404)


    def send_content(self, content, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)


#服务器运行
if __name__ == "__main__":
    serveradress = ('', 8080)
    server = BaseHTTPServer.HTTPServer(serveradress, RequestHandler)
    server.serve_forever()

#服务器的异常类
class ServerException(Exception):
    pass



