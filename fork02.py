"""
信号处理僵尸
"""
import os
import signal
import time

# 子进程退出时父进程忽略退出行为，子进程由系统处理
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

pid = os.fork()

if pid < 0:
    print("进程创建失败")
elif pid == 0:
    time.sleep(2)
    print("child PID", os.getpid())
    os._exit(0)
else:
    time.sleep(5)
    print("father PID", os.getppid())