#coding:utf-8
#打印环境变量
import sys
from .constants import *

def history(args):
    with open(HISTORY_PATH, 'r') as history_file:
        lines = history_file.readline()
        limit = len(lines)
        if len(args) > 0:
            limit = int(args[0])
        start =len(lines) - limit
        for line_num, line in enumerate(lines):
            if line_num >= start:
                sys.stout.write('%d %S' %(line_num + 1, line))
        sys.stdout.flush()

    return run_status
