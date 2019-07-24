"""
创建二级子进程处理僵尸
"""
import os
import time

pid = os.fork()

if pid < 0:
    print("进程创建失败")
# 一级子进程
elif pid == 0:
    p = os.fork()
    if pid == 0:
        time.sleep(1)
        print("二级子进程")
    else:
        os._exit(0)
# 一级父进程
else:

    os.wait()  # 等待一级子进程退出
    time.sleep(3)
    print("一级父进程")
print("父子进程同时执行部分")