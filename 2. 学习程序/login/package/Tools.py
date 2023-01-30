"""
# PyCharm Tools
# 2023.01.30
# TanBQ.
"""

import platform
import os


# 检测系统，用来做清空控制台
def SystemCheck():
    """
    此函数作用:检测系统版本
    - 由于系统不同，清空控制台方法也不同
    - Windows版本是cls
    - macOS或linux之类的可以用clean
    所以通过简单的检测方便后续的清空
    """

    os_name = platform.platform()
    OS_Info = "Windows" if os_name[:7] == 'Windows' else 'macOS'
    if OS_Info in {'Windows', 'macOS'}:
        # 如果系统的开头是这两个的话
        # 返回验证信息 = 对
        return 'Y'
    print("由于只在Windows 10和macOS 13上完成了测试")
    print("由于作者手里只有两台设备")
    print("请使用「Windows10+」或者「macOS 13+」的系统")
    return 'N'


def ClearConsole():
    if platform.platform()[:7] == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def StopConsole():
    if platform.platform()[:7] == 'Windows':
        os.system('read')
    else:
        os.system('read')
