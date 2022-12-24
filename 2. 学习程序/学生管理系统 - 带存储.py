"""
# 学生管理系统.py Beta2.3
# 2022.12.24
# TanBQ.
"""

# 经过了很长时间的学习，这个版本增加了本地的存储
# 运行后会在本文件的同级目录生成一个「UserData.pkl」的文件
# 是用来保存用户生成的文件的
# 下面是一边学习一边写出来的源码

"""工具类函数"""
import platform
# 检测系统，用来做清空控制台
def SystemCheck():
    """
    此函数作用:检测系统版本
    - 由于系统不同，清空控制台方法也不同
    - Windows版本是cls
    - macOS或linux之类的可以用clean
    所以通过简单的检测方便后续的清空
    """

    import platform
    os_name = platform.platform()
    if os_name[:7] == 'Windows':
        OS_Info = "Windows"
    else:
        OS_Info = 'macOS'

    # 获取系统版本
    if OS_Info in ['Windows', 'macOS']:
        # 如果系统的开头是这两个的话
        # 返回验证信息 = 对
        return 'Y'
    else:
        print("由于只在Windows 10和macOS 13上完成了测试")
        print("由于作者手里只有两台设备")
        print("请使用「Windows10+」或者「macOS 13+」的系统")
        return 'N'

def ClearConsole():
    import os
    if platform.platform()[:7] == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

# 后面两个函数需要这个模块
import pickle
from pathlib import Path
# 获取当前目录
def getPath(UserFile):
    return Path.cwd() / UserFile

# 检查数据文件是否存在
def checkDataFile(UserFile):
    Data = getPath(UserFile)
    if not Data.exists():
        with open(Data, 'wb') as f:
            return 'Empty'
    else:
        with open(Data, 'rb') as f:
            if not f.readlines():
                return 'Empty'

# 读取用户数据文件
def loadDataFile(UserFile):
    Data = getPath(UserFile)
    with open(Data, 'rb') as file:
        loadInfo = pickle.load(file)
    return loadInfo

# 保存用户数据文件
def saveDataFile(UserFile):
    Data = getPath(UserFile)
    with open(Data, 'wb') as file:
        pickle.dump(Student_info, file)

"""功能性函数"""
# 标题
def Title():
    """
    作用:显示标题
    """
    print('-' * 40)
    print(f"""
        >>{Today.year}-{Today.month}-{Today.day}.{week_list[Today.weekday()]}<<
        >>欢迎使用学生管理系统<<\n
    1. 添加学生         2. 删除学生
    3. 修改学生         4. 查询学生
    5. 显示学生         6. 推出系统
    """)
    print('-' * 40)

# 添加信息
def addInfo():
    # print("\n" * 10)
    print('-' * 40)
    stdID = input('学生学号: ')
    stdName = input('学生姓名: ')
    stdSex = input('学生性别: ')
    stdBirth = input('出生年月: ')
    stdAge = Today.year - int(stdBirth[:4:])
    print('-' * 40, end='')

    # 如果姓名和学号都重复说明学生存在，不存储
    for each in Student_info:
        if each['stdID'] == stdID or each['stdName'] == stdName:
            print("\n>>系统提示:有重复项.<<", end='')
            input()
            return
    # 如果学生信息不存在则添加学生信息
    stdDict = dict()
    stdDict['stdID'] = stdID
    stdDict['stdName'] = stdName
    stdDict['stdSex'] = stdSex
    stdDict['stdAge'] = stdAge
    stdDict['stdBirth'] = stdBirth
    Student_info.append(stdDict)
    input()

# 删除信息
def delInfo():
    # print("\n" * 10)
    print('-' * 40)
    delID = input("请输入要删除的学号: ")
    for each in Student_info:
        if each['stdID'] == delID:
            print(f"""
            查到需要删除的信息：
             >学号: {each['stdID']}
             >姓名: {each['stdName']}
             >性别: {each['stdSex']}
        \n输入Y删除: """, end='')
            if input() in ['y', 'Y']:
                Student_info.remove(each)
            print('-' * 40, end='')
            input()
            return
    # 这个else是对应的for循环
    else:
        print(">>查无此人<<")
        print('-' * 40, end='')
        input()
        return

# 修改信息
def modifyInfo():
    # print("\n" * 10)
    print('-' * 40)
    modifyID = input("请输入要修改的学号: ")
    if not Student_info:
        print(">>信息为空<<")
        print('-' * 40, end='')
        input()
        return
    for each in Student_info:
        if each['stdID'] == modifyID:
            print(f"""
            查到需要删除的信息：
             >学号: {each['stdID']}
             >姓名: {each['stdName']}
             >性别: {each['stdSex']}
             >年龄: {each['stdAge']}
             >生日: {each['stdBirth']}\n
        >>请输入你要修改的序号<<
    1. 学生学号         2. 学生姓名
    3. 学生性别         4. 出生日期
    输入其他退出""")
            while True:
                User_in = input('    @echo >> ')
                if User_in in ['1', '2', '3', '4']:
                    if User_in == '1':
                        each['stdID'] = input('    学生学号: ')
                    elif User_in == '2':
                        each['stdName'] = input('    学生姓名: ')
                    elif User_in == '3':
                        each['stdSex'] = input('    学生性别: ')
                    else:
                        _ = input('    出生日期: ')
                        each['stdBirth'] = Today.year - int(_[:4:])
                    continue
                else:
                    print("        >>系统提示:已退出修改.<<", end='')
                    input()
                    return
            print('-' * 40, end='')
            input()
            return
    # 注意这个else对应的是for循环的！！！
    else:
        print(">>查无此人<<")
        print('-' * 40, end='')
        input()
        return

# 查找信息
def findInfo():
    Flag = 0
    # print("\n" * 10)
    print('-' * 40)
    findName = input("请输入要查找的姓名: ")
    for each in Student_info:
        if each['stdName'] == findName:
            print(f"""
            查找到如下信息：
             >学号: {each['stdID']}
             >姓名: {each['stdName']}
             >性别: {each['stdSex']}
             >年龄: {each['stdAge']}
             >生日: {each['stdBirth']}
            """)
            print('-' * 40, end='')
            input()
            return
    if Flag == 0:
        print(">>查无此人<<")
        print('-' * 40, end='')
        input()
        return

# 显示学生信息
def showInfo():
    # print("\n" * 10)
    print('-' * 40)
    print("学号\t\t姓名\t\t性别\t\t年龄")
    for each in Student_info:
        print(f"{each['stdID']}\t\t{each['stdName']}\t\t{each['stdSex']}\t\t{each['stdAge']}")
    print('-' * 40, end='')
    input()


"""主函数"""
def StudentManagementSystem():
    ClearConsole()
    # 检测系统
    sys_info = SystemCheck()
    while sys_info == 'Y':
        Title()
        select = input("输入你想操作对象的序号:\n@echo >> ")
        ClearConsole()
        if select == '6':
            print("\n\n\n\t\t\t欢迎下次使用\n\n\n")
            break
        elif select == '1':
            addInfo()
        elif select == '2':
            delInfo()
        elif select == '3':
            modifyInfo()
        elif select == '4':
            findInfo()
        elif select == '5':
            showInfo()
        ClearConsole()


if __name__ == '__main__':
    # By_TanBQ_2022

    # 获取系统时间
    import datetime
    Today = datetime.datetime.today()
    # 创建一个星期列表用来输出
    week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    # 用来存放学生信息的列表
    Student_info = list()
    # 检测数据文件，如果没有，就创建
    # 有的话，无视
    # 由于pickle模块默认输出的文件扩展名是pkl
    # 所以创建一个用户数据的变量
    UserDataFile = 'UserData.pkl'
    if not checkDataFile(UserDataFile) == 'Empty':
        Student_info = loadDataFile(UserDataFile)
    StudentManagementSystem()
    saveDataFile(UserDataFile)
