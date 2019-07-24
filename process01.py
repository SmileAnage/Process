"""
创建多个进程
"""
from multiprocessing import Process
import time
import os


def fun01():
    time.sleep(3)
    print("吃饭")
    print(os.getppid(), '--', os.getpid())


def fun02():
    time.sleep(2)
    print("睡觉")
    print(os.getppid(), '--', os.getpid())


def fun03():
    time.sleep(4)
    print("打豆豆")
    print(os.getppid(), '--', os.getpid())


# 关联函数
things = [fun01, fun02, fun03]
jobs = []

# 循环处理进程并存入列表中
for i in things:
    p = Process(target=i)
    jobs.append(p)
    p.start()

# 循环回收进程
for i in jobs:
    i.join()
