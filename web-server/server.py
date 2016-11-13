#-*- coding:utf-8 -*-
import os
import sys
import BaseHTTPServer
import subprocess

Cases = [case_no_file(),
         case_always_fail(),
         case_directory_index_file(),
         case_existing_file(),
         case_cgi_file()]

class case_cgi_file(object):
    def test(self, handler):

    return os.path.isfile(handler.full_path) and \
            handler.full_path.endswith('.py')

    def act(self, handler):
        handler.run_cgi(handler.full_path)

def run_cgi(self,full_path):
    data = subprocess.check_output(["python", handler.full_path])

class case_directory_index_file(object):

    def index_path(self,handler):
        return os.path.join(handler.full_path, 'index.html')

    def test(self, handler):
        return os.path.isdir(handler.full_path) and \
            os.path.isfile(self.index_path(handler))

    def act(self, handler):
        handler.handle_file(self.index_path(handler))

class case_no_file(object):

    def test(self, handler):
        return not os.path.exists(handler.full_path)

    def act(self, hanler):
        raise ServerException("'{0}' not found".format(self.full_path))

class case_existing_file(object):

    def test(self, handler):
        return os.path.isfile(handler.full_path)

    def act(self, handler):
        handler.handle_file(handler.full_path)

class case_always_fail(object):

    def test(self, handler):
        return True

    def act(self, handler):
        raise ServerException("Unknown object '{0}'".format(handler.path))


class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    #处理请求
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
            full_path = os.getcwd() + self.path

            for case in self.Cases:
                handler = case()
                if handler.test(self):
                    handler.act(self)
                    break

        except Exception as msg:

            self.handle_error(msg)

    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content, 404)

    def create_page(self):
        value = {
            'date_time' : self.date_time_string(),
            'client_host': self.client_address[0],
            'client_port': self.client_address[1],
            'command'  : self.command,
            'path'  : self.path
        }
        page = self.Page.format(**values)
        return page

    def send_content(self, page):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(page)

    def handle_file(self, full_path):
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
            self.send_content(content)
        except IOError as msg:
            msg = "'{0} connot be read: {1}".format(self.path, msg)
            self.handle_error(msg)


#服务器运行
if __name__ == "__main__":
    serveradress = ('', 8080)
    server = BaseHTTPServer.HTTPServer(serveradress, RequestHandler)
    server.serve_forever()

#服务器的异常类
class ServerException(Exception):
    pass



