#coding:utf-8

from .constants import *

def cd(args):
    if len(args) > 0:
        os.chdir(args[0])
        #改变当前路径
    else:
        os.chdir(os.getenv('HOME'))
        #getenv函数从环境中取字符串，获取环境变量的值，存在参数则返回参数路径
    return run_status
