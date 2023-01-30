"""
# PyCharm app
# 2023.01.29
# TanBQ.
"""

from package.Account import *
from package.File import *
from package.Tools import *
from datetime import datetime
from sys import exit

# 由于pickle模块默认输出的文件扩展名是pkl
# 所以创建一个用户数据的变量
User_list = {}
Logined_user: str = ""
UserDataFile = 'UserData.pkl'

"""
# 导入的注释
 - Account -> 创建用户对象,加密密码
 - File -> 数据的导入、保存、文件是否存在
 - Tools -> 暂停控制台、清空控制台、检测平台
# 变量的注释
 - User_list -> 存放用户数据的字典
 - Logined_user -> 存放已经登陆的用户的账号
 - UserDataFile -> 外部存放用户数据文件[默认在根目录下data文件里]
"""


def appTitle():
    """
    启动界面的标题
     - 通过返回值去指定功能
    """
    today = datetime.now()
    week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    print(f"""
        {today.year}.{today.month}.{today.day} - {week_list[today.weekday()]}
        xxxxx系统
    1. 登陆       2. 注册
    3. 找回       4. 退出
    """)
    return input("请输入序号.\n@echo: ")


def login():
    """
    登陆函数
     - 如果账号(邮箱)和密码匹配,返回True
     - 要调用Account,使用encipherment去生成密钥
     - 最后匹配输入的密码是否一致
    """
    account_list = list(User_list.keys())
    account = input("请输入账号: ")
    password = input("请输入密码: ")
    if account not in account_list:
        return False
    if encipherment(account, password) == User_list[account].password:
        global Logined_user
        Logined_user = User_list[account].name
        return True


def register():
    """
    注册函数
     - 通过调用Account类,生成一个用户,并作为对象赋值给_
     - 通过键值对[账号(邮箱), 对象]存放用户信息 -> dict
     - 账户(邮箱)作为键,用它来检测是否重复
    """
    _ = Register()
    if User_list.get(_.email, None):
        print("该邮箱已经注册过")
        return False
    else:
        User_list[_.email] = _
        return True


def launchApp():
    """
    未来登陆后需要完成的事情
    """
    print("例子: 打印用户数据信息")
    for name in User_list:
        print(User_list[name])


if __name__ == '__main__':
    User_list = loadDataFile(UserDataFile)
    while SystemCheck() == 'Y':
        ClearConsole()
        match appTitle():
            case '1':
                ClearConsole()
                if login():
                    print(f"你好{Logined_user}")
                    launchApp()
                else:
                    print("账号或密码错误")
            case '2':
                ClearConsole()
                if register():
                    saveDataFile(User_list, UserDataFile)
                    launchApp()
            case '4':
                exit()
            case _:
                print("输入有误，请重新输入")
        StopConsole()
