"""
# PyCharm File
# 2023.01.29
# TanBQ.
"""

# 后面两个函数需要这个模块
import pickle
from pathlib import Path
from package.Account import *


# 获取当前目录
def getPath(UserFile):
    newDir = Path.cwd() / "data"
    newDir.mkdir(exist_ok=True)
    return newDir / UserFile


# 读取用户数据文件
def loadDataFile(UserFile) -> list[Account]:
    # 这里是因为有类，所以需要加这个
    Data = getPath(UserFile)
    if Data.exists():
        with open(Data, 'rb') as file:
            return pickle.load(file)
    else:
        return {}

# 保存用户数据文件
def saveDataFile(info, UserFile):
    Data = getPath(UserFile)
    with open(Data, 'wb') as file:
        pickle.dump(info, file)
