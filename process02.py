"""
给进程函数传参
"""
from multiprocessing import Process
import time


# 带参数的进程函数
def worker(sec_, name):
    for i in range(3):
        time.sleep(sec_)
        print("I'm '%s'" % name)
        print("I'm working...")


p = Process(target=worker, args=(2,), kwargs={'name':'小木'})
p.start()
p.join()
