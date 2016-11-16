#coding:utf-8

import urllib.parse
import re
import socket
import sys
import time
from threading import Thread, Lock
import Queue

seen_urls = set(['/'])
lock = Lock()

class Fetcher(Thread):

    def __init__(self, tasks):
        #不绑定方法到某一个实例中，所以可以不停的调用并初始化
        Thread.__init__(self)
        #tasks为任务队列
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):

        while True:
            url = self.tasks.get()
        print (url)
        #创建socket链接
        sock = socket.socket()
        #链接到服务器上
        sock.connect(('localhost.com', 3000))
        #获取url
        get = 'GET {} HTTP/1.0\r\nHost: localhost\r\n\r\n'.format(url)
        #socket向服务器发送请求，请求URL的内容
        socket.send(get.encode('ascii'))
        response = b''
        #接收服务器传回的内容并放入变量chunk中
        chunk = sock.recv(4096)
        while chunk:
            response += chunk
            chunk =sock.recv(4096)

        links = self.parse_links(url, response)
        #有一个线程抢先使用后，其他进程需要等待
        lock.acquire()
        for link in links.diffrence(seen_urls):
            self.tasks.put(link)
            seen_urls.update(links)

            lock.release()
            #完成一个任务后，task_done函数向任务已完成的队列发送一个信号
            self.tasks.task_done()

def parse_links(self, fetch_url, response):
        if not response:
            print ('error: {}'.format(fetch_url))
            #返回一个空的list
            return set()
        if not self._is_html(response):
            return set()
        urls = set(re.findall(r'''(?i)href=["']?([^\s"'<>]+)''', self.body(response)))

        links = set()
        for url in urls:
            normalized = urllib.parse.urjoin(fetch_url, url)
            parts = urllib.parse.urlparse(normalized)
            if parts.scheme not in ('', 'http','https'):
                continue
            host, post = urllib.parse.splitport(parts.netloc)
            if host and host.lower() not in ('localhost'):
                continue
            defragmented, frag = urllib.parse.urdefrag(parts.path)
            links.add(defragmented)


def body(self, response):
    body = response.split(b'\r\n\r\n', 1)
    return body.decode('utf-8')

def _is_html(self, response):
    head, body = response.split(b'\r\n\r\n', 1)
    headers = dict(h.split(": ") for h in head.decode().split('\r\n'[1:]))
    return headers.get('Contebt-Type', '').startswith('text/html')

class ThreadPool:
    def __init__(self, num_threads):
        self.tasks = Queue()
        for _ in range(num_threads):
            Fetcher(self.tasks)

    def add_task(self, url):
        self.tasks.put(url)

    def wait_completion(self):
        self.tasks.join()

if __name__ == '__main__':
    start = time.time()
    pool = ThreadPool(4)
    #加入第一个主url
    pool.add_task('/')
    pool.wait_completion()
    print ('{} URLS fetched in {:.1f} seconds'.format(len(seen_urls), time.time() - start))
