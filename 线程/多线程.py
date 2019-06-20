#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process
import os

def run_proc(name):
    print("Run child process %s (%s)..." % (name, os.getpid()))

if __name__ == '__main__':
    print("Parent process %s." % os.getpid())
    """
    创建子进行时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动。
    """
    p = Process(target=run_proc, args=('test',))
    print("Process will start.")
    p.start()  # start()方法启动。
    p.join()  # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print("Process end.")
