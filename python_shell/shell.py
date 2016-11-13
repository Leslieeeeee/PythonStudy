#coding:utf-8
import os
import sys
import shlex
import getpass
import socket
import signal
import subprocess
import platform
from func import *


built_in_cmds = {}
#注册命令，即建立定义函数与命令之间的对应关系
def set_command(name,func):

        built_in_cmds[name] = func

def init():

    set_command("cd", cd)
    set_command("exit", exit)
    set_command("history", history)
    set_command("getenv", getenv)

def shell_loop():
    status = run_status

    while status == run_status:

        #打印出$
        run_shell()

        #忽略ctrl-z和ctrl-c
        ignore_signals()
        try:
            #读取命令
            cmd = sys.stdin.readline()
            #解析命令
            cmd_anlysis = tokenize(cmd)
            #执行命令
            cmd_anlysis = preprocess(cmd_anlysis)
            #回到初始状态
            status = execute(cmd_anlysis)

        except:
            _, err, _ = sys.exc_info()
            #sys.exc_info(type, value, traceback)
            #返回正在处理的异常
            print'err'

def main():

    init()

    shell_loop()

if __name__ == '__main__':

    main()


def run_shell():

    user = getpass.getuser()

    hostname = socket.gethostname()
    #获得主机的名字
    #如果后面带上了参数（一个域名），则可以分析出它的IP地址

    cwd = os.getcwd()

    bash_dir = os.path.basename(cwd)

    home_dir = os.path.expanduser("~")
    if cwd == home_dir:
        bash_dir = "~"

    if platform.system() != "Windows":
        sys.stdout.write("[033[1;33m%s\033[0;0m@％s \033[1;36m%s\033[0;0m]$") %(user, hostname, bash_dir)
    else:
        sys.stdout.write("[%s@%s %s]$") %(user, hostname, bash_dir)

    sys.stdout.flush()
    #标准输出，一秒输出一个数字
    #Linux中必须加这条语句才可以实现一秒输出一个数字，win 下可以不加


def ignore_signals():

    if platform.system != "Windows":
        #忽略ctrl-z信号
        signal.signal(signal.SIGTSTP, signal.SIG_IGN)
        #忽略ctrl-c信号
        signal.signal(signal.SIGINT, signal.SIG_IGN)

def tokenize(string):

    tokens = shlex.split(string)
    return tokens

def preprocess(tokens):

    preprocess_anlysis = []

    for token in tokens:
        if token.startswith('$'):
            preprocess_anlysis.append(os.getenv(token[1:]))
        else:
            preprocess_anlysis(token)
    return preprocess_anlysis

#进程被强制中断时触发
def handler_kill(signum, frame):
    raise OSError("Killed!")

#进程被中断时触发
def execute(cmd_anlysis):

    with open(HISTORY_PATH, 'a') as history_file:
        history_file.write(''.join(cmd_anlysis) + os.linesep)
    #os.linesep给出当前操作系统使用的行终止符
    if cmd_anlysis:

        cmd_name = cmd_anlysis[0]
        cmd_args = cmd_anlysis[1:]

        if cmd_name in built_in_cmds:
            return  built_in_cmds[cmd_name](cmd_args)

        signal.signal(signal.SIGINT, handler_kill)

        if platform.system() !="Windows":

            p = subprocess.Popen(cmd_anlysis)#执行程序或者列表的第一项
            p.communicate()

        else:

            command = ''
            command = ' '.join(cmd_anlysis)
            os.system(command)

        return run_status

